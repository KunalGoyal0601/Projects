# classifier.py
# This file predicts the job role from resume text.

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess(text):
    """Convert text to lowercase and remove special characters."""
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def train_classifier(jobs_df):
    """Prepare job text so we can compare it with resume text."""
    job_text = jobs_df["combined_text"].apply(preprocess)

    vectorizer = TfidfVectorizer(stop_words="english")
    job_vectors = vectorizer.fit_transform(job_text)

    model = {
        "vectorizer": vectorizer,
        "job_vectors": job_vectors,
        "jobs_df": jobs_df,
    }

    return model, None


def predict_job_role(resume_text, model, label_encoder=None):
    """Predict role by finding the most similar job in the dataset."""
    cleaned_resume = preprocess(resume_text)

    resume_vector = model["vectorizer"].transform([cleaned_resume])
    scores = cosine_similarity(resume_vector, model["job_vectors"]).flatten()

    best_index = scores.argmax()
    best_job = model["jobs_df"].iloc[best_index]

    predicted_role = best_job["Job Role"]
    confidence = scores[best_index] * 100

    return predicted_role, confidence
