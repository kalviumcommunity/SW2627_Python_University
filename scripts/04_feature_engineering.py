"""
============================================================
PHASE 5 : FEATURE ENGINEERING
============================================================

This script performs feature engineering by creating new
meaningful features from the cleaned dataset.

Features Created:
1. Academic Risk
2. Attendance Category
3. Study Hours Category
4. Average Internal Score
5. Total Internal Score
6. Engagement Score
7. Engagement Level
8. Performance Grade

Author : SW Team 1 KARE
============================================================
"""

import pandas as pd
from pathlib import Path

print("=" * 60)
print("PHASE 5 : FEATURE ENGINEERING")
print("=" * 60)

# ----------------------------------------------------------
# Load Cleaned Dataset
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_final_marks.csv"

OUTPUT_PATH = (
    PROJECT_ROOT /
    "data" /
    "processed" /
    "featured_final_marks.csv"
)

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully.")
print(f"Shape : {df.shape}")

# ----------------------------------------------------------
# Academic Risk
# ----------------------------------------------------------

def academic_risk(mark):
    if mark < 50:
        return "High Risk"
    elif mark < 75:
        return "Moderate Risk"
    else:
        return "Low Risk"

df["Academic_Risk"] = df["Final Exam Marks (out of 100)"].apply(academic_risk)

print("Academic Risk Created.")

# ----------------------------------------------------------
# Attendance Category
# ----------------------------------------------------------

def attendance_category(attendance):
    if attendance >= 90:
        return "Excellent"
    elif attendance >= 75:
        return "Good"
    elif attendance >= 60:
        return "Average"
    else:
        return "Poor"

df["Attendance_Category"] = df["Attendance (%)"].apply(attendance_category)

print("Attendance Category Created.")

# ----------------------------------------------------------
# Study Hours Category
# ----------------------------------------------------------

def study_hours_category(hours):
    if hours >= 5:
        return "High"
    elif hours >= 3:
        return "Moderate"
    else:
        return "Low"

df["Study_Hours_Category"] = df["Daily Study Hours"].apply(study_hours_category)

print("Study Hours Category Created.")

# ----------------------------------------------------------
# Average Internal Score
# ----------------------------------------------------------

df["Average_Internal_Score"] = (
    df["Internal Test 1 (out of 40)"] +
    df["Internal Test 2 (out of 40)"]
) / 2

print("Average Internal Score Created.")

# ----------------------------------------------------------
# Total Internal Score
# ----------------------------------------------------------

df["Total_Internal_Score"] = (
    df["Internal Test 1 (out of 40)"] +
    df["Internal Test 2 (out of 40)"]
)

print("Total Internal Score Created.")

# ----------------------------------------------------------
# Engagement Score
# ----------------------------------------------------------

attendance = df["Attendance (%)"] / 100
assignment = df["Assignment Score (out of 10)"] / 10
study = df["Daily Study Hours"] / df["Daily Study Hours"].max()

df["Engagement_Score"] = (
    attendance +
    assignment +
    study
) / 3

print("Engagement Score Created.")

# ----------------------------------------------------------
# Engagement Level
# ----------------------------------------------------------

def engagement_level(score):
    if score >= 0.80:
        return "High"
    elif score >= 0.60:
        return "Moderate"
    else:
        return "Low"

df["Engagement_Level"] = df["Engagement_Score"].apply(engagement_level)

print("Engagement Level Created.")

# ----------------------------------------------------------
# Performance Grade
# ----------------------------------------------------------

def performance_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "F"

df["Performance_Grade"] = df["Final Exam Marks (out of 100)"].apply(performance_grade)

print("Performance Grade Created.")

# ----------------------------------------------------------
# Save Dataset
# ----------------------------------------------------------

df.to_csv(OUTPUT_PATH, index=False)

print("\nFeature Engineered Dataset Saved Successfully.")
print(f"Location : {OUTPUT_PATH}")

# ----------------------------------------------------------
# Preview
# ----------------------------------------------------------

print("\nNew Features Added:")

new_columns = [
    "Academic_Risk",
    "Attendance_Category",
    "Study_Hours_Category",
    "Average_Internal_Score",
    "Total_Internal_Score",
    "Engagement_Score",
    "Engagement_Level",
    "Performance_Grade"
]

print(df[new_columns].head())

print("\nFinal Dataset Shape")
print(df.shape)

print("\nFeature Engineering Completed Successfully!")