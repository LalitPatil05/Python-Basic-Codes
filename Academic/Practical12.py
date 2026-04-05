# Demonstrate the Image Insertion in Python.

from PIL import Image

# Open an image file

image_path = "image.jpeg"  # Replace with your image path
try:
    img = Image.open(image_path)
    img.show()  # This will display the image
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")    
