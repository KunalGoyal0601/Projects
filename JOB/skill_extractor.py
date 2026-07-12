# skill_extractor.py
# This file finds known skills inside resume text.

import re


# Add or remove skills from this list based on your project dataset.
SKILLS_LIST = [
    "Python", "Java", "JavaScript", "C", "C++", "C#", "R",
    "HTML", "CSS", "React", "Node.js", "Django", "Flask",
    "SQL", "MySQL", "MongoDB", "SQLite",
    "Machine Learning", "Deep Learning", "NLP",
    "Natural Language Processing", "Computer Vision",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy", "Matplotlib", "Seaborn",
    "Data Analysis", "Data Visualization", "Statistics",
    "Excel", "Power BI", "Tableau",
    "Git", "GitHub", "Docker", "AWS", "Azure", "Linux",
    "Agile", "Scrum", "Communication", "Leadership", "Teamwork",
]


def clean_text(text):
    """Convert text to lowercase and remove extra spaces."""
    text = str(text).lower()
    text = re.sub(r"\s+", " ", text)
    return text


def extract_skills(resume_text):
    """Compare resume text with SKILLS_LIST and return matched skills."""
    found_skills = []
    cleaned_resume = clean_text(resume_text)

    for skill in SKILLS_LIST:
        skill_name = skill.lower()
        pattern = r"(?<![a-z0-9+#.])" + re.escape(skill_name) + r"(?![a-z0-9+#.])"

        if re.search(pattern, cleaned_resume):
            found_skills.append(skill)

    return sorted(found_skills)
