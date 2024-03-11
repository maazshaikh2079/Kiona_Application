import customtkinter
import CTkMessagebox
import datetime
import time
import pygame
from threading import Thread

# Set the appearance mode and color theme
customtkinter.set_appearance_mode("light")  # Other options: "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Other color themes are available

# Initialize the main application window
root = customtkinter.CTk()
root.title("Alarm Clock App")
root.geometry("400x250")

# Flag to control the alarm thread
alarm_on = False
pygame.mixer.init()

alarm_clock_frame = customtkinter.CTkFrame(
    root,
    width=400,
    height=350,
    # fg_color="transparent",
    # bg_color="transparent",
)
alarm_clock_frame.pack(pady=30)

# Create time selection labels and optionmenus
hour_label = customtkinter.CTkLabel(
    alarm_clock_frame, 
    text="Hour",
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
hour_label.grid(row=0, column=0, padx=10, pady=5)
# Adjust the hour range for 12-hour format
hour_optionmenu = customtkinter.CTkOptionMenu(
    alarm_clock_frame, 
    values=[f"{i:02d}" for i in range(1, 13)],
    anchor="center",
)
hour_optionmenu.grid(row=0, column=1, padx=10, pady=5)

minute_label = customtkinter.CTkLabel(
    alarm_clock_frame, 
    text="Minute",
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
minute_label.grid(row=1, column=0, padx=10, pady=5)
minute_optionmenu = customtkinter.CTkOptionMenu(
    alarm_clock_frame, 
    values=[f"{i:02d}" for i in range(60)],
    anchor="center",
)
minute_optionmenu.grid(row=1, column=1, padx=10, pady=5)

# Add AM/PM option
am_pm_label = customtkinter.CTkLabel(
    alarm_clock_frame, 
    text="AM / PM",
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
am_pm_label.grid(row=2, column=0,  padx=10, pady=5)
am_pm_optionmenu = customtkinter.CTkOptionMenu(
    alarm_clock_frame, 
    values=["AM", "PM"],
    anchor="center",
)
am_pm_optionmenu.grid(row=2, column=1, padx=10, pady=5)

# Function to run the alarm in a separate thread
def threading():
    global alarm_on
    alarm_on = True
    
    set_alarm_button.configure(state="disabled")  # Disable the set alarm button
    hour_optionmenu.configure(state="disabled")
    minute_optionmenu.configure(state="disabled")
    am_pm_optionmenu.configure(state="disabled")

    thrd = Thread(target=alarm)
    thrd.start()


# Function to set the alarm
def alarm():
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
            
            message = CTkMessagebox.CTkMessagebox(
                title="Clock",
                icon="warning",
                message="Alarm", 
                option_1="Stop",
            )
            
            if message.get() == 'Stop':
                pygame.mixer.music.stop()
            
            set_alarm_button.configure(state="normal")  # Enable the set alarm button
            hour_optionmenu.configure(state="normal")
            minute_optionmenu.configure(state="normal")
            am_pm_optionmenu.configure(state="normal")

            break


# Function to cancel the alarm
def cancel_alarm():
    global alarm_on
    alarm_on = False
    set_alarm_button.configure(state="normal")  # Enable the set alarm button


# Create set alarm button
set_alarm_button = customtkinter.CTkButton(
    alarm_clock_frame,
    text="Set Alarm", 
    command=threading,
)
set_alarm_button.grid(row=3, column=0, padx=10, pady=15)

# Create cancel alarm button
cancel_alarm_button = customtkinter.CTkButton(
    alarm_clock_frame, 
    text="Cancel Alarm", 
    command=cancel_alarm,
)
cancel_alarm_button.grid(row=3, column=1, padx=10, pady=15)

# Start the main loop
root.mainloop()
