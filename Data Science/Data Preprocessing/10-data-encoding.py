import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data with categorical variable
data = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Green']
})

# Perform one-hot encoding
encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(data[['Color']])

# Create a new DataFrame with encoded data
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names(['Color']))

# Concatenate the original data with the encoded data
result = pd.concat([data, encoded_df], axis=1)

# Print the result
print(result)

