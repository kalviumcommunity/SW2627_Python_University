"""
============================================================
PHASE 6 : BUSINESS INSIGHTS
============================================================

Objective:
Generate business summaries, insights and recommendations
from the feature engineered dataset.

Author : SW Team 1 KARE
============================================================
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import os
import pandas as pd

print("=" * 60)
print("PHASE 6 : BUSINESS INSIGHTS")
print("=" * 60)

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "featured_final_marks.csv"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output",
    "summaries"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================================
# LOAD DATASET
# ==========================================================

print("\nLoading Feature Engineered Dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully.")

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# ==========================================================
# SUMMARY STATISTICS
# ==========================================================

print("\nGenerating Summary Statistics...")

summary = df.select_dtypes(include="number").describe().round(2)

summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "business_summary.csv"
    )
)

print("Summary Statistics Saved.")

# ==========================================================
# ACADEMIC RISK SUMMARY
# ==========================================================

print("\nAcademic Risk Summary")

risk_summary = (

    df

    .groupby("Academic_Risk")

    [

        [

            "Attendance (%)",

            "Daily Study Hours",

            "Assignment Score (out of 10)",

            "Average_Internal_Score",

            "Engagement_Score",

            "Final Exam Marks (out of 100)"

        ]

    ]

    .mean()

    .round(2)

)

risk_summary.to_csv(

    os.path.join(

        OUTPUT_DIR,

        "risk_summary.csv"

    )

)

print(risk_summary)

# ==========================================================
# ATTENDANCE SUMMARY
# ==========================================================

attendance_summary = (

    df

    .groupby("Attendance_Category")

    [

        [

            "Average_Internal_Score",

            "Engagement_Score",

            "Final Exam Marks (out of 100)"

        ]

    ]

    .mean()

    .round(2)

)

attendance_summary.to_csv(

    os.path.join(

        OUTPUT_DIR,

        "attendance_summary.csv"

    )

)

print("\nAttendance Summary Created.")

# ==========================================================
# STUDY HOURS SUMMARY
# ==========================================================

study_summary = (

    df

    .groupby("Study_Hours_Category")

    [

        [

            "Average_Internal_Score",

            "Engagement_Score",

            "Final Exam Marks (out of 100)"

        ]

    ]

    .mean()

    .round(2)

)

study_summary.to_csv(

    os.path.join(

        OUTPUT_DIR,

        "study_hours_summary.csv"

    )

)

print("Study Hours Summary Created.")

# ==========================================================
# ENGAGEMENT SUMMARY
# ==========================================================

engagement_summary = (

    df

    .groupby("Engagement_Level")

    [

        [

            "Attendance (%)",

            "Average_Internal_Score",

            "Final Exam Marks (out of 100)"

        ]

    ]

    .mean()

    .round(2)

)

engagement_summary.to_csv(

    os.path.join(

        OUTPUT_DIR,

        "engagement_summary.csv"

    )

)

print("Engagement Summary Created.")

# ==========================================================
# GRADE DISTRIBUTION
# ==========================================================

grade_summary = (

    df["Performance_Grade"]

    .value_counts()

    .sort_index()

)

grade_summary.to_csv(

    os.path.join(

        OUTPUT_DIR,

        "grade_distribution.csv"

    )

)

print("Grade Distribution Saved.")

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

numeric_columns = [

    "Attendance (%)",

    "Internal Test 1 (out of 40)",

    "Internal Test 2 (out of 40)",

    "Assignment Score (out of 10)",

    "Daily Study Hours",

    "Average_Internal_Score",

    "Total_Internal_Score",

    "Engagement_Score",

    "Final Exam Marks (out of 100)"

]

correlation = (

    df[numeric_columns]

    .corr()["Final Exam Marks (out of 100)"]

    .sort_values(ascending=False)

)

correlation.to_csv(

    os.path.join(

        OUTPUT_DIR,

        "feature_importance.csv"

    )

)

print("Feature Importance Saved.")

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

insights = []

risk_percent = (

    df["Academic_Risk"]

    .value_counts(normalize=True)

    .mul(100)

    .round(2)

)

for risk, value in risk_percent.items():

    insights.append(

        f"{value}% of students belong to the '{risk}' category."

    )

best_attendance = risk_summary["Attendance (%)"].idxmax()

lowest_attendance = risk_summary["Attendance (%)"].idxmin()

insights.append(

    f"Students classified as '{best_attendance}' have the highest average attendance."

)

insights.append(

    f"Students classified as '{lowest_attendance}' have the lowest average attendance."

)

best_study = study_summary["Final Exam Marks (out of 100)"].idxmax()

insights.append(

    f"Students with '{best_study}' study habits achieve the highest average final marks."

)

best_engagement = engagement_summary["Final Exam Marks (out of 100)"].idxmax()

insights.append(

    f"Students with '{best_engagement}' engagement demonstrate the strongest academic performance."

)

predictors = correlation.drop("Final Exam Marks (out of 100)")

insights.append(

    f"The strongest predictor of final examination marks is '{predictors.idxmax()}' with correlation {predictors.max():.2f}."

)

pd.DataFrame(

    {

        "Business Insights": insights

    }

).to_csv(

    os.path.join(

        OUTPUT_DIR,

        "business_insights.csv"

    ),

    index=False

)

print("Business Insights Generated.")

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

recommendations = [

    "Monitor students with attendance below 75%.",

    "Identify High Risk students after internal assessments.",

    "Promote consistent daily study habits.",

    "Increase mentoring support for Low Engagement students.",

    "Track assignment completion every week.",

    "Use internal test scores for early intervention.",

    "Implement an academic risk dashboard for faculty.",

    "Provide personalized learning support for High Risk students.",

    "Reward students maintaining excellent attendance.",

    "Review engagement metrics every semester."

]

pd.DataFrame(

    {

        "Recommendations": recommendations

    }

).to_csv(

    os.path.join(

        OUTPUT_DIR,

        "recommendations.csv"

    ),

    index=False

)

print("Recommendations Generated.")

print("\n" + "="*60)
print("PHASE 6 COMPLETED")
print("="*60)

print("Generated Files")

print("-----------------------")

files = [

    "business_summary.csv",

    "risk_summary.csv",

    "attendance_summary.csv",

    "study_hours_summary.csv",

    "engagement_summary.csv",

    "grade_distribution.csv",

    "feature_importance.csv",

    "business_insights.csv",

    "recommendations.csv"

]

for file in files:

    print(f"✔ {file}")

print("\nReady for Report Generation.")