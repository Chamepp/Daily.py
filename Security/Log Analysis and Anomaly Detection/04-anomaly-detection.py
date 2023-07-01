import pandas as pd
from sklearn.ensemble import IsolationForest

# Load log data into a pandas DataFrame
log_data = pd.read_csv('security_logs.csv')

# Select relevant features for anomaly detection
selected_features = ['timestamp', 'source_ip', 'destination_ip', 'event_type']

# Prepare the data for anomaly detection
data_for_detection = log_data[selected_features]

# Fit the Isolation Forest model for anomaly detection
model = IsolationForest(contamination=0.01)  # Adjust contamination based on expected anomaly rate
model.fit(data_for_detection)

# Predict anomalies in the data
anomaly_predictions = model.predict(data_for_detection)

# Add anomaly predictions to the original log data
log_data['is_anomaly'] = anomaly_predictions

# Filter out the anomalies
anomalies = log_data[log_data['is_anomaly'] == -1]

# Print the detected anomalies
print("Detected Anomalies:")
print(anomalies)

# Save the anomalies to a CSV file
anomalies.to_csv('detected_anomalies.csv', index=False)

