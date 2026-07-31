#!/usr/bin/env python3
"""
Day 9 - Prediction Tasks: Use trained model to predict student scores based on study hours.
"""

import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

os.makedirs('plots', exist_ok=True)

print("=" * 70)
print("DAY 9 - PREDICTION TASKS: STUDENT SCORE PREDICTION")
print("=" * 70)

# Load trained model
model_path = '../day8/models/linear_regression_model.pkl'
meta_path = '../day8/models/model_metadata.json'

print("\n1. LOADING TRAINED MODEL")
print("-" * 40)

model = joblib.load(model_path)
with open(meta_path) as f:
    metadata = json.load(f)

print(f"✓ Model loaded: {metadata['model_type']}")
print(f"✓ Features: {metadata['features']}")
print(f"✓ Test R²: {metadata['test_r2']:.4f}")
print(f"✓ Test RMSE: {metadata['test_rmse']:.4f}")

features = metadata['features']

# Load cleaned dataset for reference
df = pd.read_csv('../day5/student_scores_cleaned.csv')
score_cols = ['math_score', 'physics_score', 'chemistry_score', 'english_score', 'cs_score']
df['avg_score'] = df[score_cols].mean(axis=1)

# Focus: Predict based on study hours
print("\n2. PREDICTION BY STUDY HOURS (core task)")
print("-" * 40)

# Create study hour scenarios with average other features
avg_values = {
    'math_score': df['math_score'].mean(),
    'physics_score': df['physics_score'].mean(),
    'chemistry_score': df['chemistry_score'].mean(),
    'english_score': df['english_score'].mean(),
    'cs_score': df['cs_score'].mean(),
    'attendance_pct': df['attendance_pct'].mean(),
    'age': df['age'].mean()
}

study_hours_range = np.arange(0, 31, 2)
predictions_by_study = []

for hours in study_hours_range:
    student = avg_values.copy()
    student['study_hours_per_week'] = hours
    X = pd.DataFrame([student])[features]
    pred = model.predict(X)[0]
    predictions_by_study.append({'study_hours': hours, 'predicted_avg_score': pred})

pred_df = pd.DataFrame(predictions_by_study)
print(pred_df.to_string(index=False))

# Save predictions
pred_df.to_csv('predictions_by_study_hours.csv', index=False)
print("\n✓ Saved: predictions_by_study_hours.csv")

# Batch predictions on sample students
print("\n3. BATCH PREDICTIONS ON SAMPLE STUDENTS")
print("-" * 40)

samples = [
    {'name': 'High Performer', 'math': 95, 'physics': 92, 'chem': 90, 'eng': 88, 'cs': 94, 'att': 95, 'study': 25, 'age': 21},
    {'name': 'Average Student', 'math': 70, 'physics': 68, 'chem': 72, 'eng': 75, 'cs': 65, 'att': 80, 'study': 12, 'age': 20},
    {'name': 'Struggling Student', 'math': 45, 'physics': 50, 'chem': 48, 'eng': 55, 'cs': 42, 'att': 65, 'study': 5, 'age': 19},
    {'name': 'High Effort, Low Base', 'math': 60, 'physics': 58, 'chem': 62, 'eng': 65, 'cs': 55, 'att': 85, 'study': 20, 'age': 20},
    {'name': 'Low Effort, High Base', 'math': 85, 'physics': 82, 'chem': 88, 'eng': 80, 'cs': 84, 'att': 70, 'study': 8, 'age': 21},
]

results = []
for s in samples:
    X = pd.DataFrame([{
        'math_score': s['math'], 'physics_score': s['physics'],
        'chemistry_score': s['chem'], 'english_score': s['eng'],
        'cs_score': s['cs'], 'attendance_pct': s['att'],
        'study_hours_per_week': s['study'], 'age': s['age']
    }])[features]
    pred = model.predict(X)[0]
    results.append({'Student': s['name'], 'Study_Hours': s['study'], 'Predicted_Avg': round(pred, 2)})

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
results_df.to_csv('sample_predictions.csv', index=False)
print("\n✓ Saved: sample_predictions.csv")

# Predict on full dataset
print("\n4. FULL DATASET PREDICTIONS")
print("-" * 40)

