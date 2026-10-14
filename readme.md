# SpaceX Falcon 9 Landing Prediction

A Data Science and Machine Learning project developed as part of the
**IBM Applied Data Science Capstone**. The project explores SpaceX
Falcon 9 launch records, investigates factors associated with
first-stage landing outcomes, and compares classification models to
predict landing success.

> **Project status:** The Applied Data Science Capstone course is marked
> complete. The model results documented here reflect the outputs
> currently recorded in the project notebooks.

## Table of Contents

-   [Project Overview](#project-overview)
-   [Objectives](#objectives)
-   [Workflow](#workflow)
-   [Tools and Technologies](#tools-and-technologies)
-   [Repository Structure](#repository-structure)
-   [Key Analysis](#key-analysis)
-   [Machine Learning Results](#machine-learning-results)
-   [Interactive Dashboard](#interactive-dashboard)
-   [Getting Started](#getting-started)
-   [Limitations and Future
    Improvements](#limitations-and-future-improvements)
-   [Acknowledgements](#acknowledgements)

## Project Overview

The goal is to explore historical Falcon 9 launch data and understand
how launch characteristics relate to first-stage landing outcomes. The
work follows an applied data science workflow, from data collection and
preparation through exploratory analysis, visualization, and
classification.

This repository includes notebooks for data collection, web scraping,
data wrangling, SQL analysis, exploratory data analysis, geographic
visualization, and machine learning, along with a Plotly Dash dashboard
script.

## Objectives

-   Collect and prepare Falcon 9 launch records for analysis.
-   Explore launch outcomes and relationships among launch site, orbit,
    payload mass, and flight number.
-   Use SQL queries to answer questions about launch sites and mission
    outcomes.
-   Visualize launch-related geographic information with Folium.
-   Build an interactive dashboard using Plotly Dash.
-   Train and compare classification models for first-stage landing
    prediction.

## Workflow

1.  **Data Collection** --- work with launch data using the course's
    data collection and web-scraping exercises.
2.  **Data Wrangling** --- prepare the data and create a binary
    landing-class target used in the analysis.
3.  **Exploratory Data Analysis (EDA)** --- examine patterns in launch
    sites, orbit types, payload mass, flight number, and landing
    outcomes.
4.  **SQL Analysis** --- query launch records to summarize categories,
    dates, and landing outcomes.
5.  **Visualization** --- create plots, a Folium map, and a Plotly Dash
    dashboard.
6.  **Predictive Analysis** --- train and compare Logistic Regression,
    Support Vector Machine (SVM), Decision Tree, and K-Nearest Neighbors
    (KNN) classifiers.

## Tools and Technologies

-   **Language:** Python
-   **Data handling:** Pandas, NumPy
-   **Visualization:** Matplotlib, Seaborn, Plotly
-   **Mapping:** Folium
-   **Machine Learning:** Scikit-learn
-   **Database / queries:** SQL with SQLite in the notebook workflow
-   **Development:** Jupyter Notebook
-   **Dashboard:** Plotly Dash

## Repository Structure

``` text
SpaceX-Falcon-9-Landing-Prediction/
├── dashboard/
│   └── dash_interactivity.py
├── data/
│   └── spacex_launch_dash.csv
├── notebook/
│   ├── SpaceX_Machine Learning Prediction_Part_5.ipynb
│   ├── edatadaviz.ipynb
│   ├── jupyter-labs-eda-sql-coursera_sqlite.ipynb
│   ├── jupyter-labs-spacex-data-collection-api.ipynb
│   ├── jupyter-labs-webscraping.ipynb
│   ├── lab_jupyter_launch_site_location.ipynb
│   └── labs-jupyter-spacex-Data wrangling.ipynb
├── .gitignore
├── readme.md
└── requirements.txt
```

## Key Analysis

### Exploratory Data Analysis

The notebooks explore the distribution of landing outcomes and compare
the binary landing class across several launch characteristics.
Visualizations include:

-   Yearly landing success rate.
-   Landing success rate by orbit.
-   Payload mass versus launch site.
-   Flight number versus launch site.
-   Payload mass versus flight number.
-   Class-colored comparisons across orbit categories.

The yearly chart shows a general improvement in observed landing success
over the years displayed, with fluctuations between years. The orbit
chart shows that observed success rates vary by orbit; categories with
few launches should be interpreted carefully.

### SQL Analysis

The SQL notebook includes queries to:

-   List distinct launch sites.
-   Retrieve records for launch sites beginning with `CCA`.
-   Find the earliest successful ground-pad landing date.
-   Count mission outcomes.
-   Extract month values from dates and inspect selected landing
    outcomes.
-   Rank landing outcomes over a specified date range.

One data-quality observation is that outcome labels can appear in
different forms (for example, repeated `Success` categories).
Normalizing whitespace and category labels before aggregation is an
important improvement.

### Geographic Visualization

Folium is used to display launch-related geographic information on an
interactive map. The map supports zooming and panning to inspect
locations and nearby geographic features.

### Interactive Dashboard

The Plotly Dash application is located at
`dashboard/dash_interactivity.py` and uses
`data/spacex_launch_dash.csv`. The dashboard workflow includes
launch-site filtering, a summary of successful launches by site, a
payload-mass range control, and a payload-mass versus landing-success
visualization.

## Machine Learning Results

Four classifiers were compared:

  Model                            Reported test accuracy
  ------------------------------ ------------------------
  Logistic Regression                              83.33%
  Support Vector Machine (SVM)                     83.33%
  Decision Tree                                    83.33%
  K-Nearest Neighbors (KNN)                        83.33%

The notebook's score-selection code returns **Logistic Regression** as
the best-performing method because it is the first model with the
maximum score in the dictionary. Since all four displayed scores are
equal, the current results do **not** demonstrate that Logistic
Regression outperforms the other models.

Accuracy alone does not describe all model errors. Confusion matrices
and additional metrics such as precision, recall, and F1-score should be
considered when interpreting performance.

## Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/Yossefassem79/SpaceX-Falcon-9-Landing-Prediction.git
cd SpaceX-Falcon-9-Landing-Prediction
```

### 2. Create and activate a virtual environment (recommended)

**Windows:**

``` bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Explore the notebooks

Start Jupyter Notebook from the repository root:

``` bash
jupyter notebook
```

Open the notebooks in the `notebook/` folder to follow the data
collection, wrangling, SQL, EDA, mapping, and machine-learning workflow.

### 5. Run the dashboard

From the repository root, run:

``` bash
python dashboard/dash_interactivity.py
```

If the script starts successfully, open the local URL printed in the
terminal (commonly `http://127.0.0.1:8050`). Make sure the dependencies
in `requirements.txt` are installed and the dashboard CSV remains at
`data/spacex_launch_dash.csv`.

## Limitations and Future Improvements

-   Normalize categorical labels consistently before grouping or
    counting outcomes.
-   Evaluate models using cross-validation and report precision, recall,
    F1-score, and confusion matrices alongside accuracy.
-   Verify that hyperparameter tuning is evaluated without data leakage
    and that the final test set remains held out.
-   Add clearer legends and more focused screenshots for the Folium map
    and dashboard.
-   Add automated tests and a reproducible environment specification.
-   Document exact data-source URLs and data versions where applicable.

## Acknowledgements

This project was completed as part of the **IBM Applied Data Science
Capstone** learning pathway. The notebooks and workflow reflect the
practical exercises and analysis performed for the SpaceX Falcon 9
landing prediction project.

## Author

**Yossef Assem**

-   GitHub: [@Yossefassem79](https://github.com/Yossefassem79)
-   Project repository: [SpaceX Falcon 9 Landing
    Prediction](https://github.com/Yossefassem79/SpaceX-Falcon-9-Landing-Prediction)
