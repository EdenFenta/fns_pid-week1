task_1:
  project_overview: |
    This repository contains the work for Task-1 of the FNS_PID Week 1 challenge.
    The focus of this task is to:
      - Set up the Python development environment.
      - Prepare and clean news data.
      - Perform Exploratory Data Analysis (EDA).
      - Set up unit testing and continuous integration (CI) with GitHub Actions.

  folder_structure:
    - .github/workflows/unittests.yml  # CI workflow for running tests
    - .gitignore
    - requirements.txt                  # Python dependencies
    - README.md                         # This file
    - src/                              # Python scripts
      - __init__.py
      - data_prep.py                    # Data cleaning and preparation
      - eda.py                          # Optional EDA helper functions
    - notebooks/
      - 01_eda.ipynb                    # Jupyter notebook for EDA
    - tests/
      - test_data_prep.py               # Unit tests for data preparation
    - data/
      - raw/raw_analyst_ratings.csv     # Raw dataset
    - outputs/
      - figs/                           # Figures generated from EDA

  setup_instructions:
    - step_1: "Clone the repository: git clone <your-repo-url> && cd <repo-directory>"
    - step_2: "Create a virtual environment and activate it:"
      commands:
        - "python -m venv .venv"
        - "source .venv/bin/activate  # macOS/Linux"
        - ".venv\\Scripts\\activate   # Windows"
    - step_3: "Install dependencies: pip install -r requirements.txt"
    - step_4: "Prepare the data: place your CSV in data/raw/ and run python src/data_prep.py"

  eda:
    description: |
      EDA is performed in notebooks/01_eda.ipynb and includes:
        - Descriptive statistics of headline lengths (characters & tokens)
        - Publisher counts and top active publishers
        - Daily and hourly publication trends
        - Keyword extraction using CountVectorizer
        - Optional topic modeling (LDA)
        - Figures saved in outputs/figs/

  unit_tests:
    description: "Unit tests are in the tests/ folder."
    run_command: "export PYTHONPATH=. && pytest tests/"
    coverage:
      - Headline length columns: headline_length_chars, headline_length_tokens
      - Lowercased headlines
      - Date-only columns

  ci_cd:
    description: |
      A GitHub Actions workflow (.github/workflows/unittests.yml) runs tests automatically
      on push or pull_request events to the task-1 branch.

  notes:
    - Only Task-1 content is included here. Sentiment analysis, stock indicators, and correlation analysis belong to Task-2 and Task-3.
    - All generated figures and cleaned data are saved locally and are not committed for large datasets.