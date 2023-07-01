from PIL import Image, ImageDraw, ImageFont
import os

# Set the directory path containing the images
image_directory = "/path/to/images/"

# Set the watermark text and font size
watermark_text = "Your Watermark"
font_size = 30

# Set the output directory path for the watermarked images
output_directory = "/path/to/output/"

# Set the font style and color
font = ImageFont.truetype("Arial.ttf", font_size)
text_color = (255, 255, 255)  # White color

# Loop through all the images in the directory
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_directory, filename)
        
        # Open the image
        image = Image.open(image_path)
        
        # Create a transparent layer for the watermark
        watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        
        # Create a drawing context for the watermark layer
        draw = ImageDraw.Draw(watermark_layer)
        
        # Calculate the position to place the watermark (bottom-right corner)
        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = image.width - text_width - 10  # 10 pixels from the right edge
        y = image.height - text_height - 10  # 10 pixels from the bottom edge
        
        # Draw the watermark text on the watermark layer
        draw.text((x, y), watermark_text, font=font, fill=text_color)
        
        # Combine the original image and the watermark layer
        watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark_layer)
        
        # Save the watermarked image to the output directory
        output_path = os.path.join(output_directory, filename)
        watermarked_image.save(output_path)
        print(f"Watermarked image saved: {output_path}")
