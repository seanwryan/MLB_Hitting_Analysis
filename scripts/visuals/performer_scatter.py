# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_path = "/Users/seanryan/Documents/MLB_Project/data/processed/hitting/hitting_clustered_refined.csv"
hitting_data = pd.read_csv(data_path)

# Filter for Diamondbacks players only
dbacks_data = hitting_data[hitting_data['Team'] == 'ARI']

# Set up the plot style
plt.figure(figsize=(10, 8))
sns.set_style("whitegrid")

# Calculate the team average OBP and SLG to highlight top performers
avg_obp = dbacks_data['OBP'].mean()
avg_slg = dbacks_data['SLG'].mean()

# Scatter plot of OBP vs SLG
scatter = sns.scatterplot(data=dbacks_data, x='OBP', y='SLG', s=100, color='gray', edgecolor='black')

# Highlight top performers with high OBP and SLG
top_performers = dbacks_data[(dbacks_data['OBP'] > avg_obp) & (dbacks_data['SLG'] > avg_slg)]
sns.scatterplot(data=top_performers, x='OBP', y='SLG', s=150, color='red', edgecolor='black', label="Top Performers", marker='D')

# Label top performers with player names, offset for clarity
for _, player in top_performers.iterrows():
    plt.text(player['OBP'] + 0.002, player['SLG'] + 0.005, player['Player'], fontsize=10, color='navy', weight='bold')

# Add reference lines for average OBP and SLG, and shade the top-right quadrant
plt.axhline(avg_slg, color='blue', linestyle='--', label=f'Avg SLG ({avg_slg:.3f})')
plt.axvline(avg_obp, color='green', linestyle='--', label=f'Avg OBP ({avg_obp:.3f})')
plt.fill_betweenx(y=[avg_slg, dbacks_data['SLG'].max()], x1=avg_obp, x2=dbacks_data['OBP'].max(),
                  color='lightblue', alpha=0.1)  # Highlight top-right quadrant

# Customize plot labels and title
plt.title("Top Performers Among Diamondbacks Players: OBP vs SLG", fontsize=16)
plt.xlabel("On-Base Percentage (OBP)", fontsize=12)
plt.ylabel("Slugging Percentage (SLG)", fontsize=12)

# Adjust legend position to the upper left outside the plot
plt.legend(loc="upper left", bbox_to_anchor=(1, 1), frameon=False)

# Save the plot
output_path = "/Users/seanryan/Documents/MLB_Project/figures/visuals/dbacks_top_performers_refined.png"
plt.savefig(output_path, bbox_inches='tight')

# Show the plot
plt.show()