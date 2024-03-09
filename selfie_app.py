import customtkinter

import cv2
from PIL import Image, ImageTk
import os
import time

# customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

# Initialize the main window
root = customtkinter.CTk()
root.title("Selfie Application")

# Initialize video capture
video_capture = cv2.VideoCapture(0)
is_capturing = False  # Flag to control video capturing
current_image = None

video_stream_canvas = customtkinter.CTkCanvas(
    root,
    width=1065,
    height=802,
    bg="#d9d9d9",  # light mode
    # bg="#292929", # dark mode
)
video_stream_canvas.pack(padx=50, pady=70, side="left")

# Button Frame
button_frame = customtkinter.CTkFrame(root)
button_frame.pack(fill=customtkinter.X, pady=10)

# Function definitions
def start_capture():
    global is_capturing
    is_capturing = True
    update_webcam()


def hold_capture():
    global is_capturing
    is_capturing = False


def capture_image():
    if is_capturing and current_image:
        current_image.save(f'Visitor_Pictures/selfie_{int(time.time())}.jpg')


def stop_and_clear():
    global is_capturing
    is_capturing = False
    video_stream_canvas.delete("all")  # Clear the canvas


def close_program():
    video_capture.release()  
    root.destroy()


def update_webcam():
    global current_image
    if is_capturing:
        ret, video_frame = video_capture.read()
        if ret:
            video_frame = cv2.resize(video_frame, (1085, 802))
            
            current_image = Image.fromarray(cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image=current_image)
            video_stream_canvas.create_image(0, 0, image=photo, anchor=customtkinter.NW)
            video_stream_canvas.image = photo
            root.after(15, update_webcam)
        else:
            print("Failed to capture frame from webcam. Check webcam index.")

# Buttons
start_button = customtkinter.CTkButton(button_frame, text="Start Capture", command=start_capture)
start_button.pack(side=customtkinter.LEFT, padx=10)

hold_button = customtkinter.CTkButton(button_frame, text="Hold", command=hold_capture)
hold_button.pack(side=customtkinter.LEFT, padx=10)

capture_button = customtkinter.CTkButton(button_frame, text="Capture Image", command=capture_image)
capture_button.pack(side=customtkinter.LEFT, padx=10)

stop_button = customtkinter.CTkButton(button_frame, text="Stop and Clear", command=stop_and_clear)
stop_button.pack(side=customtkinter.LEFT, padx=10)

close_button = customtkinter.CTkButton(button_frame, text="Close Program", command=close_program)
close_button.pack(side=customtkinter.LEFT, padx=10)

# Set the root to full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Start the main loop
root.mainloop()
