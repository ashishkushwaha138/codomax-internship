"""
Day 4 - Pandas Fundamentals: Student Score Dataset Exploration
Internship Task: Import Pandas, load student score dataset, explore rows, columns, and dataset info.
Expected Outcome: Dataset loaded successfully.
"""

import pandas as pd
import numpy as np

# ============================================================
# TASK 1: IMPORT PANDAS
# ============================================================
print("=" * 60)
print("DAY 4 - PANDAS FUNDAMENTALS: STUDENT SCORE DATASET")
print("=" * 60)
print("\n✓ Task 1: Import Pandas")
print(f"    Pandas version: {pd.__version__}")
print(f"    NumPy version:  {np.__version__}")

# ============================================================
# TASK 2: CREATE/LOAD STUDENT SCORE DATASET
# ============================================================
print("\n" + "=" * 60)
print("✓ Task 2: Create/Load Student Score Dataset")
print("=" * 60)

# Create a sample student score dataset
np.random.seed(42)  # For reproducibility

n_students = 100
data = {
    'student_id': [f'STU{str(i).zfill(3)}' for i in range(1, n_students + 1)],
    'name': [f'Student_{i}' for i in range(1, n_students + 1)],
    'age': np.random.randint(17, 25, n_students),
    'gender': np.random.choice(['Male', 'Female', 'Other'], n_students, p=[0.48, 0.48, 0.04]),
    'department': np.random.choice(['Computer Science', 'Electronics', 'Mechanical', 'Civil', 'Chemical'], n_students),
    'math_score': np.random.normal(75, 15, n_students).clip(0, 100).round(1),
    'physics_score': np.random.normal(72, 14, n_students).clip(0, 100).round(1),
    'chemistry_score': np.random.normal(70, 16, n_students).clip(0, 100).round(1),
    'english_score': np.random.normal(78, 12, n_students).clip(0, 100).round(1),
    'cs_score': np.random.normal(80, 10, n_students).clip(0, 100).round(1),
    'attendance_pct': np.random.normal(85, 10, n_students).clip(50, 100).round(1),
    'study_hours_per_week': np.random.normal(15, 5, n_students).clip(0, 40).round(1),
    'extracurricular': np.random.choice(['Sports', 'Music', 'Debate', 'Coding', 'None'], n_students),
    'scholarship': np.random.choice([True, False], n_students, p=[0.3, 0.7]),
    'placement_status': np.random.choice(['Placed', 'Not Placed', 'Higher Studies'], n_students, p=[0.65, 0.25, 0.10])
}

df = pd.DataFrame(data)

