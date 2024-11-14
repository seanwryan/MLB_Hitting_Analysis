import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def handle_missing_data(data, features):
    """
    Handles missing data for selected features.
    - Uses mean imputation or fills with 0 for specific ratio metrics if appropriate.
    """
    for feature in features:
        if data[feature].isnull().any():
            # Custom handling based on feature type:
            if feature in ['BB/SO', 'HR/SB']:  # Ratio metrics where 0 may indicate no activity
                print(f"Filling missing values in {feature} with 0.")
                data[feature] = data[feature].fillna(0)
            else:  # Other metrics, we could use mean imputation
                mean_value = data[feature].mean()
                print(f"Imputing missing values in {feature} with mean value {mean_value:.3f}.")
                data[feature] = data[feature].fillna(mean_value)
    
    return data

def perform_sub_clustering(data, features, cluster_num, max_clusters=5):
    # Handle missing data in sub-clustering features
    data = handle_missing_data(data, features)

    # Standardize the selected features
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[features])

    # Determine the optimal number of clusters using the Elbow Method
    inertia = []
    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(data_scaled)
        inertia.append(kmeans.inertia_)
    
    # Plot the Elbow Method graph
    plt.figure(figsize=(10, 5))
    plt.plot(range(2, max_clusters + 1), inertia, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title(f'Elbow Method for Optimal K (Hitting Data - Stage 2, Cluster {cluster_num})')
    plt.show()
    
    # Automatically determine optimal clusters based on inertia elbow
    optimal_k = 3  # Default; change or automate selection here if desired

    # Fit KMeans with the chosen number of clusters
    kmeans = KMeans(n_clusters=optimal_k, random_state=0)
    data[f'Sub_Cluster_{cluster_num}'] = kmeans.fit_predict(data_scaled)
    
    print(f"Sub-clustering for Cluster {cluster_num} complete with {optimal_k} sub-clusters.")
    
    return data

# Load the stage 1 clustered data
data_stage1 = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_stage1_clustered.csv')

# Define sub-cluster feature sets for each main cluster
sub_cluster_features = {
    0: ['BB/SO', 'SO%', 'BB%'],         # Plate Discipline
    1: ['SB', 'SB%', 'R Rate'],         # Baserunning
    2: ['HR/SB', 'XBH%', 'ISO']         # Power/Extra Bases
}

# Perform sub-clustering on each main cluster
sub_clustered_data = []
for cluster_num, features in sub_cluster_features.items():
    cluster_data = data_stage1[data_stage1['Cluster'] == cluster_num].copy()
    sub_clustered_data.append(perform_sub_clustering(cluster_data, features, cluster_num=cluster_num))

# Combine all sub-clustered data into one DataFrame
data_stage2 = pd.concat(sub_clustered_data, ignore_index=True)

# Final check for any remaining missing sub-cluster labels
missing_sub_clusters = data_stage2[[f'Sub_Cluster_{i}' for i in sub_cluster_features.keys()]].isnull().any(axis=1)
if missing_sub_clusters.any():
    print("Warning: Some rows still have missing sub-cluster labels after handling missing data.")
    print(data_stage2[missing_sub_clusters][['Player-additional', 'Player', 'Cluster'] + [f'Sub_Cluster_{i}' for i in sub_cluster_features.keys()]])
else:
    print("All players have been successfully assigned to sub-clusters.")

# Save the final data with sub-clustering information
data_stage2.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_stage2_clustered.csv', index=False)
print("Stage 2 clustering complete. Data saved to /Users/seanryan/Documents/MLB_Project/data/processed/hitting_stage2_clustered.csv")