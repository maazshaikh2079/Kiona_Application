# TODO: Fix The Bug
# `# Here ->` `visitor_picture_frame` is updated / reloaded every 5 seconds which creates a filker in frame each time it is reloaded. 
# Make chages so that is reloaded only when an image is added to `Visitor_Pictures` directory.
# This bug is visible at first image button (i.e. `image_button[0]`) in `visitor_picture_frame` of `kiona_app_rpi.py`.

import customtkinter
from PIL import Image
import os

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# Function to create a new window with the clicked image
def create_image_window(clicked_image, img_width, img_height):
    image_window = customtkinter.CTkToplevel(root)
    image_window.title("Image Window")

    image_window_size = f"{img_width}x{img_height}"
    image_window.geometry(image_window_size)
    # image_window.resizable(False, False)

    image_frame = customtkinter.CTkFrame(master=image_window)
    image_frame.pack(fill="both", expand=True)

    image_label = customtkinter.CTkLabel(
        master=image_frame,
        text="",
        image=clicked_image,
    )
    image_label.pack(fill="both", expand=True)


# Create the main window
root = customtkinter.CTk()
root.title("Visitor Picture Page")
root.geometry("1024x600")
root.resizable(False, False)

visitor_picture_page = customtkinter.CTkFrame(master=root)
visitor_picture_page.pack(fill='both', expand=True)

# Back Icon
back_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/back_icon_dark.png'),
    dark_image=Image.open('Images/back_icon_light.png'),
    size=(48, 48),
)

# Back Button
back_button = customtkinter.CTkButton(
    master=visitor_picture_page,
    text="  Back                    ",
    corner_radius=0,
    height=50,
    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
)
back_button.place(x=930, y=100, anchor="center")

# Home Icon
home_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/home_icon_dark.png'),
    dark_image=Image.open('Images/home_icon_light.png'),
    size=(48, 48),
)

# Home Button
home_button = customtkinter.CTkButton(
    master=visitor_picture_page,
    text="  Home                  ",
    corner_radius=0,
    height=50,
    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=home_icon,
    compound="left",
)
home_button.place(x=930, y=165, anchor="center")

# Scrollable Frame for Image Buttons
visitor_picture_frame = customtkinter.CTkScrollableFrame(
    master=visitor_picture_page,
    width=746,
    height=446,
)
visitor_picture_frame.pack(padx=30, pady=70, side="left")

# Pictures Directory
visitor_pictures_directory_path = "Visitor_Pictures"

# Image Buttons
image_buttons = []

def update_image_buttons():
    # Clear existing buttons
    # for button in image_buttons:
    #     button.destroy()
    # image_buttons.clear()

    # Get a list of all files in the directory
    files_in_directory = os.listdir(visitor_pictures_directory_path)

    # Filter out only the files with specific extensions (e.g., ".jpg")
    image_files = [file for file in files_in_directory if file.lower().endswith('.jpg')]

    # Format the file names into the desired structure
    image_texts = []
    row_size = 4  # Number of columns in each row
    for i in range(0, len(image_files), row_size):
        row = image_files[i:i + row_size]
        image_texts.append(row)

    # Image Buttons
    # image_buttons = []

    # Re-create the image buttons
    for i, row in enumerate(image_texts):
        for j, file_name in enumerate(row):
            image_location = f"{visitor_pictures_directory_path}/{file_name}"

            image_ = Image.open(image_location)

            image_original_size = image_.size
            width, height = image_.size

            iconified_image = customtkinter.CTkImage(
                light_image=Image.open(image_location),
                dark_image=Image.open(image_location),
                size=(169, 120),
            )

            deiconified_image = customtkinter.CTkImage(
                light_image=Image.open(image_location),
                dark_image=Image.open(image_location),
                size=image_original_size,
                # size=(512, 400),
                # size=(512, 300),
            )

            button = customtkinter.CTkButton(
                master=visitor_picture_frame,
                text="",
                font=("Segoe UI Semibold", 16),
                width=160,
                height=120,
                corner_radius=2,
                image=iconified_image,
            )
            button.grid(row=i + 1, column=j, pady=5, padx=5)

            image_buttons.append(button)

            # Set the command for each button to open the image in a new window
            image_buttons[-1].configure(
                command=lambda img=deiconified_image, w=width, h=height:
                create_image_window(img, w, h),
            )

    # Here ->
    # Schedule the next update
    root.after(5000, update_image_buttons)  # Update every 5 seconds

# Call the update function for the first time
update_image_buttons()


root.mainloop()
