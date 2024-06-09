import tkinter as tk

ctrl_b_pressed = False
ctrl_f_pressed = False

# Create the main window
root = tk.Tk()
root.title("Key Press Detector")
root.geometry("400x200")

# Create a label to display the status
status_label = tk.Label(root, text="Not pressed", font=("Arial", 16))
status_label.pack(pady=50)

def on_ctrl_b_press(event):
    global ctrl_b_pressed
    ctrl_b_pressed = True

def on_ctrl_b_release(event):
    global ctrl_b_pressed
    ctrl_b_pressed = False

def on_ctrl_f_press(event):
    global ctrl_f_pressed
    ctrl_f_pressed = True

def on_ctrl_f_release(event):
    global ctrl_f_pressed
    ctrl_f_pressed = False

def update_status():
    global ctrl_b_pressed, ctrl_f_pressed

    if ctrl_b_pressed:
        print("Ctrl+B Pressed")
    else:
        print("Ctrl+B Not Pressed")

    if ctrl_f_pressed:
        print("Ctrl+F Pressed")
    else:
        print("Ctrl+F Not Pressed")

    # Call this method again after 200ms
    root.after(200, update_status)

# Update the status periodically
update_status()

root.bind('<Control-b>', on_ctrl_b_press)
root.bind('<KeyRelease-b>', on_ctrl_b_release)
root.bind('<Control-f>', on_ctrl_f_press)
root.bind('<KeyRelease-f>', on_ctrl_f_release)

root.mainloop()
