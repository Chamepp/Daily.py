import os
import glob
import shutil

LOG_DIRECTORY = "/var/log"
MAX_LOG_FILES = 10

def rotate_logs(log_directory, max_log_files):
    log_files = glob.glob(os.path.join(log_directory, "*.log"))

    if len(log_files) <= max_log_files:
        return

    log_files.sort(key=os.path.getmtime)

    files_to_remove = log_files[:len(log_files) - max_log_files]
    for file in files_to_remove:
        os.remove(file)
        print(f"Removed log file: {file}")

def main():
    try:
        rotate_logs(LOG_DIRECTORY, MAX_LOG_FILES)
    except Exception as e:
        print(f"Error occurred during log rotation: {str(e)}")

if __name__ == "__main__":
    main()

