import customtkinter
from PIL import Image
import datetime
import os

mode = "dark"

customtkinter.set_appearance_mode(mode)
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("KIONA: Automation Works")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

# Functions:
def raise_page(page):
    page.pack(fill='both', expand=True)
    page.tkraise()
    for p in [
        home_page,
        message_centre_page,
        message_page,
        visitor_record_page,
        visitor_picture_page,
        digital_frame_page
    ]:
        if p != page:
            p.pack_forget()



def update_realtime_labels():
    now = datetime.datetime.now()

    # Format the date, time, and day as strings
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    day_str = now.strftime("%A")

    # Update the labels with the formatted strings
    date_label.configure(text=date_str)
    time_label.configure(text=time_str)
    day_label.configure(text=day_str)

    # Call the function again after 1000 milliseconds
    root.after(1000, update_realtime_labels)


def change_appearance_mode():
    global mode

    if mode == "light":
        customtkinter.set_appearance_mode("light")

        app_bar.configure(
            fg_color="#BEBEBE",
            bg_color="#BEBEBE",
        )

        # wallpaper_image_label.configure(
        #     # text_color="#FFA7AE",  # Coral
        #     text_color="#B6D5F9",  # Halcyon-blueish-gray
        #     # text_color="#4d6379",  # Blue-gray
        #     # text_color="#FFC6A4",  # Cream
        # )

        task_bar.configure(
            fg_color="#A0A0A0",
            bg_color="#A0A0A0",
        )

        video_door_phone_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        alarm_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        message_centre_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        digital_frame_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button3.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        message_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button1.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button4.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        visitor_record_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button2.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button5.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        visitor_picture_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button3.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button6.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        for button in image_buttons:
            button.configure(
                fg_color="#B8B8B8",
                text_color="#292929",
                hover_color="darkgray",
            )

        home_button7.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        for button in frame_buttons:
            button.configure(
                fg_color="#B8B8B8",
                text_color="#292929",
                hover_color="darkgray",
            )

        clear_button.configure(
            fg_color="#292929",
            text_color="white",
            hover_color="#4B4B4B",
        )

        call_button.configure(
            fg_color="#292929",
            text_color="white",
            hover_color="#4B4B4B",
        )

        mode = "dark"

    elif mode == "dark":

        customtkinter.set_appearance_mode("dark")

        app_bar.configure(
            fg_color="#292929",
            bg_color="#292929",
        )

        # wallpaper_image_label.configure(
        #     # text_color="#FFA7AE",  # Coral
        #     # text_color="#B6D5F9",  # Halcyon-blueish-gray
        #     # text_color="#4d6379",  # Blue-gray
        #     # text_color="#FFC6A4",  # Cream
        #     text_color="white",
        # )

        task_bar.configure(
            fg_color="#292929",
            bg_color="#292929",
        )

        video_door_phone_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        alarm_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        message_centre_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        digital_frame_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button3.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        message_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button1.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button4.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        visitor_record_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button2.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button5.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        visitor_picture_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button3.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button6.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        for button in image_buttons:
            button.configure(
                fg_color="#4B4B4B",
                text_color="white",
                hover_color="#585858",
            )

        home_button7.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        for button in frame_buttons:
            button.configure(
                fg_color="#4B4B4B",
                text_color="white",
                hover_color="#585858",
            )

        clear_button.configure(
            fg_color="#FFFFFF",
            text_color="#292929",
            hover_color="#B8B8B8",
        )

        call_button.configure(
            fg_color="#FFFFFF",
            text_color="#292929",
            hover_color="#B8B8B8",
        )

        mode = "light"


# Pages & GUI Components:

home_page = customtkinter.CTkFrame(master=root)

message_centre_page = customtkinter.CTkFrame(master=root)
message_page = customtkinter.CTkFrame(master=root)
visitor_record_page = customtkinter.CTkFrame(master=root)
visitor_picture_page = customtkinter.CTkFrame(master=root)

digital_frame_page = customtkinter.CTkFrame(master=root)

#________________________________________________________________________


# Home page GUI components:

# Calculate image size based on screen resolution
image_width = screen_width
image_height = screen_height

wallpaper_image = customtkinter.CTkImage(
    light_image=Image.open("Images/Modern-Building-Morning_1024x600.jpg")
    .resize((image_width, image_height)),
    dark_image=Image.open("Images/Modern-Building-Night-2.jpg")
    .resize((image_width, image_height)),
    size=(image_width, image_height),
)

