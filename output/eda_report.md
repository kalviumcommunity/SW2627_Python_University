# Academic Risk Analysis - Exploratory Data Analysis (EDA) Report

## Executive Summary
This report presents the findings from the Exploratory Data Analysis (EDA) conducted on the cleaned dataset of **2000 student records**. The analysis evaluates key factors influencing student academic performance and identifies indicators for academic risk.

---

## Key Findings

### 1. Feature Correlations with Final Exam Marks
The features most strongly correlated with **Final Exam Marks** are:
1. **Internal Test 1 & Internal Test 2**: Strong positive correlation ($r \approx 0.69$ and $r \approx 0.69$).
2. **Attendance (%)**: Positive correlation ($r \approx 0.73$).
3. **Daily Study Hours**: Moderate positive correlation ($r \approx 0.41$).

---

## Summary Statistics Table

| Feature | Mean | Std | Min | Median | Max | Skewness |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Attendance (%) | 84.89 | 7.76 | 52.00 | 85.00 | 100.00 | -0.14 |
| Internal Test 1 (out of 40) | 32.12 | 4.56 | 18.00 | 32.00 | 40.00 | -0.23 |
| Internal Test 2 (out of 40) | 32.46 | 4.52 | 16.00 | 33.00 | 40.00 | -0.21 |
| Assignment Score (out of 10) | 7.51 | 1.02 | 4.00 | 8.00 | 10.00 | -0.13 |
| Daily Study Hours | 2.82 | 0.61 | 1.00 | 3.00 | 5.00 | -0.04 |
| Final Exam Marks (out of 100) | 64.86 | 11.34 | 25.00 | 65.00 | 100.00 | -0.12 |

---

## Academic Risk Group Breakdown

- **Total Students Analyzed**: 2000
- **High Risk (<50)**: 188 students (9.40%)
- **Moderate (50-74)**: 1387 students (69.35%)
- **High Performer (>=75)**: 425 students (21.25%)

---

## Key Takeaways & Recommendations

1. **Early Intervention Indicator**: Internal Test 1 and Test 2 performance are strong predictors of final marks. Students scoring below 50% in internal tests should be flagged for academic counseling.
2. **Attendance Requirement**: Attendance below 75% significantly corresponds with lower final examination outcomes.
3. **Study Hours**: Students maintaining consistent daily study hours (>= 3 hours) demonstrate noticeably higher average final performance.

---

## Visualizations Generated
- `output/figures/01_distributions.png`: Univariate feature distributions and density estimates.
- `output/figures/02_boxplots_outliers.png`: Boxplots illustrating value spreads and potential outliers.
- `output/figures/03_correlation_heatmap.png`: Correlation matrix of numeric attributes.
- `output/figures/04_relationships.png`: Regression plots showing key drivers of final marks.
- `output/figures/05_risk_group_analysis.png`: Risk level distributions and attendance impacts.
