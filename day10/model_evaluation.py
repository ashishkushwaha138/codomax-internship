#!/usr/bin/env python3
"""
Day 10 - Model Evaluation Tasks
Evaluate the model using MAE, MSE and R² Score.
Expected Outcome: Model performance measured.
"""

import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

os.makedirs('plots', exist_ok=True)

print("=" * 70)
print("DAY 10 - MODEL EVALUATION TASKS")
print("Evaluate model using MAE, MSE and R² Score")
print("=" * 70)

# Load trained model and metadata
model_path = '../day8/models/linear_regression_model.pkl'
meta_path = '../day8/models/model_metadata.json'

print("\n1. LOADING TRAINED MODEL AND METADATA")
print("-" * 50)

model = joblib.load(model_path)
with open(meta_path) as f:
    metadata = json.load(f)

print(f"✓ Model loaded: {metadata['model_type']}")
print(f"✓ Features: {metadata['features']}")
print(f"✓ Test R² (from training): {metadata['test_r2']:.4f}")
print(f"✓ Test RMSE (from training): {metadata['test_rmse']:.4f}")

features = metadata['features']

# Load cleaned dataset
df = pd.read_csv('../day5/student_scores_cleaned.csv')
score_cols = ['math_score', 'physics_score', 'chemistry_score', 'english_score', 'cs_score']
df['avg_score'] = df[score_cols].mean(axis=1)

X = df[features]
y_true = df['avg_score']

# Make predictions on full dataset
y_pred = model.predict(X)

print("\n2. CALCULATING EVALUATION METRICS")
print("-" * 50)

# MAE - Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)
print(f"MAE (Mean Absolute Error): {mae:.6f}")

# MSE - Mean Squared Error
mse = mean_squared_error(y_true, y_pred)
print(f"MSE (Mean Squared Error):  {mse:.6f}")

# RMSE - Root Mean Squared Error
rmse = np.sqrt(mse)
print(f"RMSE (Root Mean Squared Error): {rmse:.6f}")

# R² Score - Coefficient of Determination
r2 = r2_score(y_true, y_pred)
print(f"R² Score (Coefficient of Determination): {r2:.6f}")

# Additional metrics
print("\n3. ADDITIONAL METRICS")
print("-" * 50)

# Mean Absolute Percentage Error (MAPE)
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
print(f"MAPE (Mean Absolute Percentage Error): {mape:.2f}%")

# Max Error
max_error = np.max(np.abs(y_true - y_pred))
print(f"Max Error: {max_error:.4f}")

# Median Absolute Error
median_ae = np.median(np.abs(y_true - y_pred))
print(f"Median Absolute Error: {median_ae:.4f}")

# Explained Variance Score
from sklearn.metrics import explained_variance_score
evs = explained_variance_score(y_true, y_pred)
print(f"Explained Variance Score: {evs:.6f}")

# Residual statistics
residuals = y_true - y_pred
print(f"\nResidual Statistics:")
print(f"  Mean: {residuals.mean():.6f}")
print(f"  Std:  {residuals.std():.6f}")
print(f"  Min:  {residuals.min():.4f}")
print(f"  Max:  {residuals.max():.4f}")

print("\n4. EVALUATION SUMMARY")
print("-" * 50)

metrics = {
    'MAE': mae,
    'MSE': mse,
    'RMSE': rmse,
    'R2_Score': r2,
    'MAPE': mape,
    'Max_Error': max_error,
    'Median_AE': median_ae,
    'Explained_Variance': evs
}

print("MODEL PERFORMANCE METRICS:")
for name, value in metrics.items():
    print(f"  {name}: {value:.6f}")

# Performance interpretation
print("\n5. PERFORMANCE INTERPRETATION")
print("-" * 50)

if r2 >= 0.9:
    perf = "EXCELLENT"
elif r2 >= 0.7:
    perf = "GOOD"
elif r2 >= 0.5:
    perf = "MODERATE"
else:
    perf = "POOR"

print(f"R² = {r2:.4f} → Model Performance: {perf}")
print(f"The model explains {r2*100:.1f}% of the variance in student scores.")
print(f"Average prediction error (MAE): {mae:.2f} points")
print(f"Typical prediction error (RMSE): {rmse:.2f} points")

# Compare with training-time metrics
print("\n6. COMPARISON WITH TRAINING-TIME METRICS")
print("-" * 50)
print(f"Training-time Test R²:    {metadata['test_r2']:.6f}")
print(f"Current Evaluation R²:    {r2:.6f}")
print(f"Training-time Test RMSE:  {metadata['test_rmse']:.6f}")
print(f"Current Evaluation RMSE:  {rmse:.6f}")

diff_r2 = abs(metadata['test_r2'] - r2)
diff_rmse = abs(metadata['test_rmse'] - rmse)
print(f"\nDifference in R²:   {diff_r2:.6f}")
print(f"Difference in RMSE: {diff_rmse:.6f}")

if diff_r2 < 0.01 and diff_rmse < 0.1:
    print("✓ Metrics consistent with training evaluation")
else:
    print("⚠ Metrics differ from training - investigate!")

# Save metrics to JSON
metrics_output = {
    'model_type': metadata['model_type'],
    'features': features,
    'n_samples': int(len(df)),
    'metrics': {
        'MAE': float(mae),
        'MSE': float(mse),
        'RMSE': float(rmse),
        'R2_Score': float(r2),
        'MAPE': float(mape),
        'Max_Error': float(max_error),
        'Median_AE': float(median_ae),
        'Explained_Variance': float(evs)
    },
    'residual_stats': {
        'mean': float(residuals.mean()),
        'std': float(residuals.std()),
        'min': float(residuals.min()),
        'max': float(residuals.max())
    },
    'performance_rating': perf,
    'variance_explained_pct': float(r2 * 100)
}

