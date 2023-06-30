import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(data_path):
    # Load data
    df = pd.read_csv(data_path)

    # Basic statistics
    print("Basic Statistics:")
    print(df.describe())

    # Data distribution visualization
    print("Data Distribution:")
    sns.set(style="ticks")
    sns.pairplot(df)
    plt.show()

    # Correlation matrix visualization
    print("Correlation Matrix:")
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.show()

    # Additional exploratory visualizations
    # Add more code here for additional visualizations based on your dataset and requirements

# Example usage
data_path = "path/to/your/data.csv"
perform_eda(data_path)

