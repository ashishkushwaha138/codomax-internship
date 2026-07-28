"""
Day 6 - Data Visualization Tasks
Create scatter plots, bar charts and line charts using Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style for better looking plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Create output directory for plots
os.makedirs('plots', exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv('../day5/student_scores_cleaned.csv')

print("=" * 60)
print("DAY 6 - DATA VISUALIZATION TASKS")
print("=" * 60)
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print()

# ============================================================
# TASK 1: SCATTER PLOTS
# ============================================================
print("=" * 60)
print("TASK 1: SCATTER PLOTS")
print("=" * 60)

# 1.1 Scatter plot: Math Score vs Physics Score colored by Placement
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['math_score'], df['physics_score'], 
                      c=df['placement_status'].map({'Placed': 1, 'Not Placed': 0}),
                      cmap='RdYlGn', alpha=0.7, s=80, edgecolors='white', linewidth=0.5)
plt.colorbar(scatter, label='Placement Status (Green=Placed)')
plt.xlabel('Math Score', fontsize=12)
plt.ylabel('Physics Score', fontsize=12)
plt.title('Scatter Plot: Math Score vs Physics Score\nColored by Placement Status', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/scatter_math_vs_physics_placement.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: scatter_math_vs_physics_placement.png")

# 1.2 Scatter plot: Study Hours vs Attendance colored by Department
plt.figure(figsize=(12, 7))
departments = df['department'].unique()
colors = plt.cm.tab10(np.linspace(0, 1, len(departments)))

for i, dept in enumerate(departments):
    subset = df[df['department'] == dept]
    plt.scatter(subset['study_hours_per_week'], subset['attendance_pct'], 
                label=dept, color=colors[i], alpha=0.7, s=80, edgecolors='white', linewidth=0.5)

plt.xlabel('Study Hours per Week', fontsize=12)
plt.ylabel('Attendance Percentage', fontsize=12)
plt.title('Scatter Plot: Study Hours vs Attendance by Department', fontsize=14, fontweight='bold')
plt.legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/scatter_study_vs_attendance_dept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: scatter_study_vs_attendance_dept.png")

# 1.3 Scatter plot: Math Score vs CS Score with trend line
plt.figure(figsize=(10, 6))
plt.scatter(df['math_score'], df['cs_score'], alpha=0.6, s=80, c='steelblue', edgecolors='white', linewidth=0.5)

# Add trend line
z = np.polyfit(df['math_score'], df['cs_score'], 1)
p = np.poly1d(z)
x_trend = np.linspace(df['math_score'].min(), df['math_score'].max(), 100)
plt.plot(x_trend, p(x_trend), "r--", linewidth=2, label=f'Trend Line (slope={z[0]:.2f})')

# Calculate correlation
corr = df['math_score'].corr(df['cs_score'])
plt.xlabel('Math Score', fontsize=12)
plt.ylabel('CS Score', fontsize=12)
plt.title(f'Scatter Plot: Math Score vs CS Score\nCorrelation: {corr:.3f}', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/scatter_math_vs_cs_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: scatter_math_vs_cs_trend.png")

# 1.4 Scatter plot with size encoding: Math vs Physics, size = Study Hours
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['math_score'], df['physics_score'], 
                      s=df['study_hours_per_week'] * 5,  # Size based on study hours
                      c=df['attendance_pct'], cmap='viridis', alpha=0.7, edgecolors='white', linewidth=0.5)
plt.colorbar(scatter, label='Attendance %')
plt.xlabel('Math Score', fontsize=12)
plt.ylabel('Physics Score', fontsize=12)
plt.title('Scatter Plot: Math vs Physics\nSize = Study Hours/Week, Color = Attendance %', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/scatter_math_physics_size_color.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: scatter_math_physics_size_color.png")


# ============================================================
# TASK 2: BAR CHARTS
# ============================================================
print("\n" + "=" * 60)
print("TASK 2: BAR CHARTS")
print("=" * 60)

# 2.1 Bar chart: Average scores by Department
plt.figure(figsize=(12, 7))
score_cols = ['math_score', 'physics_score', 'chemistry_score', 'english_score', 'cs_score']
dept_avg = df.groupby('department')[score_cols].mean()

x = np.arange(len(dept_avg.index))
width = 0.15
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

for i, (col, color) in enumerate(zip(score_cols, colors)):
    plt.bar(x + i * width, dept_avg[col], width, label=col.replace('_', ' ').title(), color=color, edgecolor='white', linewidth=0.5)

plt.xlabel('Department', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.title('Average Scores by Department', fontsize=14, fontweight='bold')
plt.xticks(x + width * 2, dept_avg.index, rotation=45, ha='right')
plt.legend(title='Subject', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/bar_avg_scores_by_dept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: bar_avg_scores_by_dept.png")

# 2.2 Bar chart: Placement Count by Department
plt.figure(figsize=(10, 6))
placement_dept = df.groupby(['department', 'placement_status']).size().unstack(fill_value=0)
placement_dept.plot(kind='bar', stacked=True, color=['#FF6B6B', '#4ECDC4'], edgecolor='white', linewidth=0.5)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.title('Placement Status by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Placement Status')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/bar_placement_by_dept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: bar_placement_by_dept.png")

# 2.3 Bar chart: Average scores by Gender
plt.figure(figsize=(10, 6))
gender_avg = df.groupby('gender')[score_cols].mean()
gender_avg.plot(kind='bar', color=colors, edgecolor='white', linewidth=0.5)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.title('Average Scores by Gender', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title='Subject', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/bar_avg_scores_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: bar_avg_scores_by_gender.png")

# 2.4 Bar chart: Extracurricular vs Average Math Score
plt.figure(figsize=(10, 6))
extra_avg = df.groupby('extracurricular')['math_score'].mean().sort_values(ascending=False)
bars = plt.bar(extra_avg.index, extra_avg.values, color='#4ECDC4', edgecolor='white', linewidth=0.5)
plt.xlabel('Extracurricular Activity', fontsize=12)
plt.ylabel('Average Math Score', fontsize=12)
plt.title('Average Math Score by Extracurricular Activity', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height:.1f}', ha='center', va='bottom', fontweight='bold')

plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/bar_math_by_extracurricular.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: bar_math_by_extracurricular.png")

# 2.5 Horizontal Bar chart: Average Attendance by Department
plt.figure(figsize=(10, 6))
attendance_dept = df.groupby('department')['attendance_pct'].mean().sort_values(ascending=True)
bars = plt.barh(attendance_dept.index, attendance_dept.values, color='#45B7D1', edgecolor='white', linewidth=0.5)
plt.xlabel('Average Attendance %', fontsize=12)
plt.ylabel('Department', fontsize=12)
plt.title('Average Attendance Percentage by Department', fontsize=14, fontweight='bold')

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2., 
             f'{width:.1f}%', ha='left', va='center', fontweight='bold')

plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('plots/barh_attendance_by_dept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: barh_attendance_by_dept.png")


# ============================================================
# TASK 3: LINE CHARTS
# ============================================================
print("\n" + "=" * 60)
print("TASK 3: LINE CHARTS")
print("=" * 60)

# 3.1 Line chart: Average scores across subjects (line plot for each department)
plt.figure(figsize=(12, 7))
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS']
x_pos = np.arange(len(subjects))

for dept in df['department'].unique():
    dept_data = df[df['department'] == dept]
    scores = [dept_data[col].mean() for col in score_cols]
    plt.plot(x_pos, scores, marker='o', linewidth=2.5, markersize=8, label=dept)

plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.title('Average Scores Across Subjects by Department', fontsize=14, fontweight='bold')
plt.xticks(x_pos, subjects)
plt.legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/line_avg_scores_by_dept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: line_avg_scores_by_dept.png")

# 3.2 Line chart: Placement rate by Age
plt.figure(figsize=(10, 6))
age_placement = df.groupby('age')['placement_status'].apply(lambda x: (x == 'Placed').mean() * 100)
plt.plot(age_placement.index, age_placement.values, marker='o', linewidth=2.5, markersize=10, color='#FF6B6B')
plt.xlabel('Age', fontsize=12)
plt.ylabel('Placement Rate (%)', fontsize=12)
plt.title('Placement Rate by Age', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/line_placement_rate_by_age.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: line_placement_rate_by_age.png")

# 3.3 Line chart: Study Hours vs Average Score Trend
plt.figure(figsize=(10, 6))
# Bin study hours
df['study_hours_bin'] = pd.cut(df['study_hours_per_week'], bins=5)
study_bin_scores = df.groupby('study_hours_bin', observed=False)[score_cols].mean()
study_bin_scores.index = [f"{interval.left:.0f}-{interval.right:.0f}" for interval in study_bin_scores.index]

for i, col in enumerate(score_cols):
    plt.plot(range(len(study_bin_scores)), study_bin_scores[col], marker='o', 
             linewidth=2, markersize=6, label=col.replace('_', ' ').title(), color=colors[i])

plt.xlabel('Study Hours per Week (Binned)', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.title('Average Scores by Study Hours Bins', fontsize=14, fontweight='bold')
plt.xticks(range(len(study_bin_scores)), study_bin_scores.index, rotation=45)
plt.legend(title='Subject', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/line_scores_by_study_hours.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: line_scores_by_study_hours.png")

# 3.4 Line chart with multiple lines: Attendance trend by Placement
plt.figure(figsize=(10, 6))
# Create attendance bins
df['attendance_bin'] = pd.cut(df['attendance_pct'], bins=5)
attendance_placement = df.groupby(['attendance_bin', 'placement_status'], observed=False).size().unstack(fill_value=0)
attendance_placement_pct = attendance_placement.div(attendance_placement.sum(axis=1), axis=0) * 100

for col in attendance_placement_pct.columns:
    plt.plot(range(len(attendance_placement_pct)), attendance_placement_pct[col], 
             marker='o', linewidth=2.5, markersize=8, label=col)

plt.xlabel('Attendance Percentage (Binned)', fontsize=12)
plt.ylabel('Percentage of Students', fontsize=12)
plt.title('Placement Rate by Attendance Bins', fontsize=14, fontweight='bold')
plt.xticks(range(len(attendance_placement_pct)), 
           [f"{interval.left:.0f}%-{interval.right:.0f}%" for interval in attendance_placement_pct.index], rotation=45)
plt.legend(title='Placement Status')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/line_placement_by_attendance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: line_placement_by_attendance.png")

# 3.5 Multi-line chart: Score progression (avg of all scores) by age for each gender
plt.figure(figsize=(10, 6))
df['avg_score'] = df[score_cols].mean(axis=1)
age_gender_scores = df.groupby(['age', 'gender'])['avg_score'].mean().unstack()

for gender in age_gender_scores.columns:
    plt.plot(age_gender_scores.index, age_gender_scores[gender], 
             marker='o', linewidth=2.5, markersize=8, label=gender)

plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Score (All Subjects)', fontsize=12)
plt.title('Average Score by Age and Gender', fontsize=14, fontweight='bold')
plt.legend(title='Gender')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/line_avg_score_by_age_gender.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: line_avg_score_by_age_gender.png")


# ============================================================
# TASK 4: COMBINATION PLOTS (BONUS)
# ============================================================
print("\n" + "=" * 60)
print("TASK 4: COMBINATION PLOTS (BONUS)")
print("=" * 60)

# 4.1 Subplots: 2x2 grid of different chart types
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: Scatter
axes[0, 0].scatter(df['math_score'], df['physics_score'], alpha=0.6, c='steelblue', edgecolors='white')
axes[0, 0].set_xlabel('Math Score')
axes[0, 0].set_ylabel('Physics Score')
axes[0, 0].set_title('Scatter: Math vs Physics')
axes[0, 0].grid(True, alpha=0.3)

# Top-right: Bar
dept_placement = df.groupby('department')['placement_status'].apply(lambda x: (x == 'Placed').mean() * 100)
axes[0, 1].bar(dept_placement.index, dept_placement.values, color='#4ECDC4', edgecolor='white')
axes[0, 1].set_xlabel('Department')
axes[0, 1].set_ylabel('Placement Rate %')
axes[0, 1].set_title('Bar: Placement Rate by Dept')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Bottom-left: Line
age_avg = df.groupby('age')['avg_score'].mean()
axes[1, 0].plot(age_avg.index, age_avg.values, marker='o', linewidth=2, color='#FF6B6B')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Avg Score')
axes[1, 0].set_title('Line: Avg Score by Age')
axes[1, 0].grid(True, alpha=0.3)

# Bottom-right: Horizontal Bar
gender_scores = df.groupby('gender')['avg_score'].mean().sort_values()
axes[1, 1].barh(gender_scores.index, gender_scores.values, color='#45B7D1', edgecolor='white')
axes[1, 1].set_xlabel('Avg Score')
axes[1, 1].set_title('Horizontal Bar: Avg Score by Gender')
axes[1, 1].grid(True, alpha=0.3, axis='x')

plt.suptitle('Day 6 - Data Visualization Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('plots/dashboard_combined.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: dashboard_combined.png")

# 4.2 Pair plot using seaborn (scatter matrix)
plt.figure(figsize=(12, 10))
score_df = df[score_cols + ['placement_status']]
sns.pairplot(score_df, hue='placement_status', palette={'Placed': '#4ECDC4', 'Not Placed': '#FF6B6B'}, 
             diag_kind='hist', plot_kws={'alpha': 0.6, 's': 50})
plt.suptitle('Pair Plot: Subject Scores by Placement Status', y=1.02, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('plots/pairplot_scores_placement.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: pairplot_scores_placement.png")

# 4.3 Heatmap: Correlation matrix
plt.figure(figsize=(10, 8))
corr_matrix = df[score_cols + ['attendance_pct', 'study_hours_per_week', 'age']].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdYlBu_r', 
            center=0, square=True, linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.title('Correlation Heatmap: Scores, Attendance, Study Hours, Age', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('plots/heatmap_correlation.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: heatmap_correlation.png")

# 4.4 Box plots: Scores by Placement Status
plt.figure(figsize=(12, 7))
df_melted = df.melt(id_vars=['placement_status'], value_vars=score_cols, 
                    var_name='Subject', value_name='Score')
sns.boxplot(data=df_melted, x='Subject', y='Score', hue='placement_status', 
            palette={'Placed': '#4ECDC4', 'Not Placed': '#FF6B6B'})
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.title('Score Distribution by Placement Status', fontsize=14, fontweight='bold')
plt.legend(title='Placement Status')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/boxplot_scores_by_placement.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: boxplot_scores_by_placement.png")

# 4.5 Violin plot: Study hours by Department
plt.figure(figsize=(12, 7))
sns.violinplot(data=df, x='department', y='study_hours_per_week', inner='box', palette='husl')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Study Hours per Week', fontsize=12)
plt.title('Study Hours Distribution by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('plots/violin_study_hours_by_dept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: violin_study_hours_by_dept.png")

print("\n" + "=" * 60)
print("ALL VISUALIZATION TASKS COMPLETED!")
print("=" * 60)
print(f"Total plots saved: {len(os.listdir('plots'))}")
print("Plots saved in: day6/plots/")
print("\nFiles created:")
for f in sorted(os.listdir('plots')):
    print(f"  - {f}")