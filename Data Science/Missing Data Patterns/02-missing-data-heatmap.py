import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# Generate a missing data matrix
missing_data_matrix = df.isnull()

# Create a heatmap using seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(missing_data_matrix, cmap="viridis", cbar=False)
plt.title("Missing Data Heatmap")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()

