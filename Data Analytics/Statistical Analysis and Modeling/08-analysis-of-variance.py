import pandas as pd
import scipy.stats as stats

def perform_anova(data, independent_var, dependent_var):
    # Extract the relevant columns from the dataset
    df = data[[independent_var, dependent_var]]

    # Group the data by the independent variable and calculate the means
    grouped_data = df.groupby(independent_var).mean()

    # Perform the ANOVA test
    result = stats.f_oneway(*[grouped_data[dependent_var].loc[group].values for group in grouped_data.index])

    # Print the ANOVA test results
    print("ANOVA Results:")
    print("---------------")
    print("F-value:", result.statistic)
    print("p-value:", result.pvalue)
    print()

# Example usage
# Load your dataset into a Pandas DataFrame
data = pd.read_csv('data.csv')

# Perform ANOVA test
perform_anova(data, 'Group', 'Value')

