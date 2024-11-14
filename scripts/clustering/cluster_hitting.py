import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting_regular_with_features.csv'
df = pd.read_csv(data_path)

# Function to clean player names by removing special characters and extra spaces
def clean_name(name):
    name = name.replace("#", "").replace("*", "").strip()  # Remove symbols and extra spaces
    return name

# Apply the cleaning function to the 'Player' column
df['Player'] = df['Player'].apply(clean_name)

# Select refined features for clustering
features = ['BA', 'OBP', 'SLG', 'ISO', 'BB%', 'SO%', 'BB/SO', 'XBH%']
X = df[features]

# Handle missing data
for feature in features:
    if X[feature].isnull().any():
        X[feature].fillna(X[feature].mean(), inplace=True)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using Elbow Method and Silhouette Score
inertia = []
silhouette_scores = []
K_range = range(2, 8)  # Adjust range if needed

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot Elbow Method
plt.figure(figsize=(10, 4))
plt.plot(K_range, inertia, marker='o')
plt.title("Elbow Method for Optimal K (Hitting Data)")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

# Plot Silhouette Score
plt.figure(figsize=(10, 4))
plt.plot(K_range, silhouette_scores, marker='o', color='orange')
plt.title("Silhouette Score for Optimal K (Hitting Data)")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.show()

# Based on the Elbow and Silhouette Score, choose optimal_k (e.g., 3)
optimal_k = 3

# Apply KMeans with the chosen number of clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Analyze clusters by calculating feature means for each cluster
cluster_means = df.groupby('Cluster')[features].mean()
print("Cluster Means:")
print(cluster_means)

# Define cluster labels based on interpretation of means
cluster_labels = {0: 'Contact Hitter', 1: 'Power Hitter', 2: 'Balanced Hitter'}
df['Hitter_Type'] = df['Cluster'].map(cluster_labels)

# Calculate league averages and standard deviations for speed metrics
league_avg_sb = df['SB'].mean()
league_std_sb = df['SB'].std()
league_avg_sb_percent = df['SB%'].mean()
league_std_sb_percent = df['SB%'].std()
league_avg_triples = df['3B'].mean()
league_std_triples = df['3B'].std()

# Define Speed_Tier function with refined criteria
def assign_speed_tier(row):
    if ((row['SB'] >= league_avg_sb + league_std_sb or row['SB%'] >= league_avg_sb_percent + league_std_sb_percent) 
        and row['3B'] > league_avg_triples):
        return 'High Speed'
    elif (league_avg_sb - league_std_sb <= row['SB'] <= league_avg_sb + league_std_sb and 
          league_avg_sb_percent - league_std_sb_percent <= row['SB%'] <= league_avg_sb_percent + league_std_sb_percent):
        return 'Moderate Speed'
    else:
        return 'Low Speed'

# Apply the Speed_Tier function to categorize players by speed level
df['Speed_Tier'] = df.apply(assign_speed_tier, axis=1)

# Save the dataset with refined cluster labels and Speed Tier
output_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting_clustered_refined.csv'
df.to_csv(output_path, index=False)
print(f"Clustering complete. Refined data saved to {output_path}")