"""
Day 5 - Data Cleaning Tasks
Handle missing values, remove duplicates and understand dataset statistics.
Expected Outcome: Clean dataset prepared.
"""

import pandas as pd
import numpy as np

def load_data(filepath):
    """Load the dataset from CSV file."""
    df = pd.read_csv(filepath)
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def explore_data(df):
    """Explore and understand the dataset."""
    print("\n" + "="*60)
    print("DATASET EXPLORATION")
    print("="*60)
    
    print("\n1. First 5 rows:")
    print(df.head())
    
    print("\n2. Dataset info:")
    print(df.info())
    
    print("\n3. Descriptive statistics:")
    print(df.describe())
    
    print("\n4. Column names and types:")
    print(df.dtypes)
    
    print("\n5. Missing values count:")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    if missing.sum() == 0:
        print("No missing values found!")
    
    print("\n6. Duplicate rows:")
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}")
    
    print("\n7. Unique values per column:")
    for col in df.columns:
        print(f"  {col}: {df[col].nunique()} unique values")
    
    return df

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    print("\n" + "="*60)
    print("HANDLING MISSING VALUES")
    print("="*60)
    
    # Check for missing values
    missing_before = df.isnull().sum().sum()
    print(f"Total missing values before: {missing_before}")
    
    if missing_before > 0:
        # Check each column with missing values
        for col in df.columns:
            missing_count = df[col].isnull().sum()
            if missing_count > 0:
                print(f"\nColumn '{col}' has {missing_count} missing values")
                
                if df[col].dtype in ['float64', 'int64']:
                    # For numerical columns, fill with median
                    median_val = df[col].median()
                    df[col] = df[col].fillna(median_val)
                    print(f"  Filled with median: {median_val}")
                else:
                    # For categorical columns, fill with mode
                    mode_val = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
                    df[col] = df[col].fillna(mode_val)
                    print(f"  Filled with mode: {mode_val}")
    else:
        print("No missing values to handle.")
    
    missing_after = df.isnull().sum().sum()
    print(f"\nTotal missing values after: {missing_after}")
    
    return df

def handle_duplicates(df):
    """Remove duplicate rows from the dataset."""
    print("\n" + "="*60)
    print("HANDLING DUPLICATES")
    print("="*60)
    
    duplicates_before = df.duplicated().sum()
    print(f"Duplicate rows before: {duplicates_before}")
    
    if duplicates_before > 0:
        # Check for duplicates based on student_id (should be unique)
        dup_student_id = df.duplicated(subset=['student_id']).sum()
        print(f"Duplicate student_ids: {dup_student_id}")
        
        # Remove exact duplicate rows
        df = df.drop_duplicates()
        print(f"Removed exact duplicate rows")
        
        # Remove duplicates based on student_id (keep first)
        df = df.drop_duplicates(subset=['student_id'], keep='first')
        print(f"Removed duplicate student_ids (kept first)")
    else:
        print("No duplicate rows found.")
    
    duplicates_after = df.duplicated().sum()
    print(f"Duplicate rows after: {duplicates_after}")
    
    return df

def handle_categorical_missing(df):
    """Handle 'None' string values in categorical columns."""
    print("\n" + "="*60)
    print("HANDLING 'None' STRING VALUES IN CATEGORICAL COLUMNS")
    print("="*60)
    
    categorical_cols = ['extracurricular', 'gender']
    
    for col in categorical_cols:
        if col in df.columns:
            none_count = (df[col] == 'None').sum()
            if none_count > 0:
                print(f"Column '{col}' has {none_count} 'None' string values")
                df[col] = df[col].replace('None', np.nan)
                # Fill with mode
                mode_val = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
                df[col] = df[col].fillna(mode_val)
                print(f"  Replaced 'None' with NaN and filled with mode: '{mode_val}'")
    
    return df

def dataset_statistics(df):
    """Generate comprehensive dataset statistics."""
    print("\n" + "="*60)
    print("DATASET STATISTICS SUMMARY")
    print("="*60)
    
    print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    print("\nNumerical Columns Statistics:")
    num_cols = df.select_dtypes(include=[np.number]).columns
    print(df[num_cols].describe().round(2))
    
    print("\nCategorical Columns Statistics:")
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        print(f"\n{col}:")
        print(f"  Unique values: {df[col].nunique()}")
        print(f"  Top 5 values:\n{df[col].value_counts().head()}")
    
    # Check for outliers in numerical columns using IQR
    print("\nOutlier Detection (IQR method):")
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        if len(outliers) > 0:
            print(f"  {col}: {len(outliers)} outliers (bounds: {lower_bound:.2f} - {upper_bound:.2f})")
    
    return df

def save_cleaned_data(df, output_path):
    """Save the cleaned dataset."""
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to: {output_path}")
    print(f"Final shape: {df.shape[0]} rows × {df.shape[1]} columns")

def main():
    """Main data cleaning pipeline."""
    print("="*60)
    print("DAY 5 - DATA CLEANING PIPELINE")
    print("="*60)
    
    # Load data
    input_path = '/home/ubuntu/.openclaw/workspace/day4/student_scores.csv'
    output_path = '/home/ubuntu/.openclaw/workspace/day5/student_scores_cleaned.csv'
    
    df = load_data(input_path)
    
    # Explore data
    df = explore_data(df)
    
    # Handle 'None' string values in categorical columns
    df = handle_categorical_missing(df)
    
    # Handle missing values
    df = handle_missing_values(df)
    
    # Handle duplicates
    df = handle_duplicates(df)
    
    # Dataset statistics
    df = dataset_statistics(df)
    
    # Save cleaned data
    save_cleaned_data(df, output_path)
    
    print("\n" + "="*60)
    print("DATA CLEANING COMPLETE!")
    print("="*60)

if __name__ == "__main__":
    main()