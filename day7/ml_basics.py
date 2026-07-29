#!/usr/bin/env python3
"""
Day 7 - Machine Learning Basics
Supervised Learning, Train-Test Split, and Linear Regression

Learning Objectives:
1. Understand supervised learning concepts
2. Perform train-test split
3. Implement Linear Regression (Simple & Multiple)
4. Evaluate model performance (MSE, RMSE, R²)
5. Visualize results
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Create plots directory
import os
os.makedirs('plots', exist_ok=True)

print("=" * 70)
print("DAY 7 - MACHINE LEARNING BASICS")
print("Supervised Learning, Train-Test Split & Linear Regression")
print("=" * 70)

# ============================================================
# 1. LOAD AND EXPLORE DATA
# ============================================================
print("\n" + "=" * 60)
print("1. LOADING AND EXPLORING DATA")
print("=" * 60)

# Load cleaned data from Day 5
df = pd.read_csv('../day5/student_scores_cleaned.csv')
print(f"Dataset shape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst 5 rows:")
print(df.head())

# Check data types and basic info
print(f"\nData types:")
print(df.dtypes)
print(f"\nBasic statistics:")
print(df.describe())

# ============================================================
# 2. SUPERVISED LEARNING CONCEPTS
# ============================================================
print("\n" + "=" * 60)
print("2. SUPERVISED LEARNING CONCEPTS")
print("=" * 60)

print("""
SUPERVISED LEARNING:
- Learning from labeled data (input features X, target labels y)
- Goal: Learn mapping function f: X -> y
- Two main types:
  1. REGRESSION: Predict continuous values (e.g., house prices, scores)
  2. CLASSIFICATION: Predict discrete categories (e.g., pass/fail, spam/not spam)