wallpaper_label_font = customtkinter.CTkFont(
    family="Segoe UI Black",
    size=80,
    weight="bold",
    slant="roman",
    underline=False,
    overstrike=False, 
)

wallpaper_image_label = customtkinter.CTkLabel(
    master=home_page,
    text="KIONA",
    # font=("Segoe UI Black", 80),
    font=wallpaper_label_font,
    image=wallpaper_image,
    compound="center",
)
wallpaper_image_label.pack(fill='both', expand=True)

# App Bar & Stuff:
app_bar = customtkinter.CTkFrame(
    master=home_page,
    height=30,
    width=1153,
    corner_radius=0,
    fg_color="#BEBEBE",
    bg_color="#BEBEBE",
)
app_bar.place(x=0, y=0)


date_label = customtkinter.CTkLabel(
    master=app_bar,
    text="YYYY-M-D",
    font=("Segoe UI Semibold", 18),
)
date_label.place(x=10, y=5)

day_label = customtkinter.CTkLabel(
    master=app_bar,
    text="Weekday",
    font=("Segoe UI Semibold", 15),
)
day_label.place(x=125, y=5)

modes_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/moon_dark.png'),
    dark_image=Image.open('Images/sun_light.png'),
    size=(20, 20),
)

modes_button = customtkinter.CTkButton(
    master=app_bar,
    text="",
    width=0,
    height=0,
    image=modes_icon,
    fg_color="transparent",
    hover=False,
    command=change_appearance_mode,

)
modes_button.place(x=1115, y=2)
# modes_button.place(x=1120, y=2)

# Task Bar & Stuff:
task_bar = customtkinter.CTkFrame(
    master=home_page,
    height=40,
    width=1153,
    corner_radius=0,
    fg_color="#A0A0A0",
    bg_color="#A0A0A0",

)
task_bar.place(x=0, y=760)

time_label = customtkinter.CTkLabel(
    master=task_bar,
    text="00:00:00",
    font=("Segoe UI Semibold", 18),
)
time_label.place(x=10, y=6.75)

setings_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/settings_icon_dark3.png'),
    dark_image=Image.open('Images/settings_icon_light2.png'),
    size=(29, 29),
)

settings_button = customtkinter.CTkButton(
    master=task_bar,
    text="",
    width=0,
    height=0,
    image=setings_icon,
    fg_color="transparent",
    hover=False,
)
settings_button.place(x=1105, y=2)


# Home page Buttons:
video_door_phone_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/video_phone_door_dark.png'),
    dark_image=Image.open('Images/video_phone_door_light.png'),
    size=(42, 42),
)

video_door_phone_button = customtkinter.CTkButton(
    master=home_page,
    text="Video Door Phone",
    corner_radius=0,
    height=56,
    width=186,
    font=("Segoe UI Semibold", 14),
    bg_color="black",
    image=video_door_phone_icon,
    compound="left",
)
video_door_phone_button.place(x=1059, y=100, anchor="center")

alarm_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/alarm_dark2.png'),
    dark_image=Image.open('Images/alarm_light2.png'),
    size=(48, 48),
)

alarm_button = customtkinter.CTkButton(
    master=home_page,
    text=" Alarm              ",
    corner_radius=0,
    height=50,
    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=alarm_icon,
    compound="left",
)
alarm_button.place(x=1059, y=165, anchor="center")

message_centre_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/message_dark.png'),
    dark_image=Image.open('Images/message_light.png'),
    size=(48, 48),
)

message_centre_button = customtkinter.CTkButton(
    master=home_page,
    text="Message Centre",
    corner_radius=0,
    height=50,
    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=message_centre_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
message_centre_button.place(x=1059, y=230, anchor="center")

digital_frame_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/digital_frame_icon_dark.png'),
    dark_image=Image.open('Images/digital_frame_icon_light.png'),
    size=(48, 48),
)

digital_frame_button = customtkinter.CTkButton(
    master=home_page,
    text="Digital Frame     ",
    corner_radius=0,
    height=50,
    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=digital_frame_icon,
    compound="left",
    command=lambda: raise_page(digital_frame_page)
)
digital_frame_button.place(x=1059, y=295, anchor="center")

# Home Icon:
home_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/home_icon_dark.png'),
    dark_image=Image.open('Images/home_icon_light.png'),
    size=(48, 48),
)

