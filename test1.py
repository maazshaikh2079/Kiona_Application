import os

directory_path = "Visitor_Pictures"

# Get a list of all files in the directory
all_files = os.listdir(directory_path)

# Filter out only the files with specific extensions (e.g., ".jpg")
image_files = [file for file in all_files if file.lower().endswith('.jpg')]

# Format the file names into the desired structure
image_texts = []
row_size = 4  # Number of columns in each row
for i in range(0, len(image_files), row_size):
    row = image_files[i:i + row_size]
    image_texts.append(row)

# Print the formatted file names
for row in image_texts:
    print(row)