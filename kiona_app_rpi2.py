import customtkinter
import RPi.GPIO as GPIO
import queue
import cv2
from PIL import Image, ImageTk
import datetime
import time
from threading import Thread
import pygame
import CTkMessagebox
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

# Set GPIO mode (BCM mode)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin for the button
bell_button_pin = 18
GPIO.setup(bell_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous_bell_button_state = GPIO.input(bell_button_pin)

# Set up GPIO pin for the button
hazard_button_pin = 2
GPIO.setup(hazard_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous_hazard_button_state = GPIO.input(bell_button_pin)

#________________________________________________________________________

# Functions for GPIO based Components:

# Queue for communication between threads
bell_button_queue = queue.Queue()
hazard_button_queue = queue.Queue()

def gpio_loop():
    global previous_bell_button_state
    global previous_hazard_button_state

    try:
        while True:

            # Read the state of bell button
            bell_button_state = GPIO.input(bell_button_pin)
            
            if bell_button_state != previous_bell_button_state:
                previous_bell_button_state = bell_button_state

                # Check if bell button is pressed
                if bell_button_state == GPIO.LOW:
                    # Put a message into the bell button queue
                    bell_button_queue.put("BellButtonPressed")
                    print("BellButtonPressed")

            # Read the state of hazard button
            hazard_button_state = GPIO.input(hazard_button_pin)
            
            if hazard_button_state != previous_hazard_button_state:
                previous_hazard_button_state = hazard_button_state

                # Check if hazard button is pressed
                if hazard_button_state == GPIO.LOW:
                    # Put a message into the hazard button queue
                    hazard_button_queue.put("HazardButtonPressed")
                    print("HazardButtonPressed")


            # Delay to debounce buttons
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nExiting program")

    finally:
        # Clean up GPIO
        GPIO.cleanup()


#________________________________________________________________________

# Functions for responsive UI:

def raise_page(page):
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

    page.pack(fill='both', expand=True)
    page.tkraise()

    for p in [
        fire_hazard_page,

        home_page,

        no_visitor_page,
        video_door_phone_page,
        
        alarm_page,
        clock_page,
        timer_page,
        
        message_centre_page,
        message_page,
        visitor_record_page,
        visitor_picture_page,
        
        digital_frame_page,
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
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

    global mode

    if mode == "light":
        customtkinter.set_appearance_mode("light")

        home_button_fhp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",   
        )

        app_bar.configure(
            fg_color="#BEBEBE",
            bg_color="#BEBEBE",
        )

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

        # Video Door Phone Page GUI Components:

        start_stream_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        speak_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        freeze_stream_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        take_a_pic_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )


        stop_stream_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button_vdpp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        video_stream_canvas.configure(
            bg="#d9d9d9",
        )

        # No Visitor Page GUI Components
        home_button_nvp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        # Alarm Page GUI Components:
        home_button_ap.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        clock_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        timer_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        # clock Page GUI Components:
        home_button_cp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button_cp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        hour_label.configure(
            # fg_color="#d9d9d9",
            fg_color="#e5e5e5",
            text_color="#292929",
        )

        hour_optionmenu.configure(
            # fg_color="#d9d9d9",
            fg_color="#e5e5e5",
            text_color="#292929",
            button_color="#b8b8b8",
            button_hover_color="darkgray",
        )

        minute_label.configure(
            # fg_color="#d9d9d9",
            fg_color="#e5e5e5",
            text_color="#292929",
        )

        minute_optionmenu.configure(
            # fg_color="#d9d9d9",
            fg_color="#e5e5e5",
            text_color="#292929",
            button_color="#b8b8b8",
            button_hover_color="darkgray",
        )

        am_pm_label.configure(
            # fg_color="#d9d9d9",
            fg_color="#e5e5e5",
            text_color="#292929",
        )

        am_pm_optionmenu.configure(
            # fg_color="#d9d9d9",
            fg_color="#e5e5e5",
            text_color="#292929",
            button_color="#b8b8b8",
            button_hover_color="darkgray",
        )

        set_alarm_button.configure(
            fg_color="#b8b8b8",
            text_color="#292929",
            hover_color="darkgray",
        )

        cancel_alarm_button.configure(
            fg_color="#b8b8b8",
            text_color="#292929",
            hover_color="darkgray",
        )

        # Timer Page GUI Components:
        home_button_tp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button_tp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        hours_label.configure(
            fg_color="#e5e5e5",
            text_color="#292929",
        )

        hours_optionmenu.configure(
            fg_color="#e5e5e5",
            text_color="#292929",
            button_color="#b8b8b8",
            button_hover_color="darkgray",
        )

        minutes_label.configure(
            fg_color="#e5e5e5",
            text_color="#292929",
        )

        minutes_optionmenu.configure(
            fg_color="#e5e5e5",
            text_color="#292929",
            button_color="#b8b8b8",
            button_hover_color="darkgray",
        )

        seconds_label.configure(
            fg_color="#e5e5e5",
            text_color="#292929",
        )

        seconds_optionmenu.configure(
            fg_color="#e5e5e5",
            text_color="#292929",
            button_color="#b8b8b8",
            button_hover_color="darkgray",
        )

        start_timer_button.configure(
            fg_color="#b8b8b8",
            text_color="#292929",
            hover_color="darkgray",
        )

        stop_timer_button.configure(
            fg_color="#b8b8b8",
            text_color="#292929",
            hover_color="darkgray",
        )      


        # Message Center Page GUI Components:

        home_button_mcp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        message_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button_mp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button_mp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        visitor_record_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button_vrp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button_vrp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        visitor_picture_button.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        back_button_vpp.configure(
            fg_color="#B8B8B8",
            text_color="#292929",
            hover_color="darkgray",
        )

        home_button_vpp.configure(
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

        # Digital Frame Page GUI Compnents:

        home_button_dfp.configure(
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

        home_button_fhp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        app_bar.configure(
            fg_color="#292929",
            bg_color="#292929",
        )

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

        # Video Door Phone Page GUI Components:
        start_stream_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        speak_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        freeze_stream_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        take_a_pic_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        stop_stream_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button_vdpp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        video_stream_canvas.configure(
            bg="#292929",
        )

        # No Visitor Page GUI Components
        home_button_nvp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        # Alarm Page GUI Components:
        home_button_ap.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        clock_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        timer_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        # clock Page GUI Components:
        home_button_cp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button_cp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        hour_label.configure(
            fg_color="#212121",
            text_color="white",
        )

        hour_optionmenu.configure(
            fg_color="#212121",
            text_color="white",
            button_color="#4B4B4B",
            button_hover_color="#585858",
        )

        minute_label.configure(
            fg_color="#212121",
            text_color="white",
        )

        minute_optionmenu.configure(
            fg_color="#212121",
            text_color="white",
            button_color="#4B4B4B",
            button_hover_color="#585858",
        )

        am_pm_label.configure(
            fg_color="#212121",
            text_color="white",
        )

        am_pm_optionmenu.configure(
            fg_color="#212121",
            text_color="white",
            button_color="#4B4B4B",
            button_hover_color="#585858",
        )


        set_alarm_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        cancel_alarm_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        # Timer Page GUI Components:
        home_button_tp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )
        
        back_button_tp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        hours_label.configure(
            fg_color="#212121",
            text_color="white",
        )

        hours_optionmenu.configure(
            fg_color="#212121",
            text_color="white",
            button_color="#4B4B4B",
            button_hover_color="#585858",
        )

        minutes_label.configure(
            fg_color="#212121",
            text_color="white",
        )

        minutes_optionmenu.configure(
            fg_color="#212121",
            text_color="white",
            button_color="#4B4B4B",
            button_hover_color="#585858",
        )

        seconds_label.configure(
            fg_color="#212121",
            text_color="white",
        )

        seconds_optionmenu.configure(
            fg_color="#212121",
            text_color="white",
            button_color="#4B4B4B",
            button_hover_color="#585858",
        )

        start_timer_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        stop_timer_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )      

        # Message Center Page GUI Components:

        home_button_mcp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        message_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button_mp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button_mp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        visitor_record_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button_vrp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button_vrp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        visitor_picture_button.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        back_button_vpp.configure(
            fg_color="#4B4B4B",
            text_color="white",
            hover_color="#585858",
        )

        home_button_vpp.configure(
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

        # Digital Frame Page GUI Compnents:

        home_button_dfp.configure(
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


def change_appearance_mode_of_image_buttons():
    global mode

    if mode == "light":
    
        for button in image_buttons:
            button.configure(
                fg_color="#4B4B4B",
                text_color="white",
                hover_color="#585858",
            )

    elif mode == "dark":

        for button in image_buttons:
            button.configure(
                fg_color="#B8B8B8",
                text_color="#292929",
                hover_color="darkgray",
            )


# Pages & GUI Components:
# Fire Hazard Page
fire_hazard_page = customtkinter.CTkFrame(master=root)

# Home Page
home_page = customtkinter.CTkFrame(master=root)

# Video Door Phone Page
no_visitor_page = customtkinter.CTkFrame(master=root)
video_door_phone_page = customtkinter.CTkFrame(master=root)

# Alarm Page
alarm_page = customtkinter.CTkFrame(master=root)
clock_page = customtkinter.CTkFrame(master=root)
timer_page = customtkinter.CTkFrame(master=root)

# Message Centre Page 
message_centre_page = customtkinter.CTkFrame(master=root)
message_page = customtkinter.CTkFrame(master=root)
visitor_record_page = customtkinter.CTkFrame(master=root)
visitor_picture_page = customtkinter.CTkFrame(master=root)

# Digital Frame Page
digital_frame_page = customtkinter.CTkFrame(master=root)


# _______________________________________________________________________

# Calculate image size based on screen resolution

image_width = screen_width
image_height = screen_height

#________________________________________________________________________

# Home and Back button Icon:

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

#________________________________________________________________________

# Fire Hazard Page:

fire_hazard_image = customtkinter.CTkImage(
    light_image=Image.open("Images/Fire-Hazard-Image.jpg")
    .resize((image_width, image_height)),
    dark_image=Image.open("Images/Fire-Hazard-Image.jpg")
    .resize((image_width, image_height)),
    size=(image_width, image_height),
)

fire_hazard_image_label = customtkinter.CTkLabel(
    master=fire_hazard_page,
    image=fire_hazard_image,
)
fire_hazard_image_label.pack(fill='both', expand=True)

home_button_fhp = customtkinter.CTkButton(
    master=fire_hazard_page,
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
home_button_fhp.place(x=1059, y=100, anchor="center")

#________________________________________________________________________

# Home page GUI components:

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
    command=lambda: raise_page(video_door_phone_page)
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
    command=lambda: raise_page(alarm_page)
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

#__________________________________________________________________________

# Video Door Phone Page GUI Components:

# Initialize video capture
video_capture = cv2.VideoCapture(0)
is_capturing = False  # Flag to control video capturing
current_image = None

# add `video_stream_frame` if needed

video_stream_canvas = customtkinter.CTkCanvas(
    master=video_door_phone_page,
    width=862,
    height=800,
)
video_stream_canvas.pack(padx=50, pady=75, side="left")

# Function definitions
def start_stream():
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()
   
    global is_capturing
    global video_capture

    video_capture = cv2.VideoCapture(0)
    is_capturing = True
   
    update_camera()


def record_microphone():
    # duration = input("Enter duration (in seconds) for microphone test: ")
    duration = 5
    command = f"arecord --format=S16_LE --duration={duration} --rate=16000 --file-type=raw out.raw"
    os.system(command)


def play_recorded_file():
    command = "aplay --format=S16_LE --rate=16000 out.raw"
    os.system(command)


def speak():
    
    if is_capturing and current_image:
        pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
        pygame.mixer.music.play()
        thrd = Thread(target=lambda: (record_microphone(), play_recorded_file()))
        thrd.start()


def freeze_stream():
    
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()
   
    global is_capturing
   
    is_capturing = False


def take_a_pic():
    
    if is_capturing and current_image:
        pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
        pygame.mixer.music.play()
        current_image.save(f'Visitor_Pictures/selfie_{int(time.time())}.jpg')


def stop_stream():

    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()
    
    global is_capturing
    global current_image

    is_capturing = False
    current_image = None
    
    video_stream_canvas.delete("all")  # Clear the canvas
    # Release the video capture object
    video_capture.release()
    # Destroy all OpenCV windows
    cv2.destroyAllWindows()


def update_camera():

    global current_image
    
    if is_capturing:
        ret, video_frame = video_capture.read()
    
        if ret:
            video_frame = cv2.resize(video_frame, (1085, 802))
            current_image = Image.fromarray(cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image=current_image)
            video_stream_canvas.create_image(0, 0, image=photo, anchor=customtkinter.NW)
            video_stream_canvas.image = photo
            root.after(15, update_camera)
    
        else:
            print("Failed to capture frame from webcam. Check webcam index.")


start_stream_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/start_icon_dark2.png'),
    dark_image=Image.open('Images/start_icon_light2.png'),
    size=(48, 48),
)

start_stream_button = customtkinter.CTkButton(
    master=video_door_phone_page,
    text="   Start               ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=start_stream_icon,
    compound="left",
    command=start_stream,
)
start_stream_button.place(x=1059, y=100, anchor="center")

speak_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/speak_dark.png'),
    dark_image=Image.open('Images/speak_light.png'),
    size=(48, 48),
)

# button to speak for ten seconds:
speak_button = customtkinter.CTkButton(
    master=video_door_phone_page,
    text="   Speak             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=speak_icon,
    compound="left",
    command=speak,
)
speak_button.place(x=1059, y=165, anchor="center")


freeze_stream_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/freeze_icon_dark2.png'),
    dark_image=Image.open('Images/freeze_icon_light2.png'),
    size=(48, 48),
)

freeze_stream_button = customtkinter.CTkButton(
    master=video_door_phone_page,
    text="  Freeze            ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=freeze_stream_icon,
    compound="left",
    command=freeze_stream,
)
freeze_stream_button.place(x=1059, y=230, anchor="center")

take_a_pic_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/take_pic_icon_dark2.png'),
    dark_image=Image.open('Images/take_pic_icon_light2.png'),
    size=(48, 48),
)

