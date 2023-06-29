from sklearn.decomposition import PCA
import pandas as pd

# Load the raw data
raw_data = pd.read_csv("raw_data.csv")  # Replace "raw_data.csv" with your own data file

# Separate features and target variable (if applicable)
X = raw_data.drop("target", axis=1)  # Replace "target" with your target variable column name

# Perform PCA for dimensionality reduction
pca = PCA(n_components=2)  # Set the desired number of components
X_transformed = pca.fit_transform(X)

# Create a new DataFrame with the transformed features
transformed_data = pd.DataFrame(data=X_transformed, columns=["PC1", "PC2"])

# Optional: Print the explained variance ratio
explained_variance = pca.explained_variance_ratio_
print("Explained Variance Ratio:", explained_variance)

# Optional: Print the top contributing features for each principal component
top_features = pd.DataFrame(data=pca.components_, columns=X.columns)
print("Top Features for Principal Component 1:")
print(top_features.loc[0].nlargest(5))  # Adjust the number (5) for the desired top features
print("Top Features for Principal Component 2:")
print(top_features.loc[1].nlargest(5))

# Save the transformed data to a new file
transformed_data.to_csv("transformed_data.csv", index=False)  # Replace "transformed_data.csv" with your desired file name

