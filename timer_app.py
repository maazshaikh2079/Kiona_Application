import customtkinter
import CTkMessagebox
import time
import pygame
from threading import Thread

# Set the appearance mode and color theme
customtkinter.set_appearance_mode("dark")  # Other options: "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Other color themes are available

# Flag to control the timer thread
timer_on = False
pygame.mixer.init()

# Initialize the main application window
root = customtkinter.CTk()
root.title("Timer App")
root.geometry("400x250")

timer_frame = customtkinter.CTkFrame(
    root,
    width=400,
    height=350,
    # fg_color="transparent",
    # bg_color="transparent",
)
timer_frame.pack(pady=30)

# Create time selection labels and optionmenus for the timer duration
hours_label = customtkinter.CTkLabel(
    timer_frame, 
    text="Hours",
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
hours_label.grid(row=0, column=0, padx=10, pady=5)
hours_optionmenu = customtkinter.CTkOptionMenu(
    timer_frame, 
    values=[f"{i:02d}" for i in range(24)], 
    anchor="center",
)
hours_optionmenu.grid(row=0, column=1, padx=10, pady=5)

minutes_label = customtkinter.CTkLabel(
    timer_frame, 
    text="Minutes",
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
minutes_label.grid(row=1, column=0, padx=10, pady=5)
minutes_optionmenu = customtkinter.CTkOptionMenu(
    timer_frame, 
    values=[f"{i:02d}" for i in range(60)],
    anchor="center",
)
minutes_optionmenu.grid(row=1, column=1, padx=10, pady=5)

seconds_label = customtkinter.CTkLabel(
    timer_frame, 
    text="Seconds",
    fg_color="lightblue",
    width=140,
    corner_radius=6,
)
seconds_label.grid(row=2, column=0,  padx=10, pady=5)
seconds_optionmenu = customtkinter.CTkOptionMenu(
    timer_frame, 
    values=[f"{i:02d}" for i in range(60)], 
    anchor="center",
)
seconds_optionmenu.grid(row=2, column=1, padx=10, pady=5)

# Function to run the timer in a separate thread
def start_timer():
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

        message = CTkMessagebox.CTkMessagebox(
            title="Clock", 
            message="Timer ended", 
            option_1="Stop"
        )
        
        if message.get() == 'Stop':
            pygame.mixer.music.stop()
        
        start_timer_button.configure(state="normal")  # Enable the start button
        hours_optionmenu.configure(state="normal")
        minutes_optionmenu.configure(state="normal")
        seconds_optionmenu.configure(state="normal")


# Function to stop the timer
def stop_timer():
    global timer_on
    timer_on = False
    start_timer_button.configure(state="normal")  # Enable the start button


# Create start timer button
start_timer_button = customtkinter.CTkButton(
    timer_frame, 
    text="Start Timer", 
    command=start_timer,
)
start_timer_button.grid(row=3, column=0, padx=10, pady=15)

# Create stop timer button
stop_timer_button = customtkinter.CTkButton(
    timer_frame, 
    text="Stop Timer", 
    command=stop_timer,
)
stop_timer_button.grid(row=3, column=1, padx=10, pady=15)

# Start the main loop
root.mainloop()
