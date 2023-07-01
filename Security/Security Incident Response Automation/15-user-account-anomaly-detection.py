import pandas as pd

# Sample login activity data (can be replaced with actual data source)
login_activity = pd.DataFrame({
    'timestamp': ['2023-06-30 08:00:00', '2023-06-30 12:00:00', '2023-06-30 16:00:00', '2023-06-30 20:00:00'],
    'username': ['user1', 'user2', 'user3', 'user1'],
    'source_ip': ['192.168.0.100', '192.168.0.200', '192.168.0.150', '192.168.0.100']
})

def detect_anomalies(login_data):
    # Group login activity by username and count unique source IP addresses
    user_counts = login_data.groupby('username')['source_ip'].nunique()

    # Determine anomalies based on a predefined threshold
    anomaly_threshold = 2  # Adjust according to your requirements
    anomalies = user_counts[user_counts > anomaly_threshold]

    # Return a list of usernames with detected anomalies
    return list(anomalies.index)

# Example usage
anomalous_users = detect_anomalies(login_activity)
if len(anomalous_users) > 0:
    print("Anomalous user accounts detected:")
    for username in anomalous_users:
        print(username)
else:
    print("No anomalous user accounts detected.")

