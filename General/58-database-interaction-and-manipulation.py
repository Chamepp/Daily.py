import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store employee information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        designation TEXT,
        salary REAL
    )
''')

# Insert sample data into the table
cursor.execute("INSERT INTO employees (name, designation, salary) VALUES ('John Doe', 'Software Engineer', 5000.0)")
cursor.execute("INSERT INTO employees (name, designation, salary) VALUES ('Jane Smith', 'Product Manager', 7000.0)")

# Fetch and display all employee records
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Designation:", row[2])
    print("Salary:", row[3])
    print()

# Update the salary of an employee
cursor.execute("UPDATE employees SET salary = 5500.0 WHERE name = 'John Doe'")

# Delete an employee record
cursor.execute("DELETE FROM employees WHERE name = 'Jane Smith'")

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
