# Projects

A collection of small application projects and experiments. This repository currently groups several projects in one place; it is being documented before any files are moved or split into separate repositories.

## Projects in this repository

### 1. Job recommendation system — `JOB/`

The original project description says this is a simple job recommendation system. The folder contains the app entry point, recommendation/classification code, resume parsing, skill extraction, a dataset, and a requirements file.

Key files:
- `JOB/app.py` — application entry point
- `JOB/recommender.py` — recommendation logic
- `JOB/classifier.py` — classifier component
- `JOB/resume_parser.py` — resume parsing
- `JOB/skill_extractor.py` — skill extraction
- `JOB/requirements.txt` — Python dependencies
- `JOB/README.md` — project-specific instructions

### 2. MCQ generator — `mcqgeneter/`

Contains Python modules and a notebook for the MCQ-generation project. The folder name is a legacy spelling; paths should only be renamed after checking import statements and notebook references.

### 3. Medical chatbot — `medical_bot/` and `Medical chat bot/`

Both folder names appear in the repository tree. Their relationship is not yet confirmed. Compare their contents before merging, deleting, or moving either folder.

## Repository layout (current)

```text
Projects/
├── JOB/
├── mcqgeneter/
├── medical_bot/
├── Medical chat bot/
└── README.md
```

## Cleanup plan

1. Check the two medical-chatbot folders for duplicated or distinct code.
2. Add a README and tested setup instructions for each application.
3. Confirm which dataset files are redistributable and whether any secrets or personal information are present.
4. After the code runs independently, consider splitting the job recommender, MCQ generator, and medical chatbot into separate repositories. Keep this repository as an index only if that makes the portfolio easier to navigate.

## General notes

- Do not commit API keys, passwords, tokens, or real private applicant/medical information.
- Document the Python version and dependency installation for each app.
- Keep screenshots, sample data, and generated artifacts clearly separated from source code.
- This README describes the current layout; it does not claim the projects have been executed or tested in a clean environment.

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