X_full = df[features]
df['predicted_avg'] = model.predict(X_full)
df['residual'] = df['avg_score'] - df['predicted_avg']

out_cols = ['math_score', 'physics_score', 'chemistry_score', 'english_score', 'cs_score',
            'attendance_pct', 'study_hours_per_week', 'age', 'avg_score', 'predicted_avg', 'residual']
df[out_cols].to_csv('full_predictions.csv', index=False)
print(f"✓ Predictions for {len(df)} students saved: full_predictions.csv")
print(f"  Mean residual: {df['residual'].mean():.4f}")
print(f"  RMSE: {np.sqrt((df['residual']**2).mean()):.4f}")

# Visualizations
print("\n5. GENERATING VISUALIZATIONS")
print("-" * 40)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Study hours vs predicted score
ax = axes[0, 0]
ax.plot(pred_df['study_hours'], pred_df['predicted_avg_score'], 'o-', color='steelblue', linewidth=2, markersize=6)
ax.set_xlabel('Study Hours per Week')
ax.set_ylabel('Predicted Average Score')
ax.set_title('Predicted Score vs Study Hours\n(other features at dataset average)')
ax.grid(True, alpha=0.3)

# 2. Actual vs Predicted
ax = axes[0, 1]
ax.scatter(df['avg_score'], df['predicted_avg'], alpha=0.5, color='steelblue', s=30)
ax.plot([df['avg_score'].min(), df['avg_score'].max()],
        [df['avg_score'].min(), df['avg_score'].max()], 'r--', lw=2, label='Perfect')
ax.set_xlabel('Actual Average Score')
ax.set_ylabel('Predicted Average Score')
ax.set_title(f'Actual vs Predicted (All Data)\nR² = {metadata["test_r2"]:.4f}')
ax.legend()
ax.grid(True, alpha=0.3)

# 3. Residuals
ax = axes[1, 0]
ax.scatter(df['predicted_avg'], df['residual'], alpha=0.5, color='orange', s=30)
ax.axhline(0, color='red', linestyle='--', lw=2)
ax.set_xlabel('Predicted Average Score')
ax.set_ylabel('Residual')
ax.set_title('Residuals vs Predicted')
ax.grid(True, alpha=0.3)

# 4. Study hours distribution
ax = axes[1, 1]
ax.hist(df['study_hours_per_week'], bins=15, alpha=0.7, color='green', edgecolor='white', density=True)
ax.set_xlabel('Study Hours per Week')
ax.set_ylabel('Density')
ax.set_title('Study Hours Distribution in Dataset')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('plots/predictions_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: plots/predictions_analysis.png")

# Study hours specific plot
plt.figure(figsize=(10, 6))
plt.scatter(df['study_hours_per_week'], df['avg_score'], alpha=0.5, label='Actual', color='steelblue', s=40)
plt.scatter(df['study_hours_per_week'], df['predicted_avg'], alpha=0.5, label='Predicted', color='orange', s=40)
plt.plot(pred_df['study_hours'], pred_df['predicted_avg_score'], 'r-', lw=3, label='Trend (avg other features)')
plt.xlabel('Study Hours per Week')
plt.ylabel('Average Score')
plt.title('Study Hours vs Average Score: Actual vs Predicted')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('plots/study_hours_vs_score.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: plots/study_hours_vs_score.png")

# Summary
print("\n" + "=" * 70)
print("DAY 9 PREDICTION TASKS - COMPLETE")
print("=" * 70)

print(f"""
PREDICTIONS GENERATED:
✓ Study hours vs score mapping (0-30 hours)
✓ Sample student profiles (5 scenarios)
✓ Full dataset predictions ({len(df)} students)

KEY INSIGHTS:
- Study hours range in data: {df['study_hours_per_week'].min():.0f}-{df['study_hours_per_week'].max():.0f} hours/week
- Model R²: {metadata['test_r2']:.4f} (explains {metadata['test_r2']*100:.1f}% of variance)
- Each additional study hour ≈ +{pred_df['predicted_avg_score'].diff().mean():.2f} points (avg)

FILES CREATED:
  - predictions_by_study_hours.csv
  - sample_predictions.csv
  - full_predictions.csv
  - plots/predictions_analysis.png
  - plots/study_hours_vs_score.png

Task Status: COMPLETE ✓
""")