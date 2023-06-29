import pandas as pd

# Sample data
data = {
    'Region': ['North', 'North', 'South', 'South', 'West', 'West'],
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Banana'],
    'Sales': [100, 200, 150, 300, 250, 100]
}

df = pd.DataFrame(data)

# Creating a pivot table
pivot_table = df.pivot_table(values='Sales', index='Region', columns='Product', aggfunc='sum')

# Print the pivot table
print(pivot_table)

