import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting_clustered.csv'
df = pd.read_csv(data_path)

# Filter for Diamondbacks players for highlighting
diamondbacks_players = df[df['Team'] == 'ARI']

# Define the list of metrics to plot
metrics = ['BA', 'OBP', 'SLG', 'ISO', 'SO%', 'BB%', 'HR/SB', 'XBH%']

# Set up the matplotlib figure size
plt.figure(figsize=(12, 8))

# Create a boxplot for each metric
for metric in metrics:
    plt.figure(figsize=(10, 6))
    
    # Boxplot with cluster separation
    sns.boxplot(x='Cluster', y=metric, data=df, palette='Set2', showfliers=False)
    
    # Highlight Diamondbacks players
    sns.scatterplot(x=diamondbacks_players['Cluster'], y=diamondbacks_players[metric], 
                    color='red', s=100, label='Diamondbacks', marker='D', edgecolor='black')
    
    # Customize plot
    plt.title(f'{metric} Distribution by Cluster')
    plt.xlabel('Cluster')
    plt.ylabel(metric)
    plt.legend(loc='upper right')
    plt.show()