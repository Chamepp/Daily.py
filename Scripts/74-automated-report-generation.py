import pandas as pd

def generate_report(data_file, report_file):
    # Read the data from the CSV file
    data = pd.read_csv(data_file)

    # Perform data analysis and generate the report
    report = "Report generated from data in file: {}\n\n".format(data_file)
    report += "Total records: {}\n".format(len(data))
    report += "Summary Statistics:\n"
    report += "-------------------\n"
    report += "Mean: {}\n".format(data.mean())
    report += "Standard Deviation: {}\n".format(data.std())
    report += "Minimum Value: {}\n".format(data.min())
    report += "Maximum Value: {}\n".format(data.max())

    # Write the report to a text file
    with open(report_file, 'w') as file:
        file.write(report)

    print("Report generated successfully!")

# Example usage
data_file = "data.csv"
report_file = "report.txt"
generate_report(data_file, report_file)
