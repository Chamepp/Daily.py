import pandas as pd
from sklearn.model_selection import train_test_split

def data_sampling_stratification(input_file, output_file, target_column, test_size=0.2, random_state=42):
    # Read data from input file (assuming it's in CSV format)
    data = pd.read_csv(input_file)

    # Perform data stratification based on the target column
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Perform data sampling and split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    # Save the sampled data into output files
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)
    
    train_data.to_csv(output_file + "_train.csv", index=False)
    test_data.to_csv(output_file + "_test.csv", index=False)

# Example usage:
input_file = "data.csv"  # Replace with your input data file
output_file = "sampled_data"  # Replace with your desired output file name
target_column = "target"  # Replace with the name of the target column in your dataset

data_sampling_stratification(input_file, output_file, target_column)

