from PIL import Image

# Get the file path of the image
file_path = "Visitor_Pictures/img_1.jpg"

# Open the image and get the size
image = Image.open(file_path)
width, height = image.size

# Print the width and height
print(f"The width of the image is {width} pixels.")
print(f"The height of the image is {height} pixels.")
