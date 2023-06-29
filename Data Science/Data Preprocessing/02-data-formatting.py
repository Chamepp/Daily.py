import pandas as pd

def format_data(data):
    # Convert data types
    data['Age'] = data['Age'].astype(int)
    data['Salary'] = data['Salary'].astype(float)
    
    # Standardize date format
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    
    # Remove unnecessary characters
    data['Name'] = data['Name'].str.replace('[^a-zA-Z\s]', '')
    
    return data

# Sample data
data = pd.DataFrame({
    'Name': ['John!', 'Emily?', 'Mike#'],
    'Age': ['25', '32', '40'],
    'Salary': ['2500.50', '3200.75', '4000.00'],
    'Date': ['2021-05-15', '2022-02-20', '2023-01-10']
})

# Format the data
formatted_data = format_data(data)

# Print the formatted data
print(formatted_data)

