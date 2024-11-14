import pandas as pd

# Load the stage 2 clustered data
data_stage2 = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_stage2_clustered.csv')

# Define features of interest for analysis
features = [
    'BA', 'SLG', 'ISO', 'SO%', 'BB%', 'BB/SO', 'HR/SB', 'SB%', 'XBH%', 'BABIP', 
    'RBI Rate', 'R Rate'
]

# Group by each main Cluster and Sub_Cluster to calculate the mean of each feature
sub_cluster_means = data_stage2.groupby(['Cluster', 'Sub_Cluster_0', 'Sub_Cluster_1', 'Sub_Cluster_2'])[features].mean()

# Display results
print("Sub-Cluster Characteristics (Mean Feature Values):")
print(sub_cluster_means)

# Save results to a CSV for reference
sub_cluster_means.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_sub_cluster_means.csv')
print("Sub-cluster mean characteristics saved to /Users/seanryan/Documents/MLB_Project/data/processed/hitting_sub_cluster_means.csv")