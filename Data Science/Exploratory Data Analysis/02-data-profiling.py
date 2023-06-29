import pandas as pd
import pandas_profiling

# Load the dataset
data = pd.read_csv("your_dataset.csv")  # Replace "your_dataset.csv" with the path to your dataset file

# Generate the profile report
profile = pandas_profiling.ProfileReport(data)

# Save the report to an HTML file
profile.to_file("data_profile_report.html")  # Replace "data_profile_report.html" with the desired output file name

