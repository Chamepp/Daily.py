import numpy as np
from sklearn.decomposition import PCA

# Create a sample dataset (replace with your own dataset)
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Instantiate the PCA object
pca = PCA(n_components=2)  # Set the desired number of components

# Fit the PCA model to the data
pca.fit(data)

# Transform the data to the reduced dimensionality
reduced_data = pca.transform(data)

# Print the explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Print the transformed data
print("Transformed Data:")
print(reduced_data)

