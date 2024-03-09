import customtkinter
import cv2
from PIL import Image, ImageTk
import os
import time

class SelfieApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Selfie Application")

        self.video_capture = cv2.VideoCapture(0)
        self.is_capturing = False  # Flag to control video capturing

        self.current_image = None

        self.canvas = customtkinter.CTkCanvas(window, width=845, height=600)
        self.canvas.pack()

        # Button Frame
        self.button_frame = customtkinter.CTkFrame(window)
        self.button_frame.pack(fill=customtkinter.X, pady=10)

        # Buttons
        self.start_button = customtkinter.CTkButton(
            self.button_frame, 
            text="Start Capture", 
            command=self.start_capture
        )
        self.start_button.pack(side=customtkinter.LEFT, padx=10)

        self.hold_button = customtkinter.CTkButton(
            self.button_frame, text="Hold", command=self.hold_capture
        )
        self.hold_button.pack(side=customtkinter.LEFT, padx=10)

        self.capture_button = customtkinter.CTkButton(
            self.button_frame, text="Capture Image", command=self.capture_image
        )
        self.capture_button.pack(side=customtkinter.LEFT, padx=10)

        self.stop_button = customtkinter.CTkButton(
            self.button_frame, 
            text="Stop and Clear", 
            command=self.stop_and_clear
        )
        self.stop_button.pack(side=customtkinter.LEFT, padx=10)

        self.close_button = customtkinter.CTkButton(
            self.button_frame, 
            text="Close Program", 
            command=self.close_program
        )
        self.close_button.pack(side=customtkinter.LEFT, padx=10)


    def start_capture(self):
        self.is_capturing = True
        self.update_webcam()


    def hold_capture(self):
        self.is_capturing = False


    def capture_image(self):
        if self.is_capturing and self.current_image:
            # if not os.path.exists('Visitor_Pictures'):
            #     os.makedirs('Visitor_Pictures')
            self.current_image.save(f'Visitor_Pictures/selfie_{int(time.time())}.jpg')


    def stop_and_clear(self):
        self.is_capturing = False
        self.canvas.delete("all")  # Clear the canvas


    def close_program(self):
        self.video_capture.release()  # Release the webcam
        self.window.destroy()


    def update_webcam(self):
        if self.is_capturing:
            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.resize(frame, (845, 600))
                self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                self.photo = ImageTk.PhotoImage(image=self.current_image)
                self.canvas.create_image(0, 0, image=self.photo, anchor=customtkinter.NW)
                self.canvas.image = self.photo
                self.window.after(15, self.update_webcam)
            else:
                print("Failed to capture frame from webcam. Check webcam index.")


root = customtkinter.CTk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
app = SelfieApp(root)
root.mainloop()
