import pandas as pd

def automate_correlation_analysis(data):
    # Calculate correlation matrix
    correlation_matrix = data.corr()

    # Print correlation matrix
    print("Correlation Matrix:")
    print(correlation_matrix)

    # Get pairwise correlation values
    correlations = correlation_matrix.unstack().sort_values(ascending=False)

    # Remove self-correlations (diagonal elements)
    correlations = correlations[correlations.index.get_level_values(0) != correlations.index.get_level_values(1)]

    # Print pairwise correlations
    print("\nPairwise Correlations:")
    print(correlations)

# Example usage
data = pd.read_csv('data.csv')  # Replace 'data.csv' with your dataset file
automate_correlation_analysis(data)

