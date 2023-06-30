import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def automate_pca(data_file, n_components):
    # Load the data from a file (e.g., CSV)
    data = pd.read_csv(data_file)
    
    # Separate the features from the target variable (if applicable)
    X = data.drop(columns=['target'])
    
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    # Explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Output the transformed data and explained variance ratio
    transformed_data = pd.DataFrame(X_pca, columns=['PC{}'.format(i) for i in range(1, n_components+1)])
    transformed_data['target'] = data['target'] if 'target' in data.columns else None
    
    print("Transformed Data:")
    print(transformed_data.head())
    
    print("\nExplained Variance Ratio:")
    for i, ratio in enumerate(explained_variance_ratio):
        print("PC{}: {:.2f}%".format(i+1, ratio * 100))

# Example usage
data_file = "data.csv"
n_components = 2

automate_pca(data_file, n_components)

