import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
dataset = pd.read_csv('your_dataset.csv')

# Split the dataset into features (X) and target variable (y)
X = dataset.drop('target', axis=1)
y = dataset['target']

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the sizes of the train and test sets
print("Train set size:", X_train.shape[0])
print("Test set size:", X_test.shape[0])

