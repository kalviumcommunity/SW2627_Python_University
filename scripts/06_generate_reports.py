"""
============================================================
PHASE 7 : REPORT GENERATION
============================================================

Objective:
Generate professional Markdown reports from the outputs
produced during the Business Insights phase.

Author : SW Team 1 KARE
============================================================
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import os
import pandas as pd

print("=" * 60)
print("PHASE 7 : REPORT GENERATION")
print("=" * 60)

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SUMMARY_DIR = os.path.join(
    BASE_DIR,
    "output",
    "summaries"
)

REPORT_DIR = os.path.join(
    BASE_DIR,
    "output",
    "reports"
)

os.makedirs(REPORT_DIR, exist_ok=True)

# ==========================================================
# LOAD GENERATED CSV FILES
# ==========================================================

business_summary = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "business_summary.csv"
    )
)

business_insights = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "business_insights.csv"
    )
)

recommendations = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "recommendations.csv"
    )
)

feature_importance = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "feature_importance.csv"
    )
)

risk_summary = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "risk_summary.csv"
    )
)

attendance_summary = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "attendance_summary.csv"
    )
)

study_summary = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "study_hours_summary.csv"
    )
)

engagement_summary = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "engagement_summary.csv"
    )
)

grade_distribution = pd.read_csv(
    os.path.join(
        SUMMARY_DIR,
        "grade_distribution.csv"
    )
)

print("All summary files loaded successfully.")

# ==========================================================
# BUSINESS INSIGHTS REPORT
# ==========================================================

business_report = os.path.join(
    REPORT_DIR,
    "business_insights.md"
)

with open(business_report, "w") as report:

    report.write("# Academic Risk Analysis\n\n")

    report.write("## Project Objective\n\n")

    report.write(
        "This report summarizes the findings obtained from the "
        "analysis of student attendance, assignments, internal "
        "assessments, study habits, and final examination marks. "
        "The objective is to identify engagement patterns that "
        "predict academic risk before final examinations.\n\n"
    )

    report.write("---\n\n")

    report.write("## Business Insights\n\n")

    for i, row in business_insights.iterrows():

        report.write(
            f"{i+1}. {row['Business Insights']}\n"
        )

    report.write("\n---\n\n")

    report.write("## Feature Importance Ranking\n\n")

    for _, row in feature_importance.iterrows():

        report.write(
            f"- **{row.iloc[0]}** : {round(row.iloc[1],2)}\n"
        )

    report.write("\n---\n\n")

    report.write("## Academic Risk Summary\n\n")

    report.write(
        risk_summary.to_markdown(index=False)
    )

    report.write("\n\n---\n\n")

    report.write("## Attendance Summary\n\n")

    report.write(
        attendance_summary.to_markdown(index=False)
    )

    report.write("\n\n---\n\n")

    report.write("## Study Hours Summary\n\n")

    report.write(
        study_summary.to_markdown(index=False)
    )

    report.write("\n\n---\n\n")

    report.write("## Engagement Summary\n\n")

    report.write(
        engagement_summary.to_markdown(index=False)
    )

    report.write("\n\n---\n\n")

    report.write("## Grade Distribution\n\n")

    report.write(
        grade_distribution.to_markdown(index=False)
    )

print("Business Insights Report Generated.")

# ==========================================================
# RECOMMENDATION REPORT
# ==========================================================

recommendation_report = os.path.join(
    REPORT_DIR,
    "recommendations.md"
)

with open(recommendation_report, "w") as report:

    report.write("# Academic Risk Analysis Recommendations\n\n")

    report.write(
        "The following recommendations are derived from the "
        "analysis performed on the student performance dataset.\n\n"
    )

    report.write("---\n\n")

    for i, row in recommendations.iterrows():

        report.write(
            f"{i+1}. {row['Recommendations']}\n"
        )

    report.write("\n---\n\n")

    report.write("## Conclusion\n\n")

    report.write(
        "The analysis indicates that attendance, engagement, "
        "study habits, assignment performance, and internal "
        "assessment scores are valuable indicators of academic "
        "performance. Monitoring these factors throughout the "
        "semester enables universities to identify at-risk "
        "students early and provide timely academic support."
    )

print("Recommendation Report Generated.")

# ==========================================================
# EXECUTION SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("REPORT GENERATION COMPLETED")
print("=" * 60)

generated_reports = [

    "business_insights.md",

    "recommendations.md"

]

print("\nGenerated Reports")

print("------------------------")

for report in generated_reports:

    print(f"✔ {report}")

print("\nLocation")

print(REPORT_DIR)

print("\nProject Completed Successfully!")

print("=" * 60)
