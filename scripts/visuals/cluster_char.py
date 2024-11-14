import pandas as pd

# Load the clustered dataset
data_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting/hitting_clustered_refined.csv'
df = pd.read_csv(data_path)

# Select the features to summarize
features = ['BA', 'OBP', 'SLG', 'ISO', 'BB%', 'SO%']

# Calculate the mean of each feature grouped by Hitter_Type
feature_means = df.groupby('Hitter_Type')[features].mean().round(3)

# Display the summary table
print("Cluster Characteristics Summary Table:")
print(feature_means)

# Save the summary table as a CSV for reference
table_output_path = '/Users/seanryan/Documents/MLB_Project/figures/visuals/cluster_characteristics_summary.csv'
feature_means.to_csv(table_output_path)
print(f"Summary table saved to {table_output_path}")

# (Optional) Save the summary table as an image using matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))  # Adjust size as needed
ax.axis('off')  # Hide axes

# Render the table
table = ax.table(cellText=feature_means.values, 
                 colLabels=feature_means.columns,
                 rowLabels=feature_means.index,
                 cellLoc='center', 
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # Adjust scaling for readability

# Save the table as an image
image_output_path = '/Users/seanryan/Documents/MLB_Project/figures/visuals/cluster_characteristics_summary.png'
plt.savefig(image_output_path, bbox_inches='tight', dpi=300)
plt.show()

print(f"Cluster characteristics summary table image saved to {image_output_path}")