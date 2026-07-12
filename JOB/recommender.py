# recommender.py
# This file recommends jobs by comparing resume text with job descriptions.

import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from skill_extractor import SKILLS_LIST


def preprocess(text):
    """Convert text to lowercase and remove special characters."""
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_dataset(csv_path):
    """Load the job dataset and prepare one text column for matching."""
    jobs_df = pd.read_csv(csv_path)

    jobs_df["combined_text"] = (
        jobs_df["Job Title"].fillna("") + " " +
        jobs_df["Skills"].fillna("") + " " +
        jobs_df["Job Description"].fillna("")
    )

    jobs_df["combined_text"] = jobs_df["combined_text"].apply(preprocess)
    return jobs_df


def build_tfidf_matrix(jobs_df):
    """Convert all job descriptions into TF-IDF number vectors."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(jobs_df["combined_text"])
    return vectorizer, tfidf_matrix


def get_recommendations(resume_text, jobs_df, vectorizer, tfidf_matrix, top_n=5):
    """Find jobs that are most similar to the resume."""
    cleaned_resume = preprocess(resume_text)
    resume_vector = vectorizer.transform([cleaned_resume])

    similarity_scores = cosine_similarity(resume_vector, tfidf_matrix).flatten()
    best_indexes = similarity_scores.argsort()[::-1][:top_n]

    results = jobs_df.iloc[best_indexes].copy()
    results["similarity_score"] = similarity_scores[best_indexes]
    results["similarity_pct"] = (results["similarity_score"] * 100).round(2)

    return results.reset_index(drop=True)


def skill_is_present(text, skill):
    """Check if one skill is present in a text."""
    pattern = r"(?<![a-z0-9+#.])" + re.escape(skill.lower()) + r"(?![a-z0-9+#.])"
    return re.search(pattern, text) is not None


def get_missing_skills(resume_skills, job_skills_text):
    """Compare resume skills with job skills and return missing skills."""
    resume_skills_lower = [skill.lower() for skill in resume_skills]
    job_skills_cleaned = preprocess(job_skills_text)

    missing_skills = []

    for skill in SKILLS_LIST:
        skill_needed_for_job = skill_is_present(job_skills_cleaned, skill)
        skill_found_in_resume = skill.lower() in resume_skills_lower

        if skill_needed_for_job and not skill_found_in_resume:
            missing_skills.append(skill)

    return missing_skills
