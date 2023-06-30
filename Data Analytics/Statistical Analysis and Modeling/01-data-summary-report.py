import pandas as pd

def generate_summary_report(data):
    # Compute summary statistics
    summary = data.describe()

    # Add additional statistics to the summary report
    summary.loc['median'] = data.median()
    summary.loc['variance'] = data.var()
    summary.loc['skewness'] = data.skew()
    summary.loc['kurtosis'] = data.kurtosis()

    # Print the summary report
    print("Data Summary Report:")
    print(summary)

# Example usage
data = pd.read_csv("data.csv")  # Replace with your dataset file
generate_summary_report(data)

