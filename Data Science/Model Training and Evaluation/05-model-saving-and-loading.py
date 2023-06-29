import joblib
from sklearn import svm
from sklearn import datasets

# Load a sample dataset for demonstration (you can replace this with your own data)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Train a model (SVM classifier in this example)
model = svm.SVC()
model.fit(X, y)

# Save the trained model to disk
joblib.dump(model, 'trained_model.pkl')

# Load the saved model from disk
loaded_model = joblib.load('trained_model.pkl')

# Use the loaded model for prediction
new_data = [[5.1, 3.5, 1.4, 0.2]]  # New data for prediction
prediction = loaded_model.predict(new_data)

print(f"Predicted class for new data: {prediction}")

