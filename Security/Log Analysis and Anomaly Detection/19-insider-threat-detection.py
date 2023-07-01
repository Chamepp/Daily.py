import pandas as pd

# Function to analyze user activity logs and detect insider threats
def detect_insider_threats(log_file):
    # Read user activity logs into a pandas DataFrame
    logs_df = pd.read_csv(log_file)

    # Group logs by user and calculate activity count
    user_activity = logs_df.groupby('user')['activity'].count()

    # Identify users with unusually high activity count
    suspicious_users = user_activity[user_activity > user_activity.mean() + 2 * user_activity.std()]

    # Print suspicious users
    if len(suspicious_users) > 0:
        print("Potential insider threats detected:")
        for user in suspicious_users.index:
            print("- User:", user)
    else:
        print("No potential insider threats detected.")

# Example usage
log_file = "user_activity_logs.csv"
detect_insider_threats(log_file)

