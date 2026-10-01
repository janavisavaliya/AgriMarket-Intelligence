# Real-Time Agriculture Analytics using India Open Government Data

## Project Title
Real-Time Agriculture Analytics using India Open Government Data (data.gov.in / Agmarknet)

## Project Overview
This project focuses on analyzing agricultural market data from India’s government open datasets to understand trends in crop production, pricing, yield, and market behavior across regions and seasons. The objective is to generate actionable insights for policymakers, mandi managers, supply chain officers, and agronomists by combining statistical analysis, machine learning, and dashboard-ready data preparation.

The project uses agricultural market data sourced from India’s Agmarknet and related open government data sources, with a focus on real-time and time-sensitive market intelligence for crop planning, procurement decisions, and agricultural operations.

## Objectives
- Analyze agricultural performance across crops, seasons, and regions.
- Identify how production, yield, and modal price relate to market behavior.
- Detect the influence of seasonality and crop category on agricultural trends.
- Build a predictive model for crop yield using market and production features.
- Prepare a cleaned, dashboard-ready dataset for Tableau and business intelligence workflows.

## Key Stakeholders
1. Mandi Managers: to monitor price variation and plan procurement and logistics.
2. Supply Chain Officers: to optimize transportation, storage, and distribution.
3. Agronomists / Agricultural Extension Officers: to understand crop productivity and season-wise performance.
4. Government and Policy Analysts: to support region-wise planning and subsidy decisions.

## Research Questions
This project addresses the following four core research questions:
1. How do Area, Production, and Modal Price vary across different crops and seasons in India?
2. What is the relationship between crop yield and market revenue potential?
3. Is there a statistically significant association between season and crop type in the dataset?
4. Can crop yield be predicted accurately using market and agricultural variables such as area, production, and modal price?

## Dataset Source
The agricultural dataset used in this project is based on Agmarknet information available through the India Open Government Data portal:
- data.gov.in / Agmarknet
- Source: https://www.data.gov.in/
- Agmarknet-related agriculture market datasets and commodity price data

Note: Download the raw CSV file into the project folder as:
- data/raw_agmarknet.csv

## Repository Structure
```text
.
├── data/
│   ├── raw_agmarknet.csv          # Raw Agmarknet dataset (download and place here)
│   └── cleaned_agriculture_data.csv  # Output from the data pipeline
├── notebooks/
│   └── 01_dav_analysis.ipynb     # Jupyter analytics notebook
├── reports/
│   └── Medium_Article_Draft.md   # Publication-ready article draft
├── data_pipeline.py              # Cleaning, analysis, and ML pipeline
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .gitignore
```

## Setup Instructions
### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.\.venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add the dataset
Download the raw Agmarknet CSV from data.gov.in and save it to:
```text
data/raw_agmarknet.csv
```

### 5. Run the data processing pipeline
```bash
python data_pipeline.py
```
This script will:
- load the raw CSV dataset,
- clean and transform the data,
- run statistical tests,
- train a Random Forest model,
- generate `data/cleaned_agriculture_data.csv` for Tableau.

### 6. Run the notebook
```bash
jupyter notebook notebooks/01_dav_analysis.ipynb
```
The notebook includes:
- dataset exploration,
- correlation analysis,
- visual analytics,
- machine learning summary,
- Tableau-ready dataset narrative.

## Tableau Integration Guide
To visualize the cleaned dataset in Tableau:
1. Open Tableau Desktop.
2. Click "Connect to Data" and select Text File / CSV.
3. Choose the cleaned dataset file:
```text
data/cleaned_agriculture_data.csv
```
4. Drag fields like `Crop`, `Season`, `Yield`, `Area`, `Production`, `Modal_Price`, and `Estimated_Revenue_INR` into the dashboard.
5. Use the following suggested visualizations:
   - Bar chart: Crop vs Production
   - Line chart: Seasonal price trend
   - Scatter plot: Yield vs Estimated Revenue
   - Heatmap: Correlation matrix
   - Map: State / District crop performance (if region fields are available)

## Expected Outputs
After running the pipeline, the project will generate:
- `data/cleaned_agriculture_data.csv`
- Pearson correlation matrices and statistical summaries in console output
- Chi-square analysis between `Season` and `Crop`
- Random Forest regression metrics for yield prediction
- Tableau-ready cleaned data

## Dependencies
The project uses the following Python libraries:
- pandas
- numpy
- scipy
- scikit-learn
- matplotlib
- seaborn
- jupyter

## Project Significance
This project demonstrates how open government agricultural data can be transformed into data-driven decision support for real-world agricultural operations. By combining analytics with machine learning, the project provides a clear methodology for identifying patterns in crop performance, pricing volatility, and yield drivers using accessible public data.

## License
This project is intended for academic and research purposes under standard educational usage. Add a project license if required by your institution.

## Authors / Contributors
- Janavi Savaliya
- B.Tech Data Analysis and Visualization Project
- Semester 5

## Contact
For questions or collaboration, contact the project author through the GitHub repository or institutional platform.
