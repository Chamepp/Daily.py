import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
data = pd.read_csv('data.csv')

# Perform data analysis and generate visualizations
# Replace the following code with your specific data analysis and visualization tasks

# Example: Generate a bar chart of total sales by product category
sales_by_category = data.groupby('Category')['Sales'].sum()
sales_by_category.plot(kind='bar', rot=45)
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.title('Sales by Category')
plt.tight_layout()
plt.show()

# Example: Calculate average revenue per customer by region
revenue_per_customer = data.groupby('Region')['Revenue'].mean()
print("Average Revenue per Customer by Region:")
print(revenue_per_customer)

# Example: Generate a summary report
summary_report = data.describe()
summary_report.to_csv('summary_report.csv')

# Save visualizations to image files
# Replace the following code with your specific visualization saving tasks

# Example: Save the bar chart as an image file
sales_by_category.plot(kind='bar', rot=45)
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.title('Sales by Category')
plt.tight_layout()
plt.savefig('sales_by_category.png')

