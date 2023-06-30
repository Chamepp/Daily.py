import pandas as pd

def merge_datasets(input_files, output_file):
    # Read the first input file as the base dataset
    base_df = pd.read_csv(input_files[0])

    # Iterate over the remaining input files and merge them with the base dataset
    for file in input_files[1:]:
        df = pd.read_csv(file)
        base_df = pd.merge(base_df, df, on='common_column', how='inner')

    # Write the merged dataset to an output file
    base_df.to_csv(output_file, index=False)
    print("Datasets merged successfully. Merged dataset saved to", output_file)

# Example usage
input_files = ['dataset1.csv', 'dataset2.csv', 'dataset3.csv']
output_file = 'merged_dataset.csv'

merge_datasets(input_files, output_file)