with open('model_evaluation_metrics.json', 'w') as f:
    json.dump(metrics_output, f, indent=2)
print("\n✓ Metrics saved to: model_evaluation_metrics.json")

# ============================================================
# VISUALIZATIONS
# ============================================================
print("\n7. GENERATING EVALUATION VISUALIZATIONS")
print("-" * 50)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 1. Actual vs Predicted
ax = axes[0, 0]
ax.scatter(y_true, y_pred, alpha=0.5, color='steelblue', s=30, edgecolor='white')
min_val, max_val = y_true.min(), y_true.max()
ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
ax.set_xlabel('Actual Average Score')
ax.set_ylabel('Predicted Average Score')
ax.set_title(f'Actual vs Predicted\nR² = {r2:.4f}')
ax.legend()
ax.grid(True, alpha=0.3)

# 2. Residuals vs Predicted
ax = axes[0, 1]
ax.scatter(y_pred, residuals, alpha=0.5, color='orange', s=30, edgecolor='white')
ax.axhline(y=0, color='red', linestyle='--', lw=2)
ax.set_xlabel('Predicted Average Score')
ax.set_ylabel('Residuals')
ax.set_title('Residuals vs Predicted')
ax.grid(True, alpha=0.3)

# 3. Residual Distribution
ax = axes[0, 2]
ax.hist(residuals, bins=20, alpha=0.7, color='green', edgecolor='white', density=True)
from scipy.stats import norm
x = np.linspace(residuals.min(), residuals.max(), 100)
ax.plot(x, norm.pdf(x, residuals.mean(), residuals.std()), 'r-', lw=2, label='Normal Fit')
ax.set_xlabel('Residuals')
ax.set_ylabel('Density')
ax.set_title('Residual Distribution')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# 4. Q-Q Plot
ax = axes[1, 0]
from scipy.stats import probplot
probplot(residuals, dist="norm", plot=ax)
ax.set_title('Q-Q Plot (Residuals vs Normal)')
ax.grid(True, alpha=0.3)

# 5. Metrics Bar Chart
ax = axes[1, 1]
metric_names = ['MAE', 'MSE', 'RMSE', 'R²', 'MAPE', 'Max Err', 'Median AE', 'Exp Var']
metric_values = [mae, mse, rmse, r2, mape/100, max_error, median_ae, evs]
colors = ['steelblue']*3 + ['green'] + ['orange']*3 + ['purple']
bars = ax.bar(metric_names, metric_values, color=colors, edgecolor='white', alpha=0.8)
ax.set_ylabel('Value')
ax.set_title('Model Evaluation Metrics')
ax.tick_params(axis='x', rotation=45)
for bar, val in zip(bars, metric_values):
    ax.annotate(f'{val:.3f}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# 6. Error Distribution by Score Range
ax = axes[1, 2]
score_bins = pd.cut(y_true, bins=5)
df['score_bin'] = score_bins
df['residual'] = residuals
df['abs_error'] = np.abs(residuals)
bin_errors = df.groupby('score_bin')['abs_error'].mean()
bin_centers = [interval.mid for interval in bin_errors.index]
ax.bar(range(len(bin_errors)), bin_errors.values, color='coral', edgecolor='white', alpha=0.8)
ax.set_xticks(range(len(bin_errors)))
ax.set_xticklabels([f'{c:.0f}' for c in bin_centers])
ax.set_xlabel('Actual Score Range (center)')
ax.set_ylabel('Mean Absolute Error')
ax.set_title('Error by Score Range')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('plots/model_evaluation_detailed.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: plots/model_evaluation_detailed.png")

# Additional focused plot: Metrics comparison
plt.figure(figsize=(10, 6))
key_metrics = ['MAE', 'MSE', 'RMSE', 'R² Score']
key_values = [mae, mse, rmse, r2]
colors = ['steelblue', 'orange', 'green', 'red']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(key_metrics, key_values, color=colors, edgecolor='white', alpha=0.8, width=0.6)
ax.set_ylabel('Value')
ax.set_title('Key Model Evaluation Metrics', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

for bar, val in zip(bars, key_values):
    ax.annotate(f'{val:.4f}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', 
                fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('plots/key_metrics.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: plots/key_metrics.png")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("DAY 10 MODEL EVALUATION - COMPLETE")
print("=" * 70)

print(f"""
EVALUATION RESULTS:
✓ Model Type: {metadata['model_type']}
✓ Samples Evaluated: {len(df)}
✓ Features: {len(features)}

KEY METRICS:
  MAE:  {mae:.6f}
  MSE:  {mse:.6f}
  RMSE: {rmse:.6f}
  R²:   {r2:.6f}

PERFORMANCE RATING: {perf}
Variance Explained: {r2*100:.1f}%

INTERPRETATION:
- On average, predictions are off by {mae:.2f} points (MAE)
- Typical error magnitude is {rmse:.2f} points (RMSE)
- Model explains {r2*100:.1f}% of score variance
- Max prediction error: {max_error:.2f} points

FILES CREATED:
  - model_evaluation_metrics.json (detailed metrics)
  - plots/model_evaluation_detailed.png (6-panel evaluation)
  - plots/key_metrics.png (key metrics bar chart)

Task Status: COMPLETE ✓
Submission: Ready for Google Form
""")

print("=" * 70)