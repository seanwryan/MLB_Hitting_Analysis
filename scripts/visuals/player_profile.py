# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Load data
data_path = "/Users/seanryan/Documents/MLB_Project/data/processed/hitting/hitting_clustered_refined.csv"
hitting_data = pd.read_csv(data_path)

# Filter for Diamondbacks players only
dbacks_data = hitting_data[hitting_data['Team'] == 'ARI']

# Set up the grid layout
num_players = len(dbacks_data)
cols = 3  # Number of columns in the grid
rows = (num_players // cols) + (num_players % cols > 0)  # Calculate the required number of rows

# Define metrics and colors for each metric
metrics = ['BA', 'OBP', 'SLG', 'OPS']
metric_labels = ["Batting Avg (BA)", "On-Base % (OBP)", "Slugging % (SLG)", "On-Base + Slugging (OPS)"]
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']  # Different colors for each metric

# Create figure and gridspec layout
fig = plt.figure(figsize=(16, rows * 2.5))
gs = gridspec.GridSpec(rows, cols, figure=fig)

# Loop over each player to create a profile with horizontal bar charts
for i, (index, player) in enumerate(dbacks_data.iterrows()):
    ax = fig.add_subplot(gs[i])
    
    # Plot horizontal bars for key metrics
    values = [player[metric] for metric in metrics]

    # Plot bars with labels for each metric
    for j, (value, color) in enumerate(zip(values, colors)):
        ax.barh(j, value, color=color, edgecolor='black')
        # Align labels on the left side for consistency and reduce font size slightly
        ax.text(0.02, j, f"{metric_labels[j]}: {value:.3f}", va='center', ha='left', fontsize=8, color='black')

    # Add player name as the title for each subplot
    ax.set_title(player['Player'], fontsize=12, weight='bold')

    # Customize each subplot
    ax.set_xlim(0, 1)
    ax.set_yticks([])
    ax.set_xticks([])  # Remove x-axis ticks
    ax.invert_yaxis()  # Highest value (OPS) at the top
    ax.set_frame_on(True)  # Add subtle frame around each subplot

# Remove the legend at the bottom, as labels are included on each bar
plt.suptitle("Diamondbacks Player Profiles with Key Metrics", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to make room for the title

# Save the plot
output_path = "/Users/seanryan/Documents/MLB_Project/figures/visuals/dbacks_player_profiles_final.png"
plt.savefig(output_path, bbox_inches='tight')

# Show the plot
plt.show()