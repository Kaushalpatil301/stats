"""
document_notebooks.py
Inserts professional markdown documentation cells into all 21 notebooks.
Run from the repo root: python document_notebooks.py
"""

import json
import os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def md_cell(source_lines):
    """Return a notebook markdown cell dict."""
    if isinstance(source_lines, str):
        source_lines = source_lines.splitlines(keepends=True)
        # Ensure last line has no trailing newline stripped unintentionally
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source_lines
    }


def load_nb(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_nb(path, nb):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Done: {path}")


def insert_at(cells, idx, cell):
    cells.insert(idx, cell)


# ---------------------------------------------------------------------------
# Title cells per experiment
# ---------------------------------------------------------------------------

def title_cell_01(dataset):
    return md_cell(
        f"## Experiment 1 — Exploratory Data Analysis & Descriptive Statistics\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Explore the structure, distributions, and correlations within the dataset "
        f"to form initial hypotheses and identify patterns before modelling.  \n"
        f"**Techniques:** Summary statistics, histograms, correlation heatmap, top correlated pairs."
    )


def title_cell_02(dataset):
    return md_cell(
        f"## Experiment 2 — Data Preprocessing Pipeline\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Prepare raw data for analysis by handling missing values, encoding categorical "
        f"features, scaling numerical variables, and detecting/removing outliers.  \n"
        f"**Techniques:** Median/mode imputation, one-hot encoding, label encoding, StandardScaler, "
        f"MinMaxScaler, IQR-based outlier removal."
    )


def title_cell_03(dataset):
    return md_cell(
        f"## Experiment 3 — Sampling Methods\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Demonstrate three fundamental sampling strategies and compare their "
        f"representativeness against the population mean.  \n"
        f"**Techniques:** Simple Random Sampling (SRS), Proportional Stratified Sampling, Cluster Sampling."
    )


def title_cell_04(dataset):
    return md_cell(
        f"## Experiment 4 — Hypothesis Testing\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Apply inferential statistical tests to validate or reject null hypotheses "
        f"about group differences and feature associations.  \n"
        f"**Techniques:** Welch's t-test, Chi-square test of independence, One-way ANOVA, "
        f"Tukey HSD post-hoc test (α = 0.05)."
    )


def title_cell_06(dataset):
    return md_cell(
        f"## Experiment 6 — Multiple Linear Regression & Diagnostics\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Fit an OLS regression model, evaluate predictive performance, and diagnose "
        f"model assumptions including multicollinearity and influential observations.  \n"
        f"**Techniques:** OLS regression (statsmodels), Train/Test split, R², RMSE, MAE, VIF "
        f"(multicollinearity), residual analysis, Q-Q plot, Cook's Distance (influential points)."
    )


def title_cell_08(dataset):
    return md_cell(
        f"## Experiment 8 — Classification Models & ROC Analysis\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Build and compare three binary classifiers, tune KNN hyperparameters via "
        f"cross-validation, and evaluate discriminative power using ROC-AUC.  \n"
        f"**Techniques:** Logistic Regression (with odds ratios), K-Nearest Neighbours (K-tuning), "
        f"Gaussian Naive Bayes, StandardScaler pipeline, confusion matrix, classification report, "
        f"ROC curves, AUC comparison."
    )


def title_cell_09(dataset):
    return md_cell(
        f"## Experiment 9 — Decision Trees & Random Forest Ensemble\n"
        f"**Dataset:** {dataset}  \n"
        f"**Objective:** Compare interpretable tree models against an ensemble Random Forest, analyze "
        f"overfitting via depth restriction, and quantify feature contributions.  \n"
        f"**Techniques:** Decision Tree (Gini, full & restricted depth), Random Forest (OOB validation, "
        f"n_estimators tuning), permutation importance, feature importance comparison, cross-validation."
    )


# ---------------------------------------------------------------------------
# Section cells per experiment
# ---------------------------------------------------------------------------

SECTIONS_01 = [
    md_cell("### 1. Setup & Imports\nLoad all required libraries for data manipulation, visualisation, and statistical analysis."),
    md_cell("### 2. Load Dataset\nRead the CSV file into a pandas DataFrame and preview the first few rows to confirm successful loading and inspect column names."),
    md_cell("### 3. Descriptive Statistics\nCompute summary statistics (count, mean, std, min/max, quartiles) for all numerical features. The transposed view improves readability when there are many columns."),
    md_cell("### 4. Distribution Analysis — Histograms\nPlot histograms for all numerical variables to visualise their distributions, detect skewness, and identify potential outliers before any modelling step."),
    md_cell("### 5. Correlation Analysis — Heatmap\nCompute the Pearson correlation matrix and render it as an annotated heatmap using a diverging colour palette. High absolute values indicate strong linear relationships between features."),
    md_cell("### 6. Top Correlated Variable Pairs\nExtract and rank the upper triangle of the correlation matrix to surface the most strongly correlated feature pairs — useful for feature selection and multicollinearity awareness."),
]

SECTIONS_02 = [
    md_cell("### 1. Setup & Imports\nLoad libraries required for data preprocessing: pandas and numpy for data handling, scikit-learn for scaling, and matplotlib/seaborn for visualisation."),
    md_cell("### 2. Load Dataset\nRead the raw CSV file and display its shape, data types, and a sample of rows to understand the starting state of the data before any cleaning."),
    md_cell("### 3. Missing Value Analysis\nDetect and quantify missing values in each column. Understanding the missingness pattern guides the choice of imputation strategy (median for numerics, mode for categoricals)."),
    md_cell("### 4. Missing Value Imputation\nFill numeric missing values with the column median (robust to outliers) and categorical missing values with the column mode. Verify that no missing values remain after imputation."),
    md_cell("### 5. Categorical Encoding\nConvert categorical string features to numeric representations. One-hot encoding is applied to nominal features (no intrinsic order); label encoding to ordinal features where the order carries meaning."),
    md_cell("### 6. Feature Scaling\nApply StandardScaler (zero mean, unit variance) and MinMaxScaler (range [0, 1]) to numerical columns. Scaling is critical for distance-based algorithms (KNN) and gradient-based optimisers (Logistic Regression)."),
    md_cell("### 7. Outlier Detection & Removal\nUse the Interquartile Range (IQR) method to identify observations that lie beyond 1.5 × IQR from the first and third quartiles. Outliers can distort model coefficients and summary statistics."),
    md_cell("### 8. Save Preprocessed Dataset\nExport the cleaned and transformed DataFrame to CSV so downstream experiments can load a consistent, analysis-ready version of the data."),
]

SECTIONS_03 = [
    md_cell("### 1. Setup & Imports\nImport numpy, pandas, and matplotlib. Set a random seed to ensure reproducibility of all sampling operations."),
    md_cell("### 2. Load Dataset\nRead the dataset and display its shape. Understanding the population size is necessary for choosing appropriate sample sizes."),
    md_cell("### 3. Population Parameter\nCompute the true population mean for the target variable. This serves as the benchmark against which the representativeness of each sampling method will be evaluated."),
    md_cell("### 4. Simple Random Sampling (SRS)\nDraw a random sample of fixed size without replacement from the full population. SRS gives every observation an equal probability of selection — the simplest unbiased estimator."),
    md_cell("### 5. Proportional Stratified Sampling\nPartition the population into homogeneous strata (e.g., by a categorical feature) and draw samples from each stratum proportional to its size. This guarantees representation of all subgroups and typically reduces sampling variance."),
    md_cell("### 6. Cluster Sampling\nDivide the population into clusters, randomly select a subset of clusters, and include all observations from the chosen clusters. Cluster sampling reduces the cost of data collection when the population is geographically or logically grouped."),
    md_cell("### 7. Comparison — Sample Means vs Population Mean\nCompare the sample mean from each method against the true population mean to quantify representativeness. Smaller deviation indicates a more accurate estimate with the given sample size."),
    md_cell("### 8. Save Samples\nExport each sampled DataFrame to a CSV file for reference and downstream use."),
]

SECTIONS_04 = [
    md_cell("### 1. Setup & Imports\nImport scipy (for t-test and chi-square), statsmodels (for ANOVA and Tukey HSD), and pandas. Set display options for clean output formatting."),
    md_cell("### 2. Load Dataset\nRead the dataset. Hypothesis tests will be applied to specific features, so it is important to understand the schema and available group variables."),
    md_cell("### 3. Welch's Two-Sample t-Test\nTest whether the means of a continuous variable differ significantly between two independent groups. Welch's variant is used because it does not assume equal population variances — making it more robust than Student's t-test.  \n**H₀:** The group means are equal.  \n**H₁:** The group means are significantly different (α = 0.05)."),
    md_cell("### 4. Chi-Square Test of Independence\nTest whether two categorical variables are statistically independent. A low p-value indicates a significant association between the variables.  \n**H₀:** The two categorical variables are independent.  \n**H₁:** There is a significant association between them (α = 0.05)."),
    md_cell("### 5. One-Way ANOVA\nTest whether the means of a continuous variable differ significantly across three or more groups. ANOVA partitions the total variance into between-group and within-group components.  \n**H₀:** All group means are equal.  \n**H₁:** At least one group mean is significantly different (α = 0.05)."),
    md_cell("### 6. Tukey HSD Post-Hoc Test\nWhen ANOVA is significant, Tukey's Honestly Significant Difference test identifies *which specific pairs* of groups differ. It controls the family-wise error rate across all pairwise comparisons, providing more rigour than running multiple t-tests."),
    md_cell("### 7. Summary of Test Results\nCollect all test statistics, p-values, and decisions (Reject / Fail to Reject H₀) into a summary DataFrame and export to CSV for reporting."),
]

SECTIONS_06 = [
    md_cell("### 1. Setup & Imports\nImport statsmodels for OLS regression, scikit-learn for train/test splitting and metrics, and seaborn/matplotlib for diagnostic visualisations."),
    md_cell("### 2. Load & Prepare Dataset\nLoad the preprocessed dataset, select relevant numeric features, and separate the target variable from predictors. Drop any remaining non-numeric columns that cannot be used by the OLS estimator."),
    md_cell("### 3. Train / Test Split\nPartition the data into training (80%) and test (20%) sets using a fixed random seed. The model is fitted on the training set and evaluated on the held-out test set to estimate generalisation performance."),
    md_cell("### 4. OLS Regression Model\nFit an Ordinary Least Squares regression using statsmodels. The full summary table reports coefficients, standard errors, t-statistics, p-values, R², and F-statistic — providing a complete picture of model fit and individual predictor significance."),
    md_cell("### 5. Prediction & Performance Metrics\nGenerate predictions on the test set and compute R² (proportion of variance explained), RMSE (root mean squared error, in the target's units), and MAE (mean absolute error). Together these metrics capture both accuracy and error magnitude."),
    md_cell("### 6. Variance Inflation Factor (VIF) — Multicollinearity Check\nCompute VIF for each predictor. VIF > 5 indicates moderate multicollinearity; VIF > 10 signals severe multicollinearity that can destabilise coefficient estimates and inflate standard errors. Predictors with high VIF may need to be removed or combined."),
    md_cell("### 7. Residual Analysis\nPlot residuals (actual − predicted) against fitted values. A random scatter around zero indicates homoscedasticity (constant variance). Systematic patterns suggest model misspecification or heteroscedasticity."),
    md_cell("### 8. Q-Q Plot — Normality of Residuals\nA Quantile-Quantile plot compares the empirical distribution of residuals to the theoretical normal distribution. Points falling along the diagonal line confirm the OLS assumption of normally distributed errors, which underpins valid hypothesis tests on coefficients."),
    md_cell("### 9. Cook's Distance — Influential Point Detection\nCook's Distance measures how much each observation shifts the fitted values if it were removed. Observations with Cook's D > 4/n are flagged as potentially influential and may warrant closer inspection or removal."),
    md_cell("### 10. Export Regression Results\nSave predictions, residuals, and diagnostic metrics to CSV for further analysis or reporting."),
]

SECTIONS_08 = [
    md_cell("### 1. Setup & Imports\nImport scikit-learn classifiers (LogisticRegression, KNeighborsClassifier, GaussianNB), preprocessing (StandardScaler), evaluation utilities (ROC curve, AUC, classification_report), and visualisation libraries."),
    md_cell("### 2. Load & Prepare Dataset\nLoad the preprocessed dataset, define the binary target variable, and select numeric predictor features. Inspect class distribution to check for imbalance that might require stratified splitting."),
    md_cell("### 3. Train / Test Split\nSplit data 80/20 with stratification to preserve class proportions in both sets. Stratified splitting is especially important for imbalanced classification tasks."),
    md_cell("### 4. Feature Scaling\nApply StandardScaler fitted on the training set and transform both train and test sets. Scaling is essential for Logistic Regression and KNN, which are sensitive to feature magnitudes."),
    md_cell("### 5. Logistic Regression\nTrain a Logistic Regression model and interpret coefficients as log-odds. Exponentiate coefficients to obtain odds ratios, which communicate the multiplicative change in odds for a one-unit increase in each predictor."),
    md_cell("### 6. K-Nearest Neighbours — K Hyperparameter Tuning\nEvaluate KNN accuracy across a range of K values (odd numbers to avoid ties). Select the K that maximises cross-validated accuracy. Plotting accuracy vs. K reveals the bias-variance trade-off: small K overfits, large K underfits."),
    md_cell("### 7. Gaussian Naive Bayes\nTrain a Gaussian Naive Bayes classifier, which assumes conditional feature independence given the class label. Despite this strong assumption, it often performs competitively on small datasets and provides a probabilistic baseline."),
    md_cell("### 8. Model Evaluation — Confusion Matrix & Classification Report\nGenerate confusion matrices and classification reports (precision, recall, F1-score) for all three models. These metrics provide a richer picture of classifier performance than accuracy alone, particularly under class imbalance."),
    md_cell("### 9. ROC Curves & AUC Comparison\nPlot Receiver Operating Characteristic curves for all three classifiers on the same axes. The Area Under the Curve (AUC) summarises each model's ability to discriminate between classes across all decision thresholds. AUC = 1.0 is perfect; AUC = 0.5 is no better than random."),
]

SECTIONS_09 = [
    md_cell("### 1. Setup & Imports\nImport scikit-learn tree and ensemble estimators, model selection utilities (cross_val_score, train_test_split), and permutation importance. Set a random seed for reproducibility."),
    md_cell("### 2. Load & Prepare Dataset\nLoad the preprocessed dataset, define the target variable, and select predictor features. Ensure there are no remaining NaN values that would cause tree splitting to fail."),
    md_cell("### 3. Train / Test Split\nPartition data 80/20. Consistent splitting across experiments enables fair comparison of model performance."),
    md_cell("### 4. Decision Tree — Full Depth (Baseline)\nTrain an unconstrained Decision Tree with Gini impurity. A fully grown tree typically overfits the training data (low bias, high variance), establishing a performance ceiling that ensemble methods aim to surpass on unseen data."),
    md_cell("### 5. Decision Tree — Restricted Depth\nTrain a Decision Tree with a limited `max_depth` to control overfitting. Depth restriction acts as regularisation: it increases bias slightly but reduces variance, often yielding better generalisation. Compare test accuracy with the full-depth tree."),
    md_cell("### 6. Random Forest — n_estimators Tuning\nTrain Random Forests with increasing numbers of trees (`n_estimators`). Plot OOB (Out-Of-Bag) error vs. number of trees to identify the point of diminishing returns. OOB error provides an unbiased estimate of generalisation error without a separate validation set."),
    md_cell("### 7. Random Forest — Final Model & Evaluation\nFit the final Random Forest with the chosen `n_estimators` and evaluate on the held-out test set. Compare accuracy, precision, recall, and F1 against the Decision Tree baselines to quantify the ensemble benefit."),
    md_cell("### 8. Feature Importance — Gini Impurity\nExtract mean Gini impurity decrease for each feature from the trained Random Forest. Features that consistently reduce impurity across many trees are ranked highest. Visualise as a horizontal bar chart."),
    md_cell("### 9. Permutation Feature Importance\nCompute permutation importance by randomly shuffling each feature column on the test set and measuring the resulting drop in accuracy. Unlike Gini importance, permutation importance is model-agnostic and unbiased towards high-cardinality features."),
    md_cell("### 10. Cross-Validation\nRun stratified k-fold cross-validation on the final Random Forest to confirm that the test-set performance is not a lucky split. Report mean and standard deviation of accuracy across folds."),
]

# Map experiment filename fragment -> (title_cell_func, section_cells_list)
EXP_CONFIG = {
    "Exp_01": (title_cell_01, SECTIONS_01),
    "Exp_02": (title_cell_02, SECTIONS_02),
    "Exp_03": (title_cell_03, SECTIONS_03),
    "Exp_04": (title_cell_04, SECTIONS_04),
    "Exp_06": (title_cell_06, SECTIONS_06),
    "Exp_08": (title_cell_08, SECTIONS_08),
    "Exp_09": (title_cell_09, SECTIONS_09),
}

DATASET_NAMES = {
    "Housing": "Housing Dataset (Real-Estate Pricing)",
    "Iris": "Iris Dataset (Fisher's Classic)",
    "Titanic": "Titanic Dataset (Passenger Survival)",
}

# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def process_notebook(nb_path, dataset_name, title_fn, section_cells):
    nb = load_nb(nb_path)
    cells = nb["cells"]

    # 1. Prepend title cell
    title = title_fn(dataset_name)
    cells.insert(0, title)

    # 2. Insert section markdown cells before each code cell.
    #    We work backwards through the list so that insertions don't shift indices.
    #    Find all code cells (after the title we just added, so original code cells
    #    now start at index 1).
    code_indices = [i for i, c in enumerate(cells) if c["cell_type"] == "code"]

    # Pair section cells with code cell positions. If there are more code cells
    # than section descriptions, we skip (don't annotate extra cells).
    for section_idx, code_cell_pos in enumerate(reversed(code_indices)):
        if section_idx >= len(section_cells):
            break
        # section_cells are in forward order; reversed code_indices means we
        # insert the last section first to keep indices stable.
        section = section_cells[len(section_cells) - 1 - section_idx]
        cells.insert(code_cell_pos, section)

    nb["cells"] = cells
    save_nb(nb_path, nb)


def main():
    datasets = ["Housing", "Iris", "Titanic"]
    total = 0

    for ds in datasets:
        ds_dir = os.path.join(REPO_ROOT, ds)
        for exp_key, (title_fn, sections) in EXP_CONFIG.items():
            # Find the notebook matching this experiment key
            candidates = [f for f in os.listdir(ds_dir) if f.startswith(exp_key) and f.endswith(".ipynb")]
            if not candidates:
                print(f"WARNING: No notebook found for {exp_key} in {ds_dir}")
                continue
            nb_path = os.path.join(ds_dir, candidates[0])
            dataset_name = DATASET_NAMES[ds]
            process_notebook(nb_path, dataset_name, title_fn, sections)
            total += 1

    print(f"\n✅ All done. {total} notebooks documented.")


if __name__ == "__main__":
    main()
