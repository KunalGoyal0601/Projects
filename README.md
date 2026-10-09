# Project Collection

This repository is a small collection of application work that has not yet been fully separated into standalone repositories. New independent projects should live in their own repositories; this repository is being kept as a transition/index for the remaining work.

## Projects

### Job recommendation system — `JOB/`

A resume-based job recommendation prototype using skill extraction, TF-IDF, cosine similarity, and a Logistic Regression classifier.

- Entry point: `JOB/app.py`
- Recommendation logic: `JOB/recommender.py`
- Classification: `JOB/classifier.py`
- Resume parsing and skill extraction: `JOB/resume_parser.py`, `JOB/skill_extractor.py`
- Dependencies: `JOB/requirements.txt`
- Project-specific documentation: [`JOB/README.md`](JOB/README.md)

This project still needs to be copied into a dedicated repository and tested from a clean environment.

### MCQ generator

Moved into its own repository: [`mcqgen`](https://github.com/KunalGoyal0601/mcqgen). The standalone copy includes a README, dependency list, environment-variable example, ignore rules, source package, and a notebook with saved outputs cleared. It is still an experimental prototype and has not been validated from a clean environment.

### Medical chatbot — pending review

The current tree contains `medical_bot/` and `Medical chat bot`. Their relationship is not known yet, so neither should be merged or removed until their contents are compared.

## Remaining cleanup

1. Compare the medical-chatbot paths and decide whether they are one project or separate projects.
2. Move the job recommender to its own repository once the destination is created and verified.
3. Review datasets for licensing, personal data, and redistribution restrictions before making any project public.
4. Add tests and clean setup instructions to each standalone project.

## Safety and reproducibility

- Never commit API keys, tokens, passwords, private applicant information, or medical information.
- Keep local virtual environments, logs, caches, generated outputs, and large raw datasets out of Git.
- Document dependencies and Python versions; test instructions from a fresh environment.
- A README documents intent and current structure; it is not proof that the application runs.

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
