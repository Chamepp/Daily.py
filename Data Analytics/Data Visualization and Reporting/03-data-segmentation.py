import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv("your_dataset.csv")  # Replace with your dataset file path

# Select the features for clustering
features = data[['feature1', 'feature2', 'feature3']]  # Replace with your desired features

# Define the number of clusters
num_clusters = 3

# Perform clustering
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(features)

# Add the cluster labels to the dataset
data['cluster_label'] = kmeans.labels_

# Save the segmented data to a new file
data.to_csv("segmented_data.csv", index=False)  # Replace with your desired output file path

