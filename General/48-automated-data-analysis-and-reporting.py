import pandas as pd

# Load the data from a CSV file
data = pd.read_csv('data.csv')

# Perform data analysis
summary = data.describe()

# Generate a report
report = summary.to_html()

# Save the report to an HTML file
with open('data_report.html', 'w') as file:
    file.write(report)

print("Data analysis report generated successfully!")