KEY CONCEPTS:
- Features (X): Input variables used for prediction
- Target (y): Variable we want to predict
- Training data: Used to train the model
- Test data: Used to evaluate model performance (unseen data)
- Overfitting: Model memorizes training data, fails on new data
- Underfitting: Model too simple, fails to capture patterns
- Bias-Variance Tradeoff: Balance between overfitting and underfitting
""")

# ============================================================
# 3. PREPARE DATA FOR REGRESSION
# ============================================================
print("\n" + "=" * 60)
print("3. PREPARING DATA FOR REGRESSION")
print("=" * 60)

# Define features and target for predicting 'avg_score' (average of all subject scores)
# We'll use multiple features to predict average score
feature_cols = ['math_score', 'physics_score', 'chemistry_score', 
                'english_score', 'cs_score', 'attendance_pct', 
                'study_hours_per_week', 'age']

# Create target variable: average of all subject scores
score_cols = ['math_score', 'physics_score', 'chemistry_score', 'english_score', 'cs_score']
df['avg_score'] = df[score_cols].mean(axis=1)

# We'll use multiple features to predict average score
X = df[feature_cols]
y = df['avg_score']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")
print(f"\nFeatures: {feature_cols}")
print(f"Target: avg_score")

# Check correlation with target
correlations = X.corrwith(y).sort_values(ascending=False)
print(f"\nCorrelation with target (avg_score):")
print(correlations)

# Visualize correlations
plt.figure(figsize=(10, 6))
correlations.plot(kind='barh', color='steelblue')
plt.xlabel('Correlation with avg_score')
plt.title('Feature Correlation with Target (avg_score)')
plt.tight_layout()
plt.savefig('plots/feature_correlation.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: feature_correlation.png")

# ============================================================
# 4. TRAIN-TEST SPLIT
# ============================================================
print("\n" + "=" * 60)
print("4. TRAIN-TEST SPLIT")
print("=" * 60)

print("""
TRAIN-TEST SPLIT:
- Split data into training set (to train model) and test set (to evaluate)
- Common splits: 80/20, 70/30, 90/10
- random_state ensures reproducibility
- stratify parameter for classification (maintains class distribution)
- shuffle=True (default) shuffles data before splitting
""")

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

print(f"Training set size: {X_train.shape[0]} samples ({X_train.shape[0]/len(X)*100:.0f}%)")
print(f"Test set size: {X_test.shape[0]} samples ({X_test.shape[0]/len(X)*100:.0f}%)")
print(f"\nTraining target stats:")
print(y_train.describe())
print(f"\nTest target stats:")
print(y_test.describe())

# Visualize train-test split
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(y_train, bins=20, alpha=0.7, label='Train', color='steelblue', edgecolor='white')
plt.hist(y_test, bins=20, alpha=0.7, label='Test', color='orange', edgecolor='white')
plt.xlabel('Average Score')
plt.ylabel('Frequency')
plt.title('Target Distribution: Train vs Test')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(range(len(y_train)), sorted(y_train), alpha=0.5, label='Train', color='steelblue', s=20)
plt.scatter(range(len(y_test)), sorted(y_test), alpha=0.5, label='Test', color='orange', s=20)
plt.xlabel('Sample Index (sorted)')
plt.ylabel('Average Score')
plt.title('Target Values: Train vs Test (sorted)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('plots/train_test_split.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: train_test_split.png")

# ============================================================
# 5. SIMPLE LINEAR REGRESSION (Single Feature)
# ============================================================
print("\n" + "=" * 60)
print("5. SIMPLE LINEAR REGRESSION (Single Feature)")
print("=" * 60)

print("""
SIMPLE LINEAR REGRESSION:
- One feature (X) to predict target (y)
- Model: y = β₀ + β₁X + ε
- β₀: intercept (y when X=0)
- β₁: slope (change in y per unit change in X)
- ε: error term (noise)
- Goal: Find β₀, β₁ that minimize MSE
""")

# Use 'study_hours_per_week' as single feature to predict 'avg_score'
X_simple = df[['study_hours_per_week']]
y_simple = df['avg_score']

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_simple, y_simple, test_size=0.2, random_state=42
)

# Train simple linear regression
lr_simple = LinearRegression()
lr_simple.fit(X_train_s, y_train_s)

# Predictions
y_pred_train_s = lr_simple.predict(X_train_s)
y_pred_test_s = lr_simple.predict(X_test_s)

# Coefficients
print(f"Simple Linear Regression Results:")
print(f"  Intercept (β₀): {lr_simple.intercept_:.4f}")
print(f"  Coefficient (β₁): {lr_simple.coef_[0]:.4f}")
print(f"  Equation: avg_score = {lr_simple.intercept_:.2f} + {lr_simple.coef_[0]:.2f} × study_hours")

# Evaluate
train_mse_s = mean_squared_error(y_train_s, y_pred_train_s)
test_mse_s = mean_squared_error(y_test_s, y_pred_test_s)
train_rmse_s = np.sqrt(train_mse_s)
test_rmse_s = np.sqrt(test_mse_s)
train_r2_s = r2_score(y_train_s, y_pred_train_s)
test_r2_s = r2_score(y_test_s, y_pred_test_s)

print(f"\n  Training Metrics:")
print(f"    MSE: {train_mse_s:.4f}")
print(f"    RMSE: {train_rmse_s:.4f}")
print(f"    R²: {train_r2_s:.4f}")
print(f"\n  Test Metrics:")
print(f"    MSE: {test_mse_s:.4f}")
print(f"    RMSE: {test_rmse_s:.4f}")
print(f"    R²: {test_r2_s:.4f}")

# Visualize simple linear regression
plt.figure(figsize=(12, 5))

# Plot 1: Regression line on training data
plt.subplot(1, 2, 1)
plt.scatter(X_train_s, y_train_s, alpha=0.6, label='Train data', color='steelblue', edgecolor='white')
plt.scatter(X_test_s, y_test_s, alpha=0.6, label='Test data', color='orange', edgecolor='white')
# Plot regression line
x_line = np.linspace(X_simple.min(), X_simple.max(), 100).reshape(-1, 1)
y_line = lr_simple.predict(x_line)
plt.plot(x_line, y_line, 'r-', linewidth=2, label=f'Regression line (R²={test_r2_s:.3f})')
plt.xlabel('Study Hours per Week')
plt.ylabel('Average Score')
plt.title('Simple Linear Regression: Study Hours vs Avg Score')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Predicted vs Actual
plt.subplot(1, 2, 2)
plt.scatter(y_test_s, y_pred_test_s, alpha=0.6, color='green', edgecolor='white')
plt.plot([y_test_s.min(), y_test_s.max()], [y_test_s.min(), y_test_s.max()], 'r--', lw=2, label='Perfect prediction')
plt.xlabel('Actual Average Score')
plt.ylabel('Predicted Average Score')
plt.title('Predicted vs Actual (Test Set)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('plots/simple_linear_regression.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: simple_linear_regression.png")

# Residual plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
residuals_train = y_train_s - y_pred_train_s
residuals_test = y_test_s - y_pred_test_s
plt.scatter(y_pred_train_s, residuals_train, alpha=0.5, label='Train', color='steelblue')
plt.scatter(y_pred_test_s, residuals_test, alpha=0.5, label='Test', color='orange')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
# Q-Q plot for residuals
from scipy import stats
stats.probplot(residuals_test, dist="norm", plot=plt)
plt.title('Q-Q Plot of Test Residuals')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('plots/simple_lr_residuals.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: simple_lr_residuals.png")

# ============================================================
# 6. MULTIPLE LINEAR REGRESSION (Multiple Features)
# ============================================================
print("\n" + "=" * 60)
print("6. MULTIPLE LINEAR REGRESSION (Multiple Features)")
print("=" * 60)

print("""
MULTIPLE LINEAR REGRESSION:
- Multiple features (X₁, X₂, ..., Xₙ) to predict target (y)
- Model: y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε
- Each βᵢ represents the effect of Xᵢ on y, holding other features constant
- Assumptions: Linearity, Independence, Homoscedasticity, Normality of residuals
""")

# Train multiple linear regression
lr_multi = LinearRegression()
lr_multi.fit(X_train, y_train)

# Predictions
y_pred_train_m = lr_multi.predict(X_train)
y_pred_test_m = lr_multi.predict(X_test)

# Coefficients
coef_df = pd.DataFrame({
    'Feature': feature_cols,
    'Coefficient': lr_multi.coef_
}).sort_values('Coefficient', key=abs, ascending=False)

print(f"Multiple Linear Regression Coefficients:")
print(coef_df.to_string(index=False))
print(f"\nIntercept: {lr_multi.intercept_:.4f}")

# Equation
eq_terms = [f"{coef:.3f}×{feat}" for feat, coef in zip(feature_cols, lr_multi.coef_)]
equation = f"avg_score = {lr_multi.intercept_:.3f} + " + " + ".join(eq_terms)
print(f"\nEquation: {equation}")

# Evaluate
train_mse_m = mean_squared_error(y_train, y_pred_train_m)
test_mse_m = mean_squared_error(y_test, y_pred_test_m)
train_rmse_m = np.sqrt(train_mse_m)
test_rmse_m = np.sqrt(test_mse_m)
train_mae_m = mean_absolute_error(y_train, y_pred_train_m)
test_mae_m = mean_absolute_error(y_test, y_pred_test_m)
train_r2_m = r2_score(y_train, y_pred_train_m)
test_r2_m = r2_score(y_test, y_pred_test_m)

print(f"\n  Training Metrics:")
print(f"    MSE: {train_mse_m:.4f}")
print(f"    RMSE: {train_rmse_m:.4f}")
print(f"    MAE: {train_mae_m:.4f}")
print(f"    R²: {train_r2_m:.4f}")
print(f"\n  Test Metrics:")
print(f"    MSE: {test_mse_m:.4f}")
print(f"    RMSE: {test_rmse_m:.4f}")
print(f"    MAE: {test_mae_m:.4f}")
print(f"    R²: {test_r2_m:.4f}")

# ============================================================
# 7. MODEL EVALUATION METRICS EXPLAINED
# ============================================================
print("\n" + "=" * 60)
print("7. MODEL EVALUATION METRICS EXPLAINED")
print("=" * 60)

improvement = test_r2_m - test_r2_s
print(f"""
REGRESSION METRICS:

