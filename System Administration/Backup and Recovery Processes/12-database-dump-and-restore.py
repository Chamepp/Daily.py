import subprocess

# Configuration
db_host = 'localhost'
db_user = 'your_username'
db_password = 'your_password'
db_name = 'your_database_name'
backup_path = '/path/to/backup/directory'

# Dump the database
dump_filename = f'{backup_path}/{db_name}_backup.sql'
dump_command = f'mysqldump -h {db_host} -u {db_user} -p{db_password} {db_name} > {dump_filename}'
subprocess.run(dump_command, shell=True, check=True)

# Restore the database
restore_command = f'mysql -h {db_host} -u {db_user} -p{db_password} {db_name} < {dump_filename}'
subprocess.run(restore_command, shell=True, check=True)

# Print success message
print('Database backup and restore completed successfully!')

