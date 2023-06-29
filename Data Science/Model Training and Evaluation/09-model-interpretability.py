import shap
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load and preprocess your dataset
data = pd.read_csv("your_dataset.csv")
X = data.drop("target_variable", axis=1)
y = data["target_variable"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestRegressor model (you can replace it with your own trained model)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Initialize the SHAP explainer
explainer = shap.Explainer(model)

# Compute SHAP values for a specific observation or a set of observations
# Replace `observation` with the data you want to explain (single observation or a subset of X_test)
shap_values = explainer.shap_values(observation)

# Print the SHAP values for each feature
for feature, value in zip(X.columns, shap_values):
    print(f"{feature}: {value}")

# Visualize the SHAP values
shap.summary_plot(shap_values, X_test)