1. MEAN SQUARED ERROR (MSE):
   - Average of squared differences between predicted and actual
   - Penalizes large errors heavily (quadratic)
   - Unit: squared target unit
   - Lower is better

2. ROOT MEAN SQUARED ERROR (RMSE):
   - Square root of MSE
   - Same unit as target variable
   - Interpretable as "typical prediction error"
   - Lower is better

3. MEAN ABSOLUTE ERROR (MAE):
   - Average of absolute differences
   - Linear penalty (less sensitive to outliers than MSE)
   - Same unit as target
   - Lower is better

4. R² (COEFFICIENT OF DETERMINATION):
   - Proportion of variance in target explained by model
   - Range: 0 to 1 (can be negative for very bad models)
   - 1 = perfect fit, 0 = model predicts mean
   - Higher is better
   - R² = 1 - (SS_res / SS_tot)

COMPARISON:
- Simple LR R² (test): {test_r2_s:.4f}
- Multiple LR R² (test): {test_r2_m:.4f}
- Improvement: {improvement:+.4f}
""")

# ============================================================
# 8. VISUALIZE MULTIPLE LINEAR REGRESSION RESULTS
# ============================================================
print("\n" + "=" * 60)
print("8. VISUALIZING MULTIPLE LINEAR REGRESSION RESULTS")
print("=" * 60)

# Predicted vs Actual
plt.figure(figsize=(14, 10))

# 1. Predicted vs Actual (Test)
plt.subplot(2, 3, 1)
plt.scatter(y_test, y_pred_test_m, alpha=0.6, color='steelblue', edgecolor='white')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Average Score')
plt.ylabel('Predicted Average Score')
plt.title(f'Predicted vs Actual (Test)\nR² = {test_r2_m:.4f}')
plt.grid(True, alpha=0.3)

# 2. Residuals vs Predicted
plt.subplot(2, 3, 2)
residuals_test = y_test - y_pred_test_m
plt.scatter(y_pred_test_m, residuals_test, alpha=0.6, color='orange', edgecolor='white')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted (Test)')
plt.grid(True, alpha=0.3)

# 3. Residual Distribution
plt.subplot(2, 3, 3)
plt.hist(residuals_test, bins=20, alpha=0.7, color='green', edgecolor='white', density=True)
# Overlay normal distribution
from scipy.stats import norm
x = np.linspace(residuals_test.min(), residuals_test.max(), 100)
plt.plot(x, norm.pdf(x, residuals_test.mean(), residuals_test.std()), 'r-', lw=2, label='Normal fit')
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.title('Residual Distribution (Test)')
plt.legend()
plt.grid(True, alpha=0.3)

# 4. Feature Coefficients
plt.subplot(2, 3, 4)
coef_df_sorted = coef_df.sort_values('Coefficient', ascending=True)
colors = ['red' if c < 0 else 'blue' for c in coef_df_sorted['Coefficient']]
plt.barh(coef_df_sorted['Feature'], coef_df_sorted['Coefficient'], color=colors, edgecolor='white')
plt.xlabel('Coefficient Value')
plt.title('Feature Coefficients (Multiple LR)')
plt.grid(True, alpha=0.3, axis='x')

# 5. Actual vs Predicted over samples
plt.subplot(2, 3, 5)
sample_indices = range(min(50, len(y_test)))
plt.plot(sample_indices, y_test.iloc[sample_indices].values, 'o-', label='Actual', color='steelblue', markersize=4)
plt.plot(sample_indices, y_pred_test_m[sample_indices], 's-', label='Predicted', color='orange', markersize=4)
plt.xlabel('Sample Index')
plt.ylabel('Average Score')
plt.title('Actual vs Predicted (First 50 Test Samples)')
plt.legend()
plt.grid(True, alpha=0.3)

# 6. Training vs Test R² comparison
plt.subplot(2, 3, 6)
models = ['Simple LR', 'Multiple LR']
train_r2 = [train_r2_s, train_r2_m]
test_r2 = [test_r2_s, test_r2_m]
x_pos = np.arange(len(models))
width = 0.35
plt.bar(x_pos - width/2, train_r2, width, label='Train R²', color='steelblue', edgecolor='white')
plt.bar(x_pos + width/2, test_r2, width, label='Test R²', color='orange', edgecolor='white')
plt.xlabel('Model')
plt.ylabel('R² Score')
plt.title('Train vs Test R² Comparison')
plt.xticks(x_pos, models)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.ylim(0, 1.1)

plt.tight_layout()
plt.savefig('plots/multiple_lr_results.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: multiple_lr_results.png")

# ============================================================
# 9. FEATURE SCALING AND STANDARDIZED COEFFICIENTS
# ============================================================
print("\n" + "=" * 60)
print("9. FEATURE SCALING AND STANDARDIZED COEFFICIENTS")
print("=" * 60)

print("""
FEATURE SCALING:
- Standardize features to have zero mean and unit variance
- Important when features have different scales
- Allows comparison of coefficient magnitudes
- StandardScaler: (X - mean) / std
""")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train on scaled features
lr_scaled = LinearRegression()
lr_scaled.fit(X_train_scaled, y_train)

# Get standardized coefficients
scaled_coef_df = pd.DataFrame({
    'Feature': feature_cols,
    'Standardized_Coefficient': lr_scaled.coef_
}).sort_values('Standardized_Coefficient', key=abs, ascending=False)

print("Standardized Coefficients (feature importance):")
print(scaled_coef_df.to_string(index=False))

# Visualize standardized coefficients
plt.figure(figsize=(10, 6))
colors = ['red' if c < 0 else 'blue' for c in scaled_coef_df['Standardized_Coefficient']]
plt.barh(scaled_coef_df['Feature'], scaled_coef_df['Standardized_Coefficient'], color=colors, edgecolor='white')
plt.xlabel('Standardized Coefficient (Feature Importance)')
plt.title('Feature Importance (Standardized Coefficients)')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('plots/standardized_coefficients.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: standardized_coefficients.png")

# ============================================================
# 10. PREDICTION ON NEW DATA
# ============================================================
print("\n" + "=" * 60)
print("10. MAKING PREDICTIONS ON NEW DATA")
print("=" * 60)

# Create sample new student data
new_student = pd.DataFrame({
    'math_score': [85],
    'physics_score': [80],
    'chemistry_score': [78],
    'english_score': [75],
    'cs_score': [82],
    'attendance_pct': [90],
    'study_hours_per_week': [15],
    'age': [20]
})

print("New student data:")
print(new_student)

# Predict using multiple linear regression
predicted_avg = lr_multi.predict(new_student)[0]
print(f"\nPredicted average score: {predicted_avg:.2f}")

# Also predict using scaled model
new_student_scaled = scaler.transform(new_student)
predicted_avg_scaled = lr_scaled.predict(new_student_scaled)[0]
print(f"Predicted average score (scaled model): {predicted_avg_scaled:.2f}")

# ============================================================
# 11. CROSS-VALIDATION (BONUS)
# ============================================================
print("\n" + "=" * 60)
print("11. CROSS-VALIDATION (BONUS)")
print("=" * 60)

print("""
CROSS-VALIDATION:
- Technique to assess model generalizability
- k-fold CV: Split data into k folds, train on k-1, test on 1, repeat k times
- Average performance across all folds
- Reduces variance of performance estimate
""")

from sklearn.model_selection import cross_val_score, KFold

# 5-fold cross-validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(lr_multi, X, y, cv=cv, scoring='r2')
cv_mse_scores = cross_val_score(lr_multi, X, y, cv=cv, scoring='neg_mean_squared_error')

print(f"5-Fold Cross-Validation R² Scores: {cv_scores}")
print(f"Mean R²: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
print(f"Mean MSE: {-cv_mse_scores.mean():.4f} (+/- {cv_mse_scores.std()*2:.4f})")

# Visualize CV scores
plt.figure(figsize=(8, 5))
plt.bar(range(1, 6), cv_scores, color='steelblue', edgecolor='white')
plt.axhline(y=cv_scores.mean(), color='red', linestyle='--', label=f'Mean: {cv_scores.mean():.4f}')
plt.xlabel('Fold')
plt.ylabel('R² Score')
plt.title('5-Fold Cross-Validation R² Scores')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/cross_validation.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: cross_validation.png")

# ============================================================
# 12. SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY - DAY 7 MACHINE LEARNING BASICS COMPLETED!")
print("=" * 70)

print(f"""
KEY CONCEPTS LEARNED:
✓ Supervised Learning: Regression vs Classification
✓ Train-Test Split: 80/20 split with random_state=42
✓ Simple Linear Regression: One feature (study_hours -> avg_score)
  - R² (test): {test_r2_s:.4f}
  - Equation: avg_score = {lr_simple.intercept_:.2f} + {lr_simple.coef_[0]:.2f} × study_hours
✓ Multiple Linear Regression: 8 features -> avg_score
  - R² (test): {test_r2_m:.4f}
  - Improvement over simple LR: {improvement:+.4f}
✓ Evaluation Metrics: MSE, RMSE, MAE, R²
✓ Residual Analysis: Check model assumptions
✓ Feature Scaling: StandardScaler for fair coefficient comparison
✓ Cross-Validation: 5-fold CV mean R² = {cv_scores.mean():.4f}
✓ Making Predictions: New student avg_score = {predicted_avg:.2f}

PLOTS CREATED:
""")

plot_files = sorted(os.listdir('plots'))
for f in plot_files:
    print(f"  - {f}")

print(f"\nTotal plots: {len(plot_files)}")
print("\nAll code saved in: day7/ml_basics.py")
print("=" * 70)