# statistical-ml-lab

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0+-150458?logo=pandas&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-0.14+-4c4c8f)
![scipy](https://img.shields.io/badge/scipy-1.11+-8CAAE6?logo=scipy&logoColor=white)

---

## Overview

**statistical-ml-lab** is a structured collection of applied statistics and machine-learning experiments that walks end-to-end through the data-science pipeline — from raw-data exploration to ensemble model evaluation. Each experiment is implemented across three real-world datasets (Housing, Iris, Titanic), demonstrating that the same rigorous methodology generalises across regression, multi-class classification, and binary classification problems. The repository showcases proficiency in descriptive and inferential statistics, classical ML modelling, model diagnostics, and reproducible research practices using Jupyter Notebooks.

---

## Repository Structure

```
statistical-ml-lab/
├── README.md
├── requirements.txt
├── .gitignore
│
├── Housing/                          # Regression-oriented dataset
│   ├── Housing.csv
│   ├── Exp_01_EDA_Descriptive_Statistics.ipynb
│   ├── Exp_02_Data_Preprocessing.ipynb
│   ├── Exp_03_Sampling_Methods.ipynb
│   ├── Exp_04_Hypothesis_Testing.ipynb
│   ├── Exp_06_Linear_Regression_Diagnostics.ipynb
│   ├── Exp_08_Classification_Models_ROC.ipynb
│   └── Exp_09_Decision_Trees_Random_Forest.ipynb
│
├── Iris/                             # Multi-class classification dataset
│   ├── Iris.csv
│   ├── Exp_01_EDA_Descriptive_Statistics.ipynb
│   ├── Exp_02_Data_Preprocessing.ipynb
│   ├── Exp_03_Sampling_Methods.ipynb
│   ├── Exp_04_Hypothesis_Testing.ipynb
│   ├── Exp_06_Linear_Regression_Diagnostics.ipynb
│   ├── Exp_08_Classification_Models_ROC.ipynb
│   └── Exp_09_Decision_Trees_Random_Forest.ipynb
│
└── Titanic/                          # Binary classification dataset
    ├── Titanic-Dataset.csv
    ├── Exp_01_EDA_Descriptive_Statistics.ipynb
    ├── Exp_02_Data_Preprocessing.ipynb
    ├── Exp_03_Sampling_Methods.ipynb
    ├── Exp_04_Hypothesis_Testing.ipynb
    ├── Exp_06_Linear_Regression_Diagnostics.ipynb
    ├── Exp_08_Classification_Models_ROC.ipynb
    └── Exp_09_Decision_Trees_Random_Forest.ipynb
```

---

## Experiments Overview

| Exp # | Title | Techniques | Datasets |
|-------|-------|------------|----------|
| 01 | EDA & Descriptive Statistics | Summary statistics, histograms, Pearson correlation heatmap, top correlated pairs | Housing, Iris, Titanic |
| 02 | Data Preprocessing Pipeline | Missing value imputation, one-hot/label encoding, StandardScaler, MinMaxScaler, IQR outlier removal | Housing, Iris, Titanic |
| 03 | Sampling Methods | Simple Random Sampling (SRS), Proportional Stratified Sampling, Cluster Sampling | Housing, Iris, Titanic |
| 04 | Hypothesis Testing | Welch's t-test, Chi-square test of independence, One-way ANOVA, Tukey HSD post-hoc (α = 0.05) | Housing, Iris, Titanic |
| 06 | Multiple Linear Regression & Diagnostics | OLS regression, R²/RMSE/MAE, VIF multicollinearity, residual analysis, Q-Q plot, Cook's Distance | Housing, Iris, Titanic |
| 08 | Classification Models & ROC Analysis | Logistic Regression, K-Nearest Neighbours (K-tuning), Gaussian Naive Bayes, ROC-AUC comparison | Housing, Iris, Titanic |
| 09 | Decision Trees & Random Forest Ensemble | Decision Tree (Gini), Random Forest (OOB validation), permutation importance, cross-validation | Housing, Iris, Titanic |

---

## Key Skills Demonstrated

- **Exploratory Data Analysis (EDA):** Univariate and bivariate analysis, distribution visualisation, and correlation profiling across heterogeneous datasets.
- **Data Preprocessing:** Robust pipelines for missing-value imputation (median/mode), categorical encoding (one-hot & label), feature scaling (Standard & MinMax), and IQR-based outlier handling.
- **Statistical Sampling:** Implementation and representativeness comparison of SRS, proportional stratified, and cluster sampling strategies.
- **Inferential Statistics & Hypothesis Testing:** Selection and application of parametric tests (t-test, ANOVA) and non-parametric tests (chi-square); post-hoc analysis with Tukey HSD to pinpoint significant pairwise differences.
- **Regression Diagnostics:** OLS model fitting with full assumption checking — multicollinearity via VIF, heteroscedasticity via residual plots, normality via Q-Q plots, and influential-point detection via Cook's Distance.
- **Classification Modelling:** End-to-end pipeline from scaling to prediction for Logistic Regression, KNN (cross-validated K selection), and Gaussian Naive Bayes; thorough evaluation via confusion matrices and classification reports.
- **Ensemble Methods:** Random Forest with OOB error estimation, `n_estimators` tuning, and permutation-based feature importance compared against a single Decision Tree to demonstrate the bias-variance trade-off.

---

## Datasets

| Dataset | Rows | Key Features | Task Type |
|---------|------|-------------|-----------|
| **Housing.csv** | 545 | `price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`, `mainroad`, `airconditioning`, `furnishingstatus` | Regression |
| **Iris.csv** | 150 | `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, `PetalWidthCm`, `Species` | Multi-class Classification |
| **Titanic-Dataset.csv** | 891 | `Survived`, `Pclass`, `Sex`, `Age`, `Fare`, `Embarked`, `SibSp`, `Parch` | Binary Classification |

**Housing** is a real-estate pricing dataset well-suited for regression and multicollinearity analysis. **Iris** is the classic Fisher dataset used to benchmark multi-class classifiers and explore linear separability. **Titanic** provides a binary survival-prediction challenge with mixed feature types, missing values, and strong class-signal features.

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/statistical-ml-lab.git
cd statistical-ml-lab

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter Lab
jupyter lab
```

Open any notebook inside the `Housing/`, `Iris/`, or `Titanic/` folders and run all cells top-to-bottom.

---

## Results Highlights

- 🌲 **Random Forest OOB Validation:** Out-of-bag error estimation enabled unbiased model assessment without a dedicated validation split, with `n_estimators` tuning plateauing around 100 trees — demonstrating ensemble stability.
- 📉 **VIF Multicollinearity Diagnostics:** Variance Inflation Factor analysis in the regression experiments identified highly collinear predictors (VIF > 10), guiding feature selection and improving coefficient interpretability.
- 🔬 **Tukey HSD Post-Hoc Tests:** Following significant one-way ANOVA results, Tukey's Honestly Significant Difference test pinpointed exactly which group pairs drove the difference — adding statistical rigour beyond a simple p-value.
- 📈 **ROC-AUC Model Comparison:** Side-by-side ROC curves for Logistic Regression, KNN, and Naive Bayes quantified discriminative power, revealing that model choice and dataset characteristics (e.g., linear vs. non-linear boundaries) significantly affect AUC scores.

---

## Tech Stack

| Category | Libraries |
|----------|-----------|
| Data Manipulation | `pandas`, `numpy` |
| Visualisation | `matplotlib`, `seaborn` |
| Machine Learning | `scikit-learn` |
| Statistical Modelling | `statsmodels`, `scipy` |
| Environment | `Jupyter Lab / Notebook` |
| Language | Python 3.x |

---

*Built as a portfolio showcase of end-to-end statistical and ML methodology. Each experiment is self-contained and reproducible.*
