import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve data
cursor.execute("SELECT column1, column2, column3 FROM your_table")

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()

