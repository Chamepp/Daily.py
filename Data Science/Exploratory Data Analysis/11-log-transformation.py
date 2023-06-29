import numpy as np
import pandas as pd

# Load your dataset (replace 'data.csv' with your actual dataset file)
df = pd.read_csv('data.csv')

# Select the column(s) you want to apply the log transformation to
selected_columns = ['column1', 'column2']

# Apply log transformation to selected columns
df[selected_columns] = np.log(df[selected_columns])

# Print the transformed dataset
print(df)

