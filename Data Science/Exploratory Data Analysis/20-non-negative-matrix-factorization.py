import numpy as np
from sklearn.decomposition import NMF

# Generate or load your data matrix X (N samples x M features)
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the desired number of components (lower-dimensional representation)
n_components = 2

# Initialize the NMF model with the desired number of components
model = NMF(n_components=n_components)

# Fit the model to the data and perform dimensionality reduction
W = model.fit_transform(X)

# Obtain the reduced-dimensional representation of the data
X_reduced = np.dot(W, model.components_)

# Print the original and reduced-dimensional data
print("Original data:")
print(X)
print("\nReduced-dimensional data:")
print(X_reduced)

