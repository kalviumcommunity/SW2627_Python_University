"""
==========================================================
ACADEMIC RISK ANALYSIS PROJECT
Data Understanding
==========================================================

Objective:
Understand the dataset before performing any cleaning or analysis.

"""

# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import numpy as np

# ==========================================================
# 2. Load Dataset
# ==========================================================

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

df = pd.read_csv("../data/raw/Final_Marks_Data.csv")

print("Dataset loaded successfully!\n")

# ==========================================================
# 3. Display First Five Rows
# ==========================================================

print("=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)

print(df.head())

# ==========================================================
# 4. Display Last Five Rows
# ==========================================================

print("\n" + "=" * 60)
print("LAST FIVE ROWS")
print("=" * 60)

print(df.tail())

# ==========================================================
# 5. Dataset Shape
# ==========================================================

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)

rows, columns = df.shape

print(f"Number of Rows    : {rows}")
print(f"Number of Columns : {columns}")

# ==========================================================
# 6. Column Names
# ==========================================================

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

for column in df.columns:
    print(column)

# ==========================================================
# 7. Dataset Information
# ==========================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

# ==========================================================
# 8. Summary Statistics
# ==========================================================

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(df.describe())

# ==========================================================
# 9. Missing Values
# ==========================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ==========================================================
# 10. Duplicate Records
# ==========================================================

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

# ==========================================================
# 11. Data Types
# ==========================================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

# ==========================================================
# 12. Check for Invalid Attendance Values
# ==========================================================

print("\n" + "=" * 60)
print("ATTENDANCE VALIDATION")
print("=" * 60)

below_zero = (df["Attendance (%)"] < 0).sum()
above_hundred = (df["Attendance (%)"] > 100).sum()

print(f"Attendance below 0   : {below_zero}")
print(f"Attendance above 100 : {above_hundred}")

# ==========================================================
# 13. Check for Invalid Final Marks
# ==========================================================

print("\n" + "=" * 60)
print("FINAL MARKS VALIDATION")
print("=" * 60)

negative_marks = (df["Final Exam Marks (out of 100)"] < 0).sum()
marks_above_hundred = (df["Final Exam Marks (out of 100)"] > 100).sum()

print(f"Negative Marks    : {negative_marks}")
print(f"Marks Above 100   : {marks_above_hundred}")

# ==========================================================
# 14. Random Sample
# ==========================================================

print("\n" + "=" * 60)
print("RANDOM SAMPLE OF STUDENTS")
print("=" * 60)

print(df.sample(5))

# ==========================================================
# 15. Conclusion
# ==========================================================

print("\n" + "=" * 60)
print("PHASE 2 COMPLETED")
print("=" * 60)

print("""
Dataset Understanding Completed Successfully.

The following checks were performed:

✔ Dataset Loaded
✔ First & Last Records Viewed
✔ Dataset Shape Identified
✔ Column Names Reviewed
✔ Data Types Checked
✔ Summary Statistics Generated
✔ Missing Values Checked
✔ Duplicate Rows Checked
✔ Attendance Validation Completed
✔ Final Marks Validation Completed
✔ Random Sample Viewed

The dataset is now ready for Phase 3: Data Cleaning.
""")