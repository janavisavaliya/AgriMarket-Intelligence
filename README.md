# AgriMarket-Intelligence

AgriMarket-Intelligence is a B.Tech CSE 5th Semester academic project focused on agricultural market intelligence. The system performs exploratory analysis, dashboarding, forecasting, and anomaly detection for agricultural commodity prices using historical market data.

This repository is designed to work with a real market dataset supplied later by the project team. The application is built so a CSV file can be placed in `data/raw/` and processed through a reproducible pipeline.

## Objectives

- analyze price trends and market behavior
- compare commodity prices across markets
- detect volatility and unusual movements
- forecast short-term prices when historical data supports it
- present results through a Streamlit dashboard and FastAPI backend
- keep the pipeline flexible for real-world datasets

## Project scope

This project supports the following academic components:

- problem definition
- stakeholder analysis
- analytical questions
- data preparation
- EDA
- at least five meaningful visualizations
- machine learning and forecasting
- anomaly detection
- dashboard development
- project report and article outline

## Repository structure

```text
AgriMarket-Intelligence/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── pyproject.toml
├── docker-compose.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── notebooks/
│   ├── README.md
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_evaluation.ipynb
├── src/
│   └── agrimarket/
│       ├── __init__.py
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   ├── validator.py
│       │   └── preprocessing.py
│       ├── analysis/
│       │   ├── __init__.py
│       │   ├── eda.py
│       │   ├── statistics.py
│       │   └── correlations.py
│       ├── features/
│       │   ├── __init__.py
│       │   └── engineering.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── forecasting.py
│       │   ├── anomaly_detection.py
│       │   ├── evaluation.py
│       │   └── model_registry.py
│       ├── database/
│       │   ├── __init__.py
│       │   ├── connection.py
│       │   ├── models.py
│       │   └── repository.py
│       └── utils/
│           ├── __init__.py
│           └── logging_config.py
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       ├── health.py
│       ├── markets.py
│       ├── commodities.py
│       ├── analytics.py
│       ├── forecasts.py
│       └── anomalies.py
├── dashboard/
│   ├── app.py
│   ├── components/
│   ├── pages/
│   └── utils/
├── models/
│   └── .gitkeep
├── tests/
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_models.py
│   └── test_api.py
├── scripts/
│   ├── generate_sample_data.py
│   ├── ingest_data.py
│   ├── preprocess_data.py
│   ├── train_models.py
│   ├── run_pipeline.py
│   └── README.md
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── ml_methodology.md
│   ├── dashboard.md
│   ├── project_scope.md
│   └── academic_deliverables.md
├── PROJECT_STATUS.md
├── .github/
│   └── workflows/
│       └── ci.yml
└── .pytest_cache/
```

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables:

```bash
cp .env.example .env
```

4. Generate sample data for testing:

```bash
python scripts/generate_sample_data.py
```

5. Run the pipeline:

```bash
python scripts/run_pipeline.py
```

6. Start the API:

```bash
uvicorn api.main:app --reload
```

7. Start the dashboard:

```bash
streamlit run dashboard/app.py
```

8. Run tests:

```bash
pytest
```

## Data placement

Place the real agricultural market CSV in the following directory:

```text
data/raw/
```

The system includes configurable validation and preprocessing for adapting to the actual dataset schema when it is supplied.

## Important notes

- Do not fabricate model results or conclusions.
- Predictions are support estimates only.
- Forecasts should not be treated as guaranteed market outcomes.
- The system is designed to work with real data and a synthetic sample dataset for testing only.

## Academic deliverables

This project documentation includes placeholders for:

- problem definition
- stakeholder analysis
- analytical questions
- EDA outputs
- insights
- recommendations
- unexpected finding documentation
- project report and article outline

## License

MIT License