# Back Icon:
back_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/back_icon_dark.png'),
    dark_image=Image.open('Images/back_icon_light.png'),
    size=(48, 48),
)


#__________________________________________________________________________

#


#__________________________________________________________________________



#__________________________________________________________________________

# Message centre page GUI components:



home_button3 = customtkinter.CTkButton(
    master=message_centre_page,
    text="  Home             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=home_icon,
    compound="left",
    command=lambda: raise_page(home_page)
)
home_button3.place(x=1059, y=100, anchor="center")

message_centre_frame = customtkinter.CTkFrame(
    master=message_centre_page,
    fg_color="transparent",
    bg_color="transparent",
)
message_centre_frame.pack(pady=320)

message_icon = customtkinter.CTkImage(
    light_image=Image.open("Images/notice_icon_dark.png"),
    dark_image=Image.open("Images/notice_icon_light.png"),
    size=(58, 58),
)

message_button = customtkinter.CTkButton(
    master=message_centre_frame,
    width=170,
    height=130,
    text="Message",
    font=("Segoe UI Semibold", 16),
    image=message_icon,
    compound="top",
    command=lambda: raise_page(message_page),
)
message_button.grid(row=0, column=0, pady=10, padx=25)

visitor_record_icon = customtkinter.CTkImage(
    light_image=Image.open("Images/visitor_record_icon_dark.png"),
    dark_image=Image.open("Images/visitor_record_icon_light.png"),
    size=(70, 70),
)

visitor_record_button = customtkinter.CTkButton(
    master=message_centre_frame,
    width=170,
    height=130,
    text="Visitor Record",
    font=("Segoe UI Semibold", 16),
    image=visitor_record_icon,
    compound="top",
    command=lambda: raise_page(visitor_record_page),
)
visitor_record_button.grid(row=0, column=1, pady=10, padx=25)

visitor_picture_icon = customtkinter.CTkImage(
    light_image=Image.open("Images/visitor_photo_light.png"),
    dark_image=Image.open("Images/visitor_photo_dark.png"),
    size=(58, 58),
)

visitor_picture_button = customtkinter.CTkButton(
    master=message_centre_frame,
    width=170,
    height=130,
    text="Visitor Picture",
    font=("Segoe UI Semibold", 16),
    image=visitor_picture_icon,
    compound="top",
    command=lambda: raise_page(visitor_picture_page),
)
visitor_picture_button.grid(row=0, column=2, pady=10, padx=25)

# __________________________________________________________________________
# Message page GUI Components:

