# 🔍 Resume-Based Job Recommendation System using Machine Learning

A complete end-to-end ML project that analyzes a resume, extracts skills, 
recommends suitable jobs using TF-IDF + Cosine Similarity, and predicts the 
most suitable job role using a Logistic Regression classifier.

---

## 📁 Project Structure

```
Resume-Job-Recommender/
│
├── app.py              → Main Tkinter GUI application
├── resume_parser.py    → Extract text from PDF / DOCX resumes
├── skill_extractor.py  → NLP-based skill extraction using regex
├── recommender.py      → TF-IDF vectorization + Cosine Similarity
├── classifier.py       → Logistic Regression job role classifier
├── dataset.csv         → Job dataset (25 jobs, 4 columns)
├── requirements.txt    → Python dependencies
├── sample_resume.txt   → Sample resume for testing
└── README.md           → Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

---

## 🧠 How It Works

### Step 1 — Resume Input
- User uploads a `.pdf` or `.docx` resume via the GUI
- `resume_parser.py` extracts raw text using **PyPDF2** (PDF) or **python-docx** (DOCX)

### Step 2 — Skill Extraction
- `skill_extractor.py` scans the resume text against a predefined list of 100+ skills
- Uses **regex with word boundaries** for accurate matching

### Step 3 — TF-IDF Vectorization
- `recommender.py` converts all job descriptions + skills into TF-IDF vectors
- Resume text is also transformed using the **same vectorizer vocabulary**

### Step 4 — Cosine Similarity (Job Matching)
- Computes cosine similarity between the resume vector and each job vector
- Returns **Top 5 job recommendations** sorted by similarity score

### Step 5 — Classification (Job Role Prediction)
- `classifier.py` trains a **Logistic Regression** model on job descriptions → job roles
- Predicts the most likely job role for the uploaded resume with confidence %

### Step 6 — Missing Skills Detection
- Compares skills in each recommended job against extracted resume skills
- Highlights which skills are missing so the user knows what to learn

---

## 📊 Dataset

`dataset.csv` contains 25 jobs with 4 columns:

| Column         | Description                              |
|----------------|------------------------------------------|
| `Job Title`    | Specific job title (e.g. Data Scientist) |
| `Skills`       | Space-separated required skills          |
| `Job Description` | Detailed role description             |
| `Job Role`     | Category label for classification        |

---

## 🖥️ GUI Features (Tkinter)

| Tab                   | Content                                              |
|-----------------------|------------------------------------------------------|
| Skills & Prediction   | Extracted skills list + Predicted job role + confidence |
| Job Recommendations   | Top 5 jobs with similarity scores and descriptions   |
| Missing Skills        | Per-job gap analysis                                 |
| Resume Text           | Raw extracted resume text                            |

---

## 🤖 ML Concepts Demonstrated

| Concept               | Implementation                         |
|-----------------------|----------------------------------------|
| TF-IDF                | `TfidfVectorizer` with bigrams         |
| Cosine Similarity     | `cosine_similarity` from sklearn        |
| Classification        | `LogisticRegression` pipeline          |
| Text Preprocessing    | Lowercasing, punctuation removal       |
| Label Encoding        | `LabelEncoder` for job roles           |
| Pipeline              | `sklearn.pipeline.Pipeline`            |

---

## 🚀 Quick Test (No GUI)

Run this to test the ML pipeline without the GUI:

```python
from resume_parser import extract_text
from skill_extractor import extract_skills
from recommender import load_dataset, build_tfidf_matrix, get_recommendations
from classifier import train_classifier, predict_job_role

# Use sample text directly
with open("sample_resume.txt") as f:
    resume_text = f.read()

skills = extract_skills(resume_text)
print("Skills:", skills)

df = load_dataset("dataset.csv")
vectorizer, matrix = build_tfidf_matrix(df)
clf, le = train_classifier(df)

recs = get_recommendations(resume_text, df, vectorizer, matrix)
role, conf = predict_job_role(resume_text, clf, le)

print(f"\nPredicted Role: {role} ({conf}%)")
print("\nTop Jobs:")
print(recs[["Job Title", "Job Role", "similarity_pct"]])
```

---

## 📦 Dependencies

- `pandas` — Data manipulation
- `scikit-learn` — TF-IDF, cosine similarity, logistic regression
- `PyPDF2` — PDF text extraction
- `python-docx` — DOCX text extraction
- `tkinter` — GUI (built into Python standard library)

---

## 👨‍💻 Author

Built as a final year / viva-ready ML project demonstrating NLP, supervised learning, and GUI development in Python.
