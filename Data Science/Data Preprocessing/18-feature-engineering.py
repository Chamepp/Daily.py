import pandas as pd

# Load the dataset
dataset = pd.read_csv('input.csv')

# Perform feature engineering
# Example: Create a new feature by combining existing features
dataset['total_sales'] = dataset['quantity'] * dataset['price']

# Example: Transform existing feature using a mathematical function
dataset['log_price'] = dataset['price'].apply(lambda x: math.log(x))

# Save the updated dataset
dataset.to_csv('output.csv', index=False)

