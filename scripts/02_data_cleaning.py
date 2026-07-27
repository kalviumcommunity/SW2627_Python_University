"""
============================================================
PHASE 3 : DATA CLEANING
============================================================

This script performs the following cleaning operations:

1. Load Dataset
2. Remove Extra Spaces
3. Standardize Text Columns
4. Convert Data Types
5. Handle Missing Values
6. Remove Duplicate Rows
7. Validate Numeric Columns
8. Reset Index
9. Save Cleaned Dataset

Author : SW Team 1 KARE
============================================================
"""

import pandas as pd

print("=" * 60)
print("PHASE 3 : DATA CLEANING")
print("=" * 60)

# ----------------------------------------------------------
# LOAD DATASET
# ----------------------------------------------------------

print("\nLoading Dataset...")

df = pd.read_csv("../data/raw/Final_Marks_Data.csv")

rows_before = len(df)

print("Dataset Loaded Successfully.")
print(f"Rows : {rows_before}")
print(f"Columns : {len(df.columns)}")


# ----------------------------------------------------------
# REMOVE EXTRA SPACES
# ----------------------------------------------------------

print("\nRemoving Extra Spaces...")

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Remove spaces from all text columns
text_columns = df.select_dtypes(include=["object", "string"]).columns

for column in text_columns:
    df[column] = df[column].str.strip()

print("Extra Spaces Removed.")


# ----------------------------------------------------------
# STANDARDIZE TEXT DATA
# ----------------------------------------------------------

print("\nStandardizing Text Columns...")

for column in text_columns:
    df[column] = df[column].str.upper()

print("Text Standardization Completed.")


# ----------------------------------------------------------
# CONVERT DATA TYPES
# ----------------------------------------------------------

print("\nChecking Data Types...")

numeric_columns = [
    "Attendance (%)",
    "Internal Test 1 (out of 40)",
    "Internal Test 2 (out of 40)",
    "Assignment Score (out of 10)",
    "Daily Study Hours",
    "Final Exam Marks (out of 100)"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

print("Data Types Converted Successfully.")


# ----------------------------------------------------------
# HANDLE MISSING VALUES
# ----------------------------------------------------------

print("\nChecking Missing Values...")

missing_before = df.isnull().sum().sum()

print(f"Total Missing Values Before Cleaning : {missing_before}")

# Remove rows containing missing values
df = df.dropna()

missing_after = df.isnull().sum().sum()

print(f"Total Missing Values After Cleaning  : {missing_after}")


# ----------------------------------------------------------
# REMOVE DUPLICATE ROWS
# ----------------------------------------------------------

print("\nChecking Duplicate Rows...")

duplicates_before = df.duplicated().sum()

print(f"Duplicate Rows Found : {duplicates_before}")

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print(f"Duplicate Rows Remaining : {duplicates_after}")


# ----------------------------------------------------------
# REMOVE INVALID ATTENDANCE
# ----------------------------------------------------------

print("\nValidating Attendance...")

attendance_before = len(df)

df = df[
    (df["Attendance (%)"] >= 0) &
    (df["Attendance (%)"] <= 100)
]

attendance_removed = attendance_before - len(df)

print(f"Invalid Attendance Rows Removed : {attendance_removed}")


# ----------------------------------------------------------
# VALIDATE INTERNAL TEST 1
# ----------------------------------------------------------

print("\nValidating Internal Test 1...")

before = len(df)

df = df[
    (df["Internal Test 1 (out of 40)"] >= 0) &
    (df["Internal Test 1 (out of 40)"] <= 40)
]

print(f"Rows Removed : {before - len(df)}")


# ----------------------------------------------------------
# VALIDATE INTERNAL TEST 2
# ----------------------------------------------------------

print("\nValidating Internal Test 2...")

before = len(df)

df = df[
    (df["Internal Test 2 (out of 40)"] >= 0) &
    (df["Internal Test 2 (out of 40)"] <= 40)
]

print(f"Rows Removed : {before - len(df)}")


# ----------------------------------------------------------
# VALIDATE ASSIGNMENT SCORE
# ----------------------------------------------------------

print("\nValidating Assignment Score...")

before = len(df)

df = df[
    (df["Assignment Score (out of 10)"] >= 0) &
    (df["Assignment Score (out of 10)"] <= 10)
]

print(f"Rows Removed : {before - len(df)}")


# ----------------------------------------------------------
# VALIDATE DAILY STUDY HOURS
# ----------------------------------------------------------

print("\nValidating Daily Study Hours...")

before = len(df)

df = df[
    (df["Daily Study Hours"] >= 0) &
    (df["Daily Study Hours"] <= 24)
]

print(f"Rows Removed : {before - len(df)}")


# ----------------------------------------------------------
# VALIDATE FINAL EXAM MARKS
# ----------------------------------------------------------

print("\nValidating Final Exam Marks...")

before = len(df)

df = df[
    (df["Final Exam Marks (out of 100)"] >= 0) &
    (df["Final Exam Marks (out of 100)"] <= 100)
]

print(f"Rows Removed : {before - len(df)}")


# ----------------------------------------------------------
# RESET INDEX
# ----------------------------------------------------------

print("\nResetting Index...")

df.reset_index(drop=True, inplace=True)

print("Index Reset Completed.")


# ----------------------------------------------------------
# SAVE CLEANED DATASET
# ----------------------------------------------------------

output_path = "../data/processed/cleaned_final_marks.csv"

df.to_csv(output_path, index=False)

print("\nCleaned Dataset Saved Successfully.")
print(f"Location : {output_path}")


# ----------------------------------------------------------
# FINAL REPORT
# ----------------------------------------------------------

rows_after = len(df)

print("\n" + "=" * 60)
print("DATA CLEANING REPORT")
print("=" * 60)

print(f"Rows Before Cleaning : {rows_before}")
print(f"Rows After Cleaning  : {rows_after}")
print(f"Rows Removed         : {rows_before - rows_after}")

print("\nFinal Dataset Shape")
print(df.shape)

print("\nFirst Five Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

print("\nData Types")
print(df.dtypes)

print("\nCleaning Completed Successfully!")

print("\nThe following operations were performed:")

print("""
✔ Dataset Loaded
✔ Extra Spaces Removed
✔ Text Standardized
✔ Data Types Checked
✔ Missing Values Removed
✔ Duplicate Rows Removed
✔ Attendance Validated
✔ Internal Test 1 Validated
✔ Internal Test 2 Validated
✔ Assignment Score Validated
✔ Daily Study Hours Validated
✔ Final Exam Marks Validated
✔ Index Reset
✔ Cleaned Dataset Saved
""")