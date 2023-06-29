import pandas as pd

def generate_data_summary(dataset):
    # Load the dataset
    df = pd.read_csv(dataset)  # Modify this line based on your dataset format

    # Calculate basic statistics for each column
    summary = df.describe()

    # Add mode as a separate row
    mode_row = df.mode().iloc[0]
    summary.loc['mode'] = mode_row

    # Add median as a separate row
    median_row = df.median()
    summary.loc['median'] = median_row

    # Print the summary
    print(summary)

# Example usage
dataset_file = 'your_dataset.csv'  # Replace with the path to your dataset file
generate_data_summary(dataset_file)

