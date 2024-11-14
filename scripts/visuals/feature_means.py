import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the clustered dataset
data_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting/hitting_clustered_refined.csv'
df = pd.read_csv(data_path)

# Select the features to compare
features = ['BA', 'OBP', 'SLG', 'ISO', 'BB%', 'SO%']

# Calculate the mean of each feature grouped by Hitter_Type
feature_means = df.groupby('Hitter_Type')[features].mean()

# Setup figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Set up bar width and colors
bar_width = 0.12
colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e', '#8c564b']
x = np.arange(len(feature_means.index))  # the label locations for each hitter type

# Plot each metric
for i, feature in enumerate(features):
    ax.bar(x + i * bar_width, feature_means[feature], bar_width, label=feature, color=colors[i])

# Add labels on each bar
for i, feature in enumerate(features):
    for j, value in enumerate(feature_means[feature]):
        ax.text(j + i * bar_width, value + 0.01, f"{value:.2f}", ha='center', va='bottom', fontsize=8)

# Set labels and title
ax.set_xlabel("Hitter Type", fontsize=12)
ax.set_ylabel("Average Metric Value", fontsize=12)
ax.set_title("Average Hitting Metrics by Hitter Type (with Key Metrics)", fontsize=16)
ax.set_xticks(x + bar_width * (len(features) - 1) / 2)
ax.set_xticklabels(feature_means.index, fontsize=12)

# Add legend below the plot
ax.legend(title="Metrics", loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=10)

# Add light gridlines for better readability
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Save the refined plot
output_path = '/Users/seanryan/Documents/MLB_Project/figures/visuals/hitter_type_feature_means_final.png'
plt.tight_layout()
plt.savefig(output_path, bbox_inches='tight', dpi=300)
plt.show()