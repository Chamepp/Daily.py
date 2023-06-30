import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Select the relevant features for clustering
features = data[['feature1', 'feature2', 'feature3']]

# Specify the number of clusters
num_clusters = 3

# Create a K-Means model
kmeans = KMeans(n_clusters=num_clusters)

# Fit the model to the data
kmeans.fit(features)

# Assign cluster labels to each data point
labels = kmeans.labels_

# Add the cluster labels to the dataset
data['cluster_label'] = labels

# Print the cluster labels
print(data['cluster_label'])

