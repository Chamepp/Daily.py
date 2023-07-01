import os
import shutil

def organize_files(directory):
    # Create folders if they don't exist
    folders = {
        'Documents': ['doc', 'docx', 'txt', 'pdf'],
        'Images': ['jpg', 'jpeg', 'png', 'gif'],
        'Videos': ['mp4', 'mov', 'avi'],
        'Music': ['mp3', 'wav'],
        'Archives': ['zip', 'rar'],
        'Others': []
    }

    for folder_name in folders:
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files into respective folders
    for filename in os.listdir(directory):
        if filename == __file__:  # Skip the script file itself
            continue

        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            extension = filename.split('.')[-1].lower()

            # Move the file to the appropriate folder
            for folder_name, extensions in folders.items():
                if extension in extensions:
                    new_folder_path = os.path.join(directory, folder_name)
                    shutil.move(file_path, new_folder_path)
                    break
            else:
                new_folder_path = os.path.join(directory, 'Others')
                shutil.move(file_path, new_folder_path)

    print('Files have been organized successfully!')

# Provide the directory path that you want to organize
directory_path = '/path/to/directory'

organize_files(directory_path)
