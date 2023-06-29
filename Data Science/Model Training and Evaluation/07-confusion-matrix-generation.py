import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
predicted_labels = [1, 0, 0, 0, 1, 0, 1, 1, 1, 0]

# Create confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Convert confusion matrix to a pandas DataFrame for better visualization
cm_df = pd.DataFrame(cm, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm_df, annot=True, cmap='Blues', fmt='d')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

