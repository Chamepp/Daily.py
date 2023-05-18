import os

def batch_rename(directory, prefix):
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Create the new filename with the desired prefix
        new_filename = f"{prefix}_{filename}"
        
        # Get the full paths of the old and new filenames
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        
        # Print the old and new filenames for reference
        print(f"Renamed: {filename} to {new_filename}")

# Specify the directory containing the files to be renamed
directory = "/path/to/files"

# Specify the prefix to be added to each filename
prefix = "new_prefix"

# Call the batch_rename function with the specified directory and prefix
batch_rename(directory, prefix)
