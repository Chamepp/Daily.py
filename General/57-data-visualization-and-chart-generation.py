import matplotlib.pyplot as plt

# Sample data
languages = ['Python', 'Java', 'JavaScript', 'C#', 'C++']
popularity = [70, 65, 60, 50, 45]

# Plotting the bar chart
plt.bar(languages, popularity)

# Adding labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')

# Displaying the chart
plt.show()
