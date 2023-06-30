import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get values from the configuration file
database_host = config.get('Database', 'host')
database_port = config.get('Database', 'port')
database_username = config.get('Database', 'username')
database_password = config.get('Database', 'password')

# Perform configuration management tasks
# For example, you can use the retrieved values to set up the database connection

def setup_database_connection():
    # Set up the database connection using the configuration values
    # Here, we are just printing the values as an example
    print("Database Configuration:")
    print(f"Host: {database_host}")
    print(f"Port: {database_port}")
    print(f"Username: {database_username}")
    print(f"Password: {database_password}")
    
    # Add your code here to establish the database connection

# Call the function to setup the database connection
setup_database_connection()

