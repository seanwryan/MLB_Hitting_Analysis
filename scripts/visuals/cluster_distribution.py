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
plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")

# Create a grouped bar chart with wider bars
sns.countplot(data=hitting_data, x='Hitter_Type', hue='Is_Diamondback', 
              palette={'Diamondbacks': '#D62728', 'Other': '#7F7F7F'},  # Adjusted colors
              dodge=True)

# Add exact count labels on top of bars
for container in plt.gca().containers:
    plt.bar_label(container, label_type='edge', fontsize=10)

# Add titles and labels
plt.title("Distribution of Hitter Archetypes Across MLB with Diamondbacks Highlighted", fontsize=14)
plt.xlabel("Hitter Type", fontsize=12)
plt.ylabel("Count of Players", fontsize=12)
plt.legend(loc="upper right")  # Move legend if it overlaps with bars

# Save the plot
output_path = "/Users/seanryan/Documents/MLB_Project/figures/visuals/cluster_distribution_refined.png"
plt.savefig(output_path, bbox_inches='tight')

# Show the plot
plt.show()