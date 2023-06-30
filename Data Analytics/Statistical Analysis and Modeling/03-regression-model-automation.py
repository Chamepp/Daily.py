import pandas as pd
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('dataset.csv')  # Replace 'dataset.csv' with your dataset file

# Separate the dependent variable (target) and independent variables (features)
target_variable = data['target_column']  # Replace 'target_column' with your target variable column name
feature_variables = data.drop('target_column', axis=1)  # Remove the target variable column from the features

# Add a constant column for the intercept term
feature_variables = sm.add_constant(feature_variables)

# Fit the regression model
model = sm.OLS(target_variable, feature_variables)
results = model.fit()

# Print the regression summary
print(results.summary())

