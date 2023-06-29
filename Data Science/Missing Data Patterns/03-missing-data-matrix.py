import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_missing_data(data):
    # Create a boolean matrix indicating missing values
    missing_data = data.isnull()

    # Create a missing data matrix using seaborn heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(missing_data, cmap='viridis', cbar=False)
    plt.title('Missing Data Matrix')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.show()

# Example usage
# Assuming 'data' is your pandas DataFrame
visualize_missing_data(data)