take_a_pic_button = customtkinter.CTkButton(
    master=video_door_phone_page,
    text=" Take a pic        ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=take_a_pic_icon,
    compound="left",
    command=take_a_pic,
)
take_a_pic_button.place(x=1059, y=295, anchor="center")

stop_stream_icon = customtkinter.CTkImage(
    light_image=Image.open('Images/stop_icon_dark2.png'),
    dark_image=Image.open('Images/stop_icon_light2.png'),
    size=(48, 48),
)

stop_stream_button = customtkinter.CTkButton(
    master=video_door_phone_page,
    text="   Stop              ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=stop_stream_icon,
    compound="left",
    command=stop_stream,
)
stop_stream_button.place(x=1059, y=360, anchor="center")

home_button_vdpp = customtkinter.CTkButton(
    master=video_door_phone_page,
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
home_button_vdpp.place(x=1059, y=425, anchor="center")

# __________________________________________________________________________

# No Visitor Page GUI Components:

home_button_nvp = customtkinter.CTkButton(
    master=no_visitor_page,
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
home_button_nvp.place(x=1059, y=100, anchor="center")

#__________________________________________________________________________

# Alarm Page GUI Components
home_button_ap = customtkinter.CTkButton(
    master=alarm_page,
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
home_button_ap.place(x=1059, y=100, anchor="center")

buttons_frame_ap = customtkinter.CTkFrame(
    master=alarm_page,
    fg_color="transparent",
    bg_color="transparent",
)
buttons_frame_ap.pack(pady=320)

clock_icon = customtkinter.CTkImage(
    light_image=Image.open("Images/clock_icon_dark.png"),
    dark_image=Image.open("Images/clock_icon_light.png"),
    size=(58, 58),
)

clock_button = customtkinter.CTkButton(
    master=buttons_frame_ap,
    width=170,
    height=130,
    text="Clock",
    font=("Segoe UI Semibold", 16),
    image=clock_icon,
    compound="top",
    command=lambda: raise_page(clock_page),
)
clock_button.grid(row=0, column=0, pady=10, padx=25)

timer_icon = customtkinter.CTkImage(
    light_image=Image.open("Images/timer_icon_dark.png"),
    dark_image=Image.open("Images/timer_icon_light.png"),
    size=(58, 58),
    # size=(70, 70),
)

timer_button = customtkinter.CTkButton(
    master=buttons_frame_ap,
    width=170,
    height=130,
    text="Timer",
    font=("Segoe UI Semibold", 16),
    image=timer_icon,
    compound="top",
    command=lambda: raise_page(timer_page),
)
timer_button.grid(row=0, column=1, pady=10, padx=25)

#__________________________________________________________________________

# Clock Page GUI Components
back_button_cp = customtkinter.CTkButton(
    master=clock_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(alarm_page)
)
back_button_cp.place(x=1059, y=100, anchor="center")

home_button_cp = customtkinter.CTkButton(
    master=clock_page,
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
home_button_cp.place(x=1059, y=165, anchor="center")

# Flag to control the alarm thread
alarm_on = False
pygame.mixer.init()

alarm_clock_frame = customtkinter.CTkFrame(
    clock_page,
)
alarm_clock_frame.pack(pady=270)

# Create time selection labels and optionmenus
hour_label = customtkinter.CTkLabel(
    alarm_clock_frame, 
    text="Hour",
    font=("Segoe UI Semibold", 16),
    fg_color="lightblue",
    width=140,
    height=35,
    corner_radius=6,
)
hour_label.grid(row=0, column=0, padx=15, pady=10)
# Adjust the hour range for 12-hour format
hour_optionmenu = customtkinter.CTkOptionMenu(
    alarm_clock_frame, 
    values=[f"{i:02d}" for i in range(1, 13)],
    font=("Segoe UI Semibold", 16),
    height=35,
    anchor="center",
)
hour_optionmenu.grid(row=0, column=1, padx=15, pady=10)

minute_label = customtkinter.CTkLabel(
    alarm_clock_frame, 
    text="Minute",
    font=("Segoe UI Semibold", 16),
    fg_color="lightblue",
    width=140,
    height=35,
    corner_radius=6,
)
minute_label.grid(row=1, column=0, padx=15, pady=10)
minute_optionmenu = customtkinter.CTkOptionMenu(
    alarm_clock_frame, 
    values=[f"{i:02d}" for i in range(60)],
    font=("Segoe UI Semibold", 16),
    anchor="center",
    height=35,
)
minute_optionmenu.grid(row=1, column=1, padx=15, pady=10)

# Add AM/PM option
am_pm_label = customtkinter.CTkLabel(
    alarm_clock_frame, 
    text="AM / PM",
    font=("Segoe UI Semibold", 16),
    fg_color="lightblue",
    width=140,
    height=35,
    corner_radius=6,
)
am_pm_label.grid(row=2, column=0,  padx=15, pady=10)
am_pm_optionmenu = customtkinter.CTkOptionMenu(
    alarm_clock_frame, 
    values=["AM", "PM"],
    font=("Segoe UI Semibold", 16),
    anchor="center",
    height=35,
)
am_pm_optionmenu.grid(row=2, column=1, padx=15, pady=10)

# Function to run the alarm in a separate thread
def threading():
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

    global alarm_on
    alarm_on = True
    
    set_alarm_button.configure(state="disabled")  # Disable the set alarm button
    hour_optionmenu.configure(state="disabled")
    minute_optionmenu.configure(state="disabled")
    am_pm_optionmenu.configure(state="disabled")

    thrd = Thread(target=set_alarm)
    thrd.start()


# Function to set the alarm
def set_alarm():
    global alarm_on
    set_alarm_time = f"{hour_optionmenu.get()}:{minute_optionmenu.get()} {am_pm_optionmenu.get()}"
    while alarm_on:
        time.sleep(1)
        # Use %I for 12-hour format and %p for AM/PM
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        if current_time == set_alarm_time:
            print("Alarm")
            
            pygame.mixer.music.load('Sounds/tone.mp3')
            pygame.mixer.music.play()

            if mode == "light":
                alarm_messagebox = CTkMessagebox.CTkMessagebox(
                    title="Clock",
                    icon="warning",
                    message="Alarm",
                    font=("Segoe UI Semibold", 16), 
                    option_1="Stop",
                    button_text_color="white",
                    button_color="#4B4B4B",
                    button_hover_color="#585858",
                )

            elif mode == "dark":
                alarm_messagebox = CTkMessagebox.CTkMessagebox(
                    title="Clock",
                    icon="warning",
                    message="Alarm",
                    font=("Segoe UI Semibold", 16), 
                    option_1="Stop",
                    button_text_color="#292929",
                    button_color="#b8b8b8",
                    button_hover_color="darkgray",
                )
            
            if alarm_messagebox.get() == 'Stop':
                pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.stop()
            
            set_alarm_button.configure(state="normal")  # Enable the set alarm button
            hour_optionmenu.configure(state="normal")
            minute_optionmenu.configure(state="normal")
            am_pm_optionmenu.configure(state="normal")

            break


# Function to cancel the alarm
def cancel_alarm():
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

    global alarm_on
    alarm_on = False

    set_alarm_button.configure(state="normal")  # Enable the set alarm button
    hour_optionmenu.configure(state="normal")
    minute_optionmenu.configure(state="normal")
    am_pm_optionmenu.configure(state="normal")


# Create set alarm button
set_alarm_button = customtkinter.CTkButton(
    alarm_clock_frame,
    text="Set Alarm",
    font=("Segoe UI Semibold", 16), 
    height=35,
    command=threading,
)
set_alarm_button.grid(row=3, column=0, padx=15, pady=20)

# Create cancel alarm button
cancel_alarm_button = customtkinter.CTkButton(
    alarm_clock_frame, 
    text="Cancel Alarm",
    font=("Segoe UI Semibold", 16),
    height=35, 
    command=cancel_alarm,
)
cancel_alarm_button.grid(row=3, column=1, padx=15, pady=20)

#__________________________________________________________________________

# Timer Page GUI Components

back_button_tp = customtkinter.CTkButton(
    master=timer_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(alarm_page)
)
back_button_tp.place(x=1059, y=100, anchor="center")

home_button_tp = customtkinter.CTkButton(
    master=timer_page,
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
home_button_tp.place(x=1059, y=165, anchor="center")


timer_frame = customtkinter.CTkFrame(
    timer_page,
    width=400,
    height=350,
)
timer_frame.pack(pady=270)

# Create time selection labels and optionmenus for the timer duration
hours_label = customtkinter.CTkLabel(
    timer_frame, 
    text="Hours",
    fg_color="lightblue",
    font=("Segoe UI Semibold", 16),
    height=35, 
    width=140,
    corner_radius=6,
)
hours_label.grid(row=0, column=0, padx=15, pady=10)
hours_optionmenu = customtkinter.CTkOptionMenu(
    timer_frame, 
    values=[f"{i:02d}" for i in range(24)], 
    font=("Segoe UI Semibold", 16),
    height=35, 
    anchor="center",
)
hours_optionmenu.grid(row=0, column=1, padx=15, pady=10)

minutes_label = customtkinter.CTkLabel(
    timer_frame, 
    text="Minutes",
    fg_color="lightblue",
    font=("Segoe UI Semibold", 16),
    height=35, 
    width=140,
    corner_radius=6,
)
minutes_label.grid(row=1, column=0, padx=15, pady=10)
minutes_optionmenu = customtkinter.CTkOptionMenu(
    timer_frame, 
    values=[f"{i:02d}" for i in range(60)],
    font=("Segoe UI Semibold", 16),
    height=35, 
    anchor="center",
)
minutes_optionmenu.grid(row=1, column=1, padx=15, pady=10)

seconds_label = customtkinter.CTkLabel(
    timer_frame, 
    text="Seconds",
    font=("Segoe UI Semibold", 16),
    height=35, 
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
seconds_label.grid(row=2, column=0,  padx=15, pady=10)
seconds_optionmenu = customtkinter.CTkOptionMenu(
    timer_frame, 
    values=[f"{i:02d}" for i in range(60)], 
    anchor="center",
    font=("Segoe UI Semibold", 16),
    height=35, 
)
seconds_optionmenu.grid(row=2, column=1, padx=15, pady=10)

# Function to run the timer in a separate thread
def start_timer():
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()
    
    global timer_on
    timer_on = True
    
    start_timer_button.configure(state="disabled")  # Disable the start button
    hours_optionmenu.configure(state="disabled")
    minutes_optionmenu.configure(state="disabled")
    seconds_optionmenu.configure(state="disabled")
    
    thrd = Thread(target=timer)
    thrd.start()


# Function for the timer countdown
def timer():
    global timer_on
    total_seconds = int(hours_optionmenu.get()) * 3600 + int(minutes_optionmenu.get()) * 60 + int(seconds_optionmenu.get())
    while total_seconds > 0 and timer_on:
        time.sleep(1)
        total_seconds -= 1
        # Update the timer display with the new time
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        time_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(time_format)  # Or update a label/text widget to display the countdown

    if total_seconds == 0:
        pygame.mixer.music.load('Sounds/tone.mp3')
        pygame.mixer.music.play()

        if mode == "light":
            timer_messagebox = CTkMessagebox.CTkMessagebox(
                title="Clock",
                message="Timer ended",
                font=("Segoe UI Semibold", 16), 
                option_1="Stop",
                button_text_color="white",
                button_color="#4B4B4B",
                button_hover_color="#585858",
            )

        elif mode == "dark":
            timer_messagebox = CTkMessagebox.CTkMessagebox(
                title="Clock",
                message="Timer ended",
                font=("Segoe UI Semibold", 16), 
                option_1="Stop",
                button_text_color="#292929",
                button_color="#b8b8b8",
                button_hover_color="darkgray",
            )
        
        if timer_messagebox.get() == 'Stop':
            pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.stop()
        
        start_timer_button.configure(state="normal")  # Enable the start button
        hours_optionmenu.configure(state="normal")
        minutes_optionmenu.configure(state="normal")
        seconds_optionmenu.configure(state="normal")


# Function to stop the timer
def stop_timer():
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

    global timer_on
    timer_on = False
    
    start_timer_button.configure(state="normal")  # Enable the start button
    hours_optionmenu.configure(state="normal")
    minutes_optionmenu.configure(state="normal")
    seconds_optionmenu.configure(state="normal")


# Create start timer button
start_timer_button = customtkinter.CTkButton(
    timer_frame, 
    text="Start Timer",
    font=("Segoe UI Semibold", 16),
    height=35, 
    command=start_timer,
)
start_timer_button.grid(row=3, column=0, padx=15, pady=20)

# Create stop timer button
stop_timer_button = customtkinter.CTkButton(
    timer_frame, 
    text="Stop Timer", 
    font=("Segoe UI Semibold", 16),
    height=35, 
    command=stop_timer,
)
stop_timer_button.grid(row=3, column=1, padx=15, pady=20)


#__________________________________________________________________________

# Message centre page GUI components:

home_button_mcp = customtkinter.CTkButton(
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
home_button_mcp.place(x=1059, y=100, anchor="center")

buttons_frame_mcp = customtkinter.CTkFrame(
    master=message_centre_page,
    fg_color="transparent",
    bg_color="transparent",
)
buttons_frame_mcp.pack(pady=320)

message_icon = customtkinter.CTkImage(
    light_image=Image.open("Images/notice_icon_dark.png"),
    dark_image=Image.open("Images/notice_icon_light.png"),
    size=(58, 58),
)

message_button = customtkinter.CTkButton(
    master=buttons_frame_mcp,
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
    master=buttons_frame_mcp,
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
    master=buttons_frame_mcp,
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

back_button_mp = customtkinter.CTkButton(
    master=message_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
back_button_mp.place(x=1059, y=100, anchor="center")

home_button_mp = customtkinter.CTkButton(
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
home_button_mp.place(x=1059, y=165, anchor="center")

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

back_button_vrp = customtkinter.CTkButton(
    master=visitor_record_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
back_button_vrp.place(x=1059, y=100, anchor="center")

home_button_vrp = customtkinter.CTkButton(
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
home_button_vrp.place(x=1059, y=165, anchor="center")

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

back_button_vpp = customtkinter.CTkButton(
    master=visitor_picture_page,
    text="  Back             ",
    corner_radius=0,
    height=50,
    width=189,
    font=("Segoe UI Semibold", 16),
    bg_color="black",
    image=back_icon,
    compound="left",
    command=lambda: raise_page(message_centre_page)
)
back_button_vpp.place(x=1059, y=100, anchor="center")

home_button_vpp = customtkinter.CTkButton(
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
home_button_vpp.place(x=1059, y=165, anchor="center")


# Function to create a new window with the clicked image
def create_image_window(clicked_image, img_width, img_height):
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

    image_window = customtkinter.CTkToplevel(root)
    image_window.title("Image Window")

    image_window_size = f"{img_width}x{img_height}"
    image_window.geometry(image_window_size)

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

# Image Buttons
image_buttons = []

def update_image_buttons():

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
                size=(170, 120),
            )

            deiconified_image = customtkinter.CTkImage(
                light_image=Image.open(image_location),
                dark_image=Image.open(image_location),
                size=image_original_size,
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

    # Uncomment following lines to add image auto-reload/update feature.
    # Warning: Adding this feature may slow down your application, leading to the occurrence of bugs.
    # change_appearance_mode_of_image_buttons()
    # # Schedule the next update
    # root.after(10000, update_image_buttons)  # Update every 5 seconds. Might be buggy

# Call the update function for the first time
update_image_buttons()

#__________________________________________________________________________

# Digital Frame Page GUI components:

home_button_dfp = customtkinter.CTkButton(
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
home_button_dfp.place(x=1059, y=100, anchor="center")

# Changed Colors:
digital_frame = customtkinter.CTkFrame(
    master=digital_frame_page,
)
digital_frame.place(x=420, y=250)  # Adjust placement based on your preference

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
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()
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
    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
    pygame.mixer.music.play()

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

raise_page(home_page)
# raise_page(fire_hazard_page)

change_appearance_mode()

update_realtime_labels()

def process_bell_button_queue():
    try:
        while True:
            # Check if there is a message in the queue
            message_ = bell_button_queue.get_nowait()
            if message_ == "BellButtonPressed":
                # Handle button press
                print("Bell button is pressed")
             
                # pygame.mixer.music.load('Sounds/tone.mp3')
                # pygame.mixer.music.play()
                
                raise_page(video_door_phone_page)
                
                if mode == "light":

                    pygame.mixer.music.load('Sounds/tone.mp3')
                    pygame.mixer.music.play()

                    call_messagebox = CTkMessagebox.CTkMessagebox(
                        title="Visitor's Call",
                        icon="info",
                        message="Visitors at the door",
                        font=("Segoe UI Semibold", 16), 
                        option_1="OK",
                        button_text_color="white",
                        button_color="#4B4B4B",
                        button_hover_color="#585858",
                    )

                elif mode == "dark":

                    pygame.mixer.music.load('Sounds/tone.mp3')
                    pygame.mixer.music.play()

                    call_messagebox = CTkMessagebox.CTkMessagebox(
                        title="Visitor's Call",
                        icon="info",
                        message="Visitors at the door",
                        font=("Segoe UI Semibold", 16), 
                        option_1="OK",
                        button_text_color="#292929",
                        button_color="#b8b8b8",
                        button_hover_color="darkgray",
                    )
            
                if call_messagebox.get() == 'OK':
                    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.stop()

    except queue.Empty:
        print("Bell button queue is empty")


def process_hazard_button_queue():
    try:
        while True:
            # Check if there is a message in the queue
            message_ = hazard_button_queue.get_nowait()
            if message_ == "HazardButtonPressed":
                # Handle button press
                print("Hazard button is pressed")

                # pygame.mixer.music.load('Sounds/emergency-alarm-with-reverb-29431.mp3')
                # pygame.mixer.music.play()
                
                raise_page(fire_hazard_page)
                
                if mode == "light":

                    pygame.mixer.music.load('Sounds/emergency-alarm-with-reverb-29431.mp3')
                    pygame.mixer.music.play()

                    call_messagebox = CTkMessagebox.CTkMessagebox(
                        title="Warning!",
                        icon="warning",
                        message="Hazard detected! Follow the given evacuation procedure.",
                        font=("Segoe UI Semibold", 16), 
                        option_1="OK",
                        button_text_color="white",
                        button_color="#4B4B4B",
                        button_hover_color="#585858",
                    )

                elif mode == "dark":

                    pygame.mixer.music.load('Sounds/emergency-alarm-with-reverb-29431.mp3')
                    pygame.mixer.music.play()

                    call_messagebox = CTkMessagebox.CTkMessagebox(
                        title="Warning!",
                        icon="warning",
                        message="Hazard detected! Follow the given evacuation procedure.",
                        font=("Segoe UI Semibold", 16), 
                        option_1="OK",
                        button_text_color="#292929",
                        button_color="#b8b8b8",
                        button_hover_color="darkgray",
                    )
            
                if call_messagebox.get() == 'OK':
                    pygame.mixer.music.load('Sounds/glass-knock-11-short.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.stop()

    except queue.Empty:
        print("Hazard button queue is empty")


# Create a separate thread to run gpio_loop()
gpio_thread = Thread(target=gpio_loop)
gpio_thread.start()

# Define a function to check the bell button queue periodically
def check_bell_button_queue():
    process_bell_button_queue()  # Call the function to process the bell button queue
    root.after(1000, check_bell_button_queue)  # Schedule the function to be called again after 1 second


# Define a function to check the hazard button queue periodically
def check_hazard_button_queue():
    process_hazard_button_queue()  # Call the function to process the hazard button queue
    root.after(1000, check_hazard_button_queue)  # Schedule the function to be called again after 1 second


# Start checking the bell button queue
check_bell_button_queue()

# Start checking the hazard button queue
check_hazard_button_queue()

# Start the tkinter main loop
root.mainloop()