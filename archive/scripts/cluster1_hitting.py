import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load cleaned hitting data
data_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting_regular_with_features.csv'  # Update this path to the actual location
df = pd.read_csv(data_path)

# Select relevant features for stage 1 clustering
features = ['BA', 'SLG', 'ISO', 'SO%', 'BB%']
X = df[features]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the elbow method and silhouette scores
inertia = []
silhouette_scores = []
K_range = range(2, 6)  # Check for 2 to 5 clusters

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot Elbow and Silhouette Score graphs to confirm that 3 clusters is optimal
plt.figure(figsize=(10, 4))
plt.plot(K_range, inertia, marker='o')
plt.title("Elbow Method for Optimal K (Hitting Data - Stage 1)")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(K_range, silhouette_scores, marker='o', color='orange')
plt.title("Silhouette Score for Optimal K (Hitting Data - Stage 1)")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.show()

# Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Analyze clusters by calculating feature means for each cluster to interpret the player type
cluster_means = df.groupby('Cluster')[features].mean()
print("Cluster Means:")
print(cluster_means)

# Label clusters based on the means
# Manually analyze the printed cluster means to label them as contact, balanced, or power hitter clusters
# For this example, let's assume clusters are as follows:
# Cluster 0: Contact Hitters, Cluster 1: Balanced Hitters, Cluster 2: Power Hitters
cluster_labels = {0: 'Contact Hitter', 1: 'Balanced Hitter', 2: 'Power Hitter'}
df['Hitter_Type'] = df['Cluster'].map(cluster_labels)

# Save the new dataset with cluster labels for Stage 1
output_path = '/Users/seanryan/Documents/MLB_Project/data/processed/hitting_stage1_clustered.csv'  # Update this path to the save location
df.to_csv(output_path, index=False)

print(f"Stage 1 clustering complete. Data saved to {output_path}")