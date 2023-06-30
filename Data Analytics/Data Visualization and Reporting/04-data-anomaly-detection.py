import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Select the features/columns for anomaly detection
features = ['feature1', 'feature2', 'feature3']

# Create the Isolation Forest model
model = IsolationForest(contamination=0.05)  # Adjust contamination parameter as needed

# Fit the model to the data
model.fit(data[features])

# Predict anomaly scores for the data
anomaly_scores = model.decision_function(data[features])

# Add the anomaly scores as a new column in the dataset
data['anomaly_score'] = anomaly_scores

# Identify anomalies based on a threshold (e.g., -0.5)
anomalies = data[data['anomaly_score'] < -0.5]

# Print the detected anomalies
print("Detected Anomalies:")
print(anomalies)

# Save the anomalies to a CSV file
anomalies.to_csv('anomalies.csv', index=False)

