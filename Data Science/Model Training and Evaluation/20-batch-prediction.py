import pandas as pd
import joblib

# Load the trained model
model = joblib.load('trained_model.pkl')

# Load the batch data for prediction
batch_data = pd.read_csv('batch_data.csv')

# Perform batch prediction
predictions = model.predict(batch_data)

# Save the predictions to a CSV file
predictions_df = pd.DataFrame({'Prediction': predictions})
predictions_df.to_csv('batch_predictions.csv', index=False)

print("Batch prediction completed. Predictions saved to 'batch_predictions.csv'.")

