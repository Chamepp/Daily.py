import joblib

def save_model(model, filepath):
    # Save the trained model to a file
    joblib.dump(model, filepath)
    print("Model saved successfully!")

def load_model(filepath):
    # Load the trained model from a file
    model = joblib.load(filepath)
    print("Model loaded successfully!")
    return model

def predict(model, data):
    # Make predictions using the loaded model
    predictions = model.predict(data)
    return predictions

# Example usage
trained_model = # Your trained model object

# Save the model to a file
save_model(trained_model, "model.pkl")

# Load the model from a file
loaded_model = load_model("model.pkl")

# Example prediction using the loaded model
test_data = # Your test data
predictions = predict(loaded_model, test_data)

# Use the predictions for further analysis or processing

