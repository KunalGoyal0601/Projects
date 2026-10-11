# Project Collection

This repository is a small collection of application work that has not yet been fully separated into standalone repositories. It is being kept as an index for projects that remain here.

## Projects

### Job recommendation system

Moved into its own repository: [job-recommendation-system](https://github.com/KunalGoyal0601/job-recommendation-system).

The standalone repository contains the Tkinter app, resume parser, skill extractor, TF-IDF/cosine-similarity job recommender, sample dataset, dependencies, and setup documentation. The current role suggestion uses similarity matching rather than a trained Logistic Regression classifier. It remains a learning prototype and has not been validated from a clean environment.

### MCQ generator

Moved into its own repository: [mcqgen](https://github.com/KunalGoyal0601/mcqgen). The standalone copy includes a README, dependency list, environment-variable example, ignore rules, source package, and a notebook with saved outputs cleared. It is still an experimental prototype and has not been validated from a clean environment.

### Medical chatbot — pending review

The current tree contains `medical_bot/` and `Medical chat bot`. Their relationship is not known yet, so neither should be merged or removed until their contents are compared.

## Remaining cleanup

1. Compare the medical-chatbot paths and decide whether they are one project or separate projects.
2. Review datasets for licensing, personal data, and redistribution restrictions before making any project public.
3. Add tests and clean setup instructions to each standalone project.

## Safety and reproducibility

- Never commit API keys, tokens, passwords, private applicant information, or medical information.
- Keep local virtual environments, logs, caches, generated outputs, and large raw datasets out of Git.
- Document dependencies and Python versions; test instructions from a fresh environment.
- A README documents intent and current structure; it is not proof that the application runs.

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
