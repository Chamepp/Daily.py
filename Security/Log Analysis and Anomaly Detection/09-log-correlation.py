import pandas as pd

def detect_login_anomalies(log_data, threshold=3):
    # Group login attempts by user
    login_attempts = log_data.groupby('username').count().reset_index()

    # Identify users with login attempts above the threshold
    anomaly_users = login_attempts[login_attempts['login_attempts'] > threshold]['username']

    if len(anomaly_users) > 0:
        print("Login Anomalies Detected:")
        print("------------------------")
        for user in anomaly_users:
            print(f"Anomaly detected for user: {user}")
    else:
        print("No login anomalies detected.")

# Example usage
log_data = pd.read_csv('login_logs.csv')
detect_login_anomalies(log_data, threshold=3)

