import cv2

def find_camera_indices():
    num_devices = 10  # Maximum number of devices to check
    for i in range(num_devices):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            cap.release()
        else:
            print(f"No camera found at index {i}")

find_camera_indices()
