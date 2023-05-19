from PIL import Image
import os

def resize_images(input_folder, output_folder, size):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image file
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Resize the image
            resized_image = image.resize(size)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_image.save(output_path)

            print(f"Resized {filename} successfully!")

# Provide the input folder containing images
input_folder = "/path/to/input/folder"

# Provide the output folder where resized images will be saved
output_folder = "/path/to/output/folder"

# Set the desired size for the resized images
size = (800, 600)  # Specify width and height in pixels

# Call the resize_images function
resize_images(input_folder, output_folder, size)