back_button1 = customtkinter.CTkButton(
    master=message_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
#    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
back_button1.place(x=1059, y=100, anchor="center")

home_button4 = customtkinter.CTkButton(
    master=message_page,
    text="  Home             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=home_icon,
    compound="left",
    command=lambda: raise_page(home_page)
)
home_button4.place(x=1059, y=165, anchor="center")

message_frame = customtkinter.CTkScrollableFrame(
    master=message_page,
    label_text="Notices",
    label_font=("Segoe UI Semibold", 18),
    label_anchor="center",
    width=845,
    height=600,
)
message_frame.pack(padx=50, pady=70, side="left")

# __________________________________________________________________________
# Visitor Records page GUI Components:

back_button2 = customtkinter.CTkButton(
    master=visitor_record_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
#    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
back_button2.place(x=1059, y=100, anchor="center")

home_button5 = customtkinter.CTkButton(
    master=visitor_record_page,
    text="  Home             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=home_icon,
    compound="left",
    command=lambda: raise_page(home_page)
)
home_button5.place(x=1059, y=165, anchor="center")

visitor_record_frame = customtkinter.CTkScrollableFrame(
    master=visitor_record_page,
    label_text="Visitor Records",
    label_font=("Segoe UI Semibold", 18),
    label_anchor="center",
    width=845,
    height=600,
)
visitor_record_frame.pack(padx=50, pady=70, side="left")


# __________________________________________________________________________
# Visitor Picture page GUI Components:

back_button3 = customtkinter.CTkButton(
    master=visitor_picture_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
#    width=186,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
back_button3.place(x=1059, y=100, anchor="center")

home_button6 = customtkinter.CTkButton(
    master=visitor_picture_page,
    text="  Home             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=home_icon,
    compound="left",
    command=lambda: raise_page(home_page)
)
home_button6.place(x=1059, y=165, anchor="center")


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


# Scrollable Frame for Image Buttons
visitor_picture_frame = customtkinter.CTkScrollableFrame(
    master=visitor_picture_page,
    label_text="Visitor Pictures",
    label_font=("Segoe UI Semibold", 18),
    label_anchor="center",
    width=845,
    height=600,
)
visitor_picture_frame.pack(padx=50, pady=70, side="left")

# Pictures Directory
visitor_pictures_directory_path = "Visitor_Pictures"

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
image_buttons = []

for i, row in enumerate(image_texts):
    for j, file_name in enumerate(row):
        image_location = f"{visitor_pictures_directory_path}/{file_name}"

        image_ = Image.open(image_location)

        image_original_size = image_.size
        width, height = image_.size

        iconified_image = customtkinter.CTkImage(
            light_image=Image.open(image_location),
            dark_image=Image.open(image_location),
            size=(170, 120),
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
            width=181,
            height=130,
            corner_radius=2,
            image=iconified_image,
        )
        button.grid(row=i + 1, column=j, pady=10, padx=15)

        image_buttons.append(button)

        # Set the command for each button to open the image in a new window
        image_buttons[-1].configure(
            command=lambda img=deiconified_image, w=width, h=height:
            create_image_window(img, w, h),
        )


#__________________________________________________________________________

# Digital Frame Page GUI components:

home_button7 = customtkinter.CTkButton(
    master=digital_frame_page,
    text="  Home             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=home_icon,
    compound="left",
    command=lambda: raise_page(home_page)
)
home_button7.place(x=1059, y=100, anchor="center")

# Changed Colors:
digital_frame = customtkinter.CTkFrame(
    master=digital_frame_page,
    #width=int(screen_width * 0.5),  # Adjust width based on your preference
    #height=int(screen_height * 0.5),  # Adjust height based on your preference
    fg_color="transparent",
    bg_color="transparent"
)
digital_frame.place(x=420, y=250)  # Adjust placement based on your preference

# numbers_font = customtkinter.CTkFont(
#     family="Segoe UI Semibold",
#     weight="bold",
#     size=18,
# )

# Create an entry field
input_no_entry = customtkinter.CTkEntry(
    digital_frame,
    font=("Segoe UI Semibold", 19),
    width=320,
    height=60,
    corner_radius=5,
)
input_no_entry.grid(row=0, column=0, pady=9, padx=12, columnspan=3)


# Function to update the entry field when a button is clicked
def on_button_click(value):
    current_text = input_no_entry.get()

    # Append the button value to the current text
    updated_text = current_text + str(value)

    input_no_entry.delete(0, customtkinter.END)  # Clear the current text in the entry field
    input_no_entry.insert(0, updated_text)  # Update the entry field with the new text


# Create buttons
frame_buttons = []

frame_buttons_texts = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"],
]

for i, row in enumerate(frame_buttons_texts):

    for j, value in enumerate(row):

        button = customtkinter.CTkButton(
            digital_frame,
            text=value,
            width=90,
            height=60,
            font=("Segoe UI Semibold", 18),
            command=lambda v=value: on_button_click(v),
        )

        button.grid(row=i+1, column=j, pady=9, padx=12)
        frame_buttons.append(button)


def delete_last_character():
    current_text = input_no_entry.get()

    # Handle special case (delete the last character)
    updated_text = current_text[:-1]

    input_no_entry.delete(0, customtkinter.END)  # Clear the current text in the entry field
    input_no_entry.insert(0, updated_text)  # Update the entry field with the new text


clear_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/clear_icon_light.png'),
    dark_image=Image.open('Images/clear_icon_dark.png'),
    size=(28, 28),
)

# Create clear button
clear_button = customtkinter.CTkButton(
    master=digital_frame_page,
    text="",
    width=70,
    height=60,
    # corner_radius=100,
    image=clear_icon,
    command=delete_last_character,
)
clear_button.place(relx=0.735, rely=0.362, anchor="e")

call_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/call_icon_light.png'),
    dark_image=Image.open('Images/call_icon_dark.png'),
    size=(26, 26),
)

# Create call button
call_button = customtkinter.CTkButton(
    master=digital_frame_page,
    text="",
    width=60,
    height=60,
    corner_radius=100,
    image=call_icon,
)
call_button.place(relx=0.5142, rely=0.897, anchor="s")

#__________________________________________________________________________

#



#__________________________________________________________________________

# Function calls:

raise_page(home_page)

change_appearance_mode()

update_realtime_labels()


root.mainloop()
