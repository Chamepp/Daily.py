import os
import csscompressor
import jsmin

def compress_css_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".css"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                original_content = file.read()
                compressed_content = csscompressor.compress(original_content)
            with open(file_path, "w") as file:
                file.write(compressed_content)
            print(f"Compressed: {file_path}")

def compress_js_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".js"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                original_content = file.read()
                compressed_content = jsmin.jsmin(original_content)
            with open(file_path, "w") as file:
                file.write(compressed_content)
            print(f"Compressed: {file_path}")

# Example usage
assets_directory = "path/to/assets"
compress_css_files(assets_directory)
compress_js_files(assets_directory)

