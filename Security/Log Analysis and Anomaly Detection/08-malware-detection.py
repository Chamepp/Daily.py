import pandas as pd
from sklearn.cluster import KMeans

# Read security log data from a CSV file
log_data = pd.read_csv('security_logs.csv')

# Extract relevant columns for user behavior profiling
user_logs = log_data[['timestamp', 'user', 'action']]

# Convert timestamp column to datetime format
user_logs['timestamp'] = pd.to_datetime(user_logs['timestamp'])

# Group user actions by user and time interval (e.g., daily, hourly)
grouped_logs = user_logs.groupby(['user', pd.Grouper(key='timestamp', freq='D')])['action'].count().reset_index()

# Pivot the table to get user behavior profiles
user_behavior_profiles = grouped_logs.pivot(index='user', columns='timestamp', values='action').fillna(0)

# Perform clustering (e.g., KMeans) on the user behavior profiles
kmeans = KMeans(n_clusters=3)
kmeans.fit(user_behavior_profiles)

# Assign cluster labels to user behavior profiles
user_behavior_profiles['cluster_label'] = kmeans.labels_

# Print the user behavior profiles with their assigned cluster labels
print(user_behavior_profiles)

