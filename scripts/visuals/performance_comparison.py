# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_path = "/Users/seanryan/Documents/MLB_Project/data/processed/hitting/hitting_clustered_refined.csv"
hitting_data = pd.read_csv(data_path)

# Add a column to identify Diamondbacks players
hitting_data['Is_Diamondback'] = hitting_data['Team'].apply(lambda x: 'Diamondbacks' if x == 'ARI' else 'Other')

# Set up the plot style
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

# Define color palette for Hitter_Type
hitter_type_palette = {
    'Balanced Hitter': '#1f77b4',  # Blue
    'Contact Hitter': '#ff7f0e',   # Orange
    'Power Hitter': '#2ca02c'      # Green
}

# Create the main scatter plot with updated colors
sns.scatterplot(data=hitting_data[hitting_data['Is_Diamondback'] == 'Other'], 
                x='SLG', y='OPS', hue='Hitter_Type', palette=hitter_type_palette, s=80, alpha=0.8)

# Highlight Diamondbacks players with a distinct style
sns.scatterplot(data=hitting_data[hitting_data['Is_Diamondback'] == 'Diamondbacks'], 
                x='SLG', y='OPS', color='red', edgecolor='black', s=120, label='Diamondbacks')

# Optional: Add reference lines for league average (assuming typical values, adjust as necessary)
plt.axhline(y=0.750, color='gray', linestyle='--', linewidth=1, label='Avg OPS (0.750)')
plt.axvline(x=0.400, color='gray', linestyle='--', linewidth=1, label='Avg SLG (0.400)')

# Add custom legend for Diamondbacks
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Diamondbacks'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4', markersize=8, label='Balanced Hitter'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff7f0e', markersize=8, label='Contact Hitter'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#2ca02c', markersize=8, label='Power Hitter'),
    Line2D([0], [0], color='gray', linestyle='--', linewidth=1, label='Avg OPS (0.750)'),
    Line2D([0], [0], color='gray', linestyle='--', linewidth=1, label='Avg SLG (0.400)')
]
plt.legend(handles=legend_elements, loc="upper left", title="Legend", fontsize=10)

# Add titles and labels
plt.title("Performance Comparison: SLG vs OPS by Hitter Type with Diamondbacks Highlighted", fontsize=14)
plt.xlabel("SLG (Slugging Percentage)", fontsize=12)
plt.ylabel("OPS (On-base Plus Slugging)", fontsize=12)

# Save the plot
output_path = "/Users/seanryan/Documents/MLB_Project/figures/visuals/performance_comparison_refined.png"
plt.savefig(output_path, bbox_inches='tight')

# Show the plot
plt.show()