import subprocess

def configure_mysql_server():
    # Install MySQL Server
    subprocess.run(["apt-get", "install", "-y", "mysql-server"])

    # Start MySQL service
    subprocess.run(["service", "mysql", "start"])

    # Secure MySQL installation
    subprocess.run(["mysql_secure_installation"])

    # Configure MySQL to listen on all IP addresses
    subprocess.run(["sed", "-i", "s/bind-address/#bind-address/", "/etc/mysql/mysql.conf.d/mysqld.cnf"])
    
    # Restart MySQL service
    subprocess.run(["service", "mysql", "restart"])

    print("MySQL server setup and configuration completed.")

# Call the function to execute the script
configure_mysql_server()

