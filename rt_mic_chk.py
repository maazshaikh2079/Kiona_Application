import os

def record_microphone_test():
    duration = input("Enter duration (in seconds) for microphone test: ")
    command = f"arecord --format=S16_LE --duration={duration} --rate=16000 --file-type=raw out.raw"
    os.system(command)

def play_recorded_file():
    command = "aplay --format=S16_LE --rate=16000 out.raw"
    os.system(command)

def main():
    while True:
        print("\nMenu:")
        print("1. Record for microphone test")
        print("2. Play the recorded file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            record_microphone_test()
        elif choice == "2":
            play_recorded_file()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()