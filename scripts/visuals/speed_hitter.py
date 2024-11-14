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
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# Create a grouped bar plot for "Other" players by Hitter_Type and Speed_Tier
sns.countplot(data=hitting_data[hitting_data['Is_Diamondback'] == 'Other'], 
              x='Hitter_Type', hue='Speed_Tier', palette='Blues', dodge=True, width=0.7)

# Overlay Diamondbacks players with custom bars
speed_tiers = hitting_data['Speed_Tier'].unique()
hitter_types = hitting_data['Hitter_Type'].unique()

# Loop over each combination of Hitter_Type and Speed_Tier to add Diamondbacks counts
for i, hitter_type in enumerate(hitter_types):
    for j, speed_tier in enumerate(speed_tiers):
        # Filter data for current Hitter_Type, Speed_Tier, and Diamondbacks players
        count = len(hitting_data[(hitting_data['Hitter_Type'] == hitter_type) & 
                                 (hitting_data['Speed_Tier'] == speed_tier) & 
                                 (hitting_data['Is_Diamondback'] == 'Diamondbacks')])
        
        # Calculate position for the bar
        bar_position = i - 0.2 + j * 0.25
        
        # Plot the bar if there is any count
        if count > 0:
            plt.bar(bar_position, count, width=0.2, color='red', edgecolor='black')
            # Add the count as a label above each red Diamondbacks bar
            plt.text(bar_position, count + 2, str(count), ha='center', color='black', fontsize=10)

# Customize plot labels and title
plt.title("Speed Tier Distribution by Hitter Type for Diamondbacks vs. Other Players", fontsize=14)
plt.xlabel("Hitter Type", fontsize=12)
plt.ylabel("Count of Players", fontsize=12)

# Create a custom legend with just one entry for Diamondbacks
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='red', edgecolor='black', label='Diamondbacks')]
plt.legend(handles=legend_elements, loc="upper right")

# Save the plot
output_path = "/Users/seanryan/Documents/MLB_Project/figures/visuals/speed_tier_distribution_grouped_refined.png"
plt.savefig(output_path, bbox_inches='tight')

# Show the plot
plt.show()