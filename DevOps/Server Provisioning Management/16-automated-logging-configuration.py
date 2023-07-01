import os
import shutil
import subprocess

def configure_logging():
    # Create a backup of the original log configuration file
    original_config_path = '/etc/rsyslog.conf'
    backup_config_path = '/etc/rsyslog.conf.bak'
    shutil.copyfile(original_config_path, backup_config_path)

    # Configure logging options in the rsyslog configuration file
    with open(original_config_path, 'a') as config_file:
        config_file.write("\n# Custom logging configuration\n")
        config_file.write("local1.* /var/log/application.log\n")
        config_file.write("& ~\n")

    # Restart the rsyslog service to apply the changes
    subprocess.run(['systemctl', 'restart', 'rsyslog'])

def configure_log_rotation():
    # Create a log rotation configuration file
    log_rotation_file = '/etc/logrotate.d/application'

    with open(log_rotation_file, 'w') as rotation_file:
        rotation_file.write("/var/log/application.log {\n")
        rotation_file.write("    rotate 7\n")
        rotation_file.write("    daily\n")
        rotation_file.write("    compress\n")
        rotation_file.write("    missingok\n")
        rotation_file.write("    notifempty\n")
        rotation_file.write("    create 0644 root root\n")
        rotation_file.write("}\n")

    # Execute log rotation to create initial log files
    subprocess.run(['logrotate', '-f', log_rotation_file])

def main():
    configure_logging()
    configure_log_rotation()
    print("Logging and log rotation configured successfully.")

if __name__ == "__main__":
    main()

