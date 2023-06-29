import pandas as pd

def random_sampling(data, sample_size):
    """
    Randomly samples a subset of data.

    Args:
        data (pandas.DataFrame): The input data to be sampled.
        sample_size (int): The desired size of the sample.

    Returns:
        pandas.DataFrame: The randomly sampled subset of data.
    """
    sample = data.sample(n=sample_size, random_state=42)  # Randomly sample the data
    return sample

# Example usage
# Assuming you have a dataset stored in a pandas DataFrame called 'data'
sample_size = 100  # Desired sample size
sampled_data = random_sampling(data, sample_size)
print(sampled_data.head())  # Print the first few rows of the sampled data

