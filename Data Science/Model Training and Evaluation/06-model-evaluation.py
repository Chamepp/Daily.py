from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Example ground truth and predicted labels
ground_truth = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
predicted_labels = [1, 0, 1, 1, 0, 0, 0, 1, 1, 1]

# Calculate accuracy
accuracy = accuracy_score(ground_truth, predicted_labels)

# Calculate precision
precision = precision_score(ground_truth, predicted_labels)

# Calculate recall
recall = recall_score(ground_truth, predicted_labels)

# Calculate F1-score
f1 = f1_score(ground_truth, predicted_labels)

# Print evaluation metrics
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")

