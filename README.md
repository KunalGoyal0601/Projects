# Project Collection

This repository is a small index for project work that has not yet been moved into standalone repositories.

## Projects

### Job recommendation system

Moved into its own repository: [job-recommendation-system](https://github.com/KunalGoyal0601/job-recommendation-system).

The standalone repository contains the Tkinter app, resume parser, skill extractor, TF-IDF/cosine-similarity job recommender, sample dataset, dependencies, and setup documentation. The current role suggestion uses similarity matching rather than a trained Logistic Regression classifier. It remains a learning prototype and has not been validated from a clean environment.

### MCQ generator

Moved into its own repository: [mcqgen](https://github.com/KunalGoyal0601/mcqgen). The standalone copy includes a README, dependency list, environment-variable example, ignore rules, source package, and a notebook with saved outputs cleared. It is still an experimental prototype and has not been validated from a clean environment.

### Medical chatbot — not implemented here yet

The previous `medical_bot/` and `Medical chat bot` paths contained only empty placeholder files; no implementation was present to migrate. These placeholders have been removed. Create a dedicated repository or add the actual source files when the project is ready.

## Remaining cleanup

1. Review public repositories for accidentally committed credentials, personal information, and data that should not be redistributed.
2. Review each project's setup instructions and test from a clean environment.
3. Add tests and appropriate data/source licensing notes where needed.

## Safety and reproducibility

- Never commit API keys, tokens, passwords, private applicant information, or medical information.
- If a real credential has been committed, revoke or rotate it; deleting it from the latest commit alone does not remove it from Git history.
- Keep local virtual environments, logs, caches, generated outputs, and large raw datasets out of Git.
- A README documents intent and current structure; it is not proof that the application runs.

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
