import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Create a sample dataset
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1, 2])

# Initialize the LDA model
lda = LinearDiscriminantAnalysis(n_components=1)

# Fit the LDA model on the dataset
X_reduced = lda.fit_transform(X, y)

# Print the original and reduced dimensions
print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)