# Save to CSV for submission/reference
csv_path = '/home/ubuntu/.openclaw/workspace/day4/student_scores.csv'
df.to_csv(csv_path, index=False)
print(f"\n✓ Dataset created and saved to: {csv_path}")
print(f"    Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# Also load from CSV to demonstrate loading (simulating real scenario)
df_loaded = pd.read_csv(csv_path)
print(f"✓ Dataset loaded successfully from CSV!")
print(f"    Loaded shape: {df_loaded.shape[0]} rows × {df_loaded.shape[1]} columns")

# ============================================================
# TASK 3: EXPLORE ROWS, COLUMNS, AND DATASET INFORMATION
# ============================================================
print("\n" + "=" * 60)
print("✓ Task 3: Explore Rows, Columns, and Dataset Information")
print("=" * 60)

# 3.1: Basic shape info
print("\n📊 3.1 DATASET SHAPE")
print("-" * 40)
print(f"    Number of rows (students): {df.shape[0]}")
print(f"    Number of columns (features): {df.shape[1]}")
print(f"    Total data points: {df.size:,}")

# 3.2: Column names and types
print("\n📋 3.2 COLUMN INFORMATION")
print("-" * 40)
print(f"    Column names ({len(df.columns)}):")
for i, col in enumerate(df.columns, 1):
    dtype = df[col].dtype
    non_null = df[col].notna().sum()
    print(f"      {i:2d}. {col:<25} | {str(dtype):<10} | Non-null: {non_null}/{len(df)}")

# 3.3: Data types summary
print("\n📊 3.3 DATA TYPES SUMMARY")
print("-" * 40)
print(df.dtypes.value_counts())

# 3.4: First 5 rows (head)
print("\n👀 3.4 FIRST 5 ROWS (df.head())")
print("-" * 40)
print(df.head().to_string())

# 3.5: Last 5 rows (tail)
print("\n👀 3.5 LAST 5 ROWS (df.tail())")
print("-" * 40)
print(df.tail().to_string())

# 3.6: Random 5 rows (sample)
print("\n🎲 3.6 RANDOM 5 ROWS (df.sample(5))")
print("-" * 40)
print(df.sample(5, random_state=42).to_string())

# 3.7: Dataset info (memory usage, non-null counts)
print("\n📋 3.7 DATASET INFO (df.info())")
print("-" * 40)
df.info(verbose=True, show_counts=True)

# 3.8: Statistical summary (describe)
print("\n📈 3.8 STATISTICAL SUMMARY (df.describe())")
print("-" * 40)
print(df.describe(include='all').to_string())

# 3.9: Numeric columns only summary
print("\n📈 3.9 NUMERIC COLUMNS SUMMARY (df.describe())")
print("-" * 40)
print(df.select_dtypes(include=[np.number]).describe().to_string())

# 3.10: Categorical columns summary
print("\n📋 3.10 CATEGORICAL COLUMNS SUMMARY")
print("-" * 40)
cat_cols = df.select_dtypes(include=['object', 'bool']).columns
for col in cat_cols:
    print(f"\n    {col}:")
    print(f"      Unique values: {df[col].nunique()}")
    print(f"      Top 5 values:")
    print(df[col].value_counts().head().to_string())

# 3.11: Memory usage
print("\n💾 3.11 MEMORY USAGE")
print("-" * 40)
print(f"    Total memory usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
print("\n    Per column:")
for col in df.columns:
    mem = df[col].memory_usage(deep=True) / 1024
    print(f"      {col:<25} {mem:>8.2f} KB")

# 3.12: Missing values check
print("\n❓ 3.12 MISSING VALUES CHECK")
print("-" * 40)
missing = df.isnull().sum()
if missing.sum() == 0:
    print("    ✓ No missing values found!")
else:
    print(missing[missing > 0])

# 3.13: Duplicate rows check
print("\n🔄 3.13 DUPLICATE ROWS CHECK")
print("-" * 40)
dupes = df.duplicated().sum()
print(f"    Duplicate rows: {dupes}")

# 3.14: Unique values per column
print("\n🔢 3.14 UNIQUE VALUES PER COLUMN")
print("-" * 40)
for col in df.columns:
    print(f"    {col:<25} {df[col].nunique():>4} unique values")

# ============================================================
# TASK 4: BASIC DATA EXPLORATION - SPECIFIC INSIGHTS
# ============================================================
print("\n" + "=" * 60)
print("✓ Task 4: Basic Data Exploration - Key Insights")
print("=" * 60)

# 4.1: Average scores by department
print("\n📊 4.1 AVERAGE SCORES BY DEPARTMENT")
print("-" * 40)
score_cols = ['math_score', 'physics_score', 'chemistry_score', 'english_score', 'cs_score']
dept_avg = df.groupby('department')[score_cols].mean().round(2)
print(dept_avg.to_string())

# 4.2: Placement statistics
print("\n🎓 4.2 PLACEMENT STATUS DISTRIBUTION")
print("-" * 40)
placement_dist = df['placement_status'].value_counts()
placement_pct = df['placement_status'].value_counts(normalize=True).mul(100).round(1)
for status in placement_dist.index:
    print(f"    {status:<15} {placement_dist[status]:>4} students ({placement_pct[status]}%)")

# 4.3: Scholarship vs placement
print("\n💰 4.3 SCHOLARSHIP vs PLACEMENT")
print("-" * 40)
scholar_place = pd.crosstab(df['scholarship'], df['placement_status'], normalize='index').mul(100).round(1)
print(scholar_place.to_string())

# 4.4: Gender distribution
print("\n👥 4.4 GENDER DISTRIBUTION")
print("-" * 40)
gender_dist = df['gender'].value_counts()
gender_pct = df['gender'].value_counts(normalize=True).mul(100).round(1)
for g in gender_dist.index:
    print(f"    {g:<10} {gender_dist[g]:>4} ({gender_pct[g]}%)")

# 4.5: Top 10 students by average score
print("\n🏆 4.5 TOP 10 STUDENTS BY AVERAGE SCORE")
print("-" * 40)
df['average_score'] = df[score_cols].mean(axis=1).round(2)
top10 = df.nlargest(10, 'average_score')[['student_id', 'name', 'department', 'average_score']]
print(top10.to_string(index=False))

# 4.6: Correlation matrix (numeric only)
print("\n📐 4.6 CORRELATION MATRIX (NUMERIC COLUMNS)")
print("-" * 40)
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr().round(2)
print(corr_matrix.to_string())

# ============================================================
# TASK 5: SAVE EXPLORATION RESULTS
# ============================================================
print("\n" + "=" * 60)
print("✓ Task 5: Save Exploration Results for Submission")
print("=" * 60)

# Save summary report
report_path = '/home/ubuntu/.openclaw/workspace/day4/exploration_report.txt'
with open(report_path, 'w') as f:
    f.write("DAY 4 - PANDAS FUNDAMENTALS: STUDENT SCORE DATASET EXPLORATION REPORT\n")
    f.write("=" * 70 + "\n\n")
    f.write(f"Dataset: student_scores.csv\n")
    f.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
    f.write(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB\n")
    f.write(f"Missing Values: {df.isnull().sum().sum()}\n")
    f.write(f"Duplicate Rows: {df.duplicated().sum()}\n\n")
    
    f.write("COLUMNS:\n")
    for i, col in enumerate(df.columns, 1):
        f.write(f"  {i:2d}. {col:<25} | {str(df[col].dtype):<10} | Unique: {df[col].nunique()}\n")
    
    f.write("\n\nSTATISTICAL SUMMARY (NUMERIC):\n")
    f.write(df.describe().to_string())
    
    f.write("\n\nPLACEMENT DISTRIBUTION:\n")
    f.write(placement_dist.to_string())
    
    f.write("\n\nTOP 10 STUDENTS BY AVERAGE SCORE:\n")
    f.write(top10.to_string(index=False))

print(f"\n✓ Exploration report saved to: {report_path}")
print(f"✓ Dataset CSV saved to: {csv_path}")

# ============================================================
# TASK 6: GOOGLE FORM SUBMISSION DATA (READY TO COPY)
# ============================================================
print("\n" + "=" * 60)
print("✓ Task 6: Google Form Submission Data (Copy-Paste Ready)")
print("=" * 60)

print("\n📋 GOOGLE FORM SUBMISSION DATA:")
print("-" * 40)
print(f"Dataset Name: Student Score Dataset")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Columns List: {', '.join(df.columns.tolist())}")
print(f"Data Types: {df.dtypes.value_counts().to_dict()}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
print(f"Departments: {', '.join(sorted(df['department'].unique()))}")
print(f"Placement Rate: {(df['placement_status'] == 'Placed').mean() * 100:.1f}%")
print(f"Scholarship Rate: {df['scholarship'].mean() * 100:.1f}%")
print(f"Average Math Score: {df['math_score'].mean():.2f}")
print(f"Average CS Score: {df['cs_score'].mean():.2f}")
print(f"Top Student: {top10.iloc[0]['name']} ({top10.iloc[0]['average_score']:.2f} avg)")

print("\n" + "=" * 60)
print("✅ DAY 4 TASK COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("✓ Pandas imported successfully")
print("✓ Student score dataset created and loaded")
print("✓ Rows, columns, and dataset information explored")
print("✓ Dataset loaded successfully - READY FOR GOOGLE FORM SUBMISSION")
print("=" * 60)

# Quick verification
print("\n🔍 QUICK VERIFICATION:")
print(f"   df.shape         -> {df.shape}")
print(f"   df.columns.tolist() -> {df.columns.tolist()}")
print(f"   df.dtypes        -> {df.dtypes.value_counts().to_dict()}")
print(f"   df.isnull().sum().sum() -> {df.isnull().sum().sum()}")
print(f"   df.head()        -> Shows first 5 rows ✓")
print(f"   df.info()        -> Shows memory, dtypes, non-null counts ✓")
print(f"   df.describe()    -> Shows statistical summary ✓")