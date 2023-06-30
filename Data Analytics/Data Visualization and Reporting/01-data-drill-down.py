import pandas as pd

# Load the dataset (assuming it's a CSV file)
data = pd.read_csv('your_dataset.csv')

# Define the column names for drill-down analysis
columns = list(data.columns)

# Perform drill-down analysis
selected_column = None

while True:
    if selected_column is None:
        # Initial drill-down prompt
        print("Available Columns:")
        for i, column in enumerate(columns):
            print(f"{i+1}. {column}")
        
        # Select the column to drill down
        selected_option = input("Select a column to drill down (0 to exit): ")
        
        if selected_option == '0':
            break
        
        selected_column = columns[int(selected_option)-1]
    else:
        # Drill-down into selected column values
        unique_values = data[selected_column].unique()
        
        print(f"Unique values in '{selected_column}':")
        for i, value in enumerate(unique_values):
            print(f"{i+1}. {value}")
        
        # Select a specific value to further drill down or exit
        selected_option = input("Select a value to further drill down (0 to go back): ")
        
        if selected_option == '0':
            selected_column = None
        else:
            selected_value = unique_values[int(selected_option)-1]
            data = data[data[selected_column] == selected_value]

# Print the final drill-down result
print("Final Drill-Down Result:")
print(data)

