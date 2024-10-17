# Filename: auto_clicker.py

import pyautogui
import time
import threading
import keyboard

# Function for auto-clicking
def clicker(interval):
    while not stop_event.is_set():
        pyautogui.click()  # Perform a mouse click
        time.sleep(interval)  # Wait for the specified interval

# Start/stop control with a hotkey-
def start_clicking(interval):
    global stop_event
    stop_event = threading.Event()  # This event is used to stop the clicking thread
    thread = threading.Thread(target=clicker, args=(interval,))
    thread.start()  # Start the clicking thread

    # Wait for 's' key to stop
    print("Auto-clicker started. Press '=' to stop.")
    keyboard.wait('=')  # Stop when '=' is pressed
    stop_event.set()  # Signal the thread to stop
    thread.join()  # Wait for the thread to finish

if __name__ == "__main__":
    # User input: time interval between clicks
    interval = 0.01
    
    # Starting the auto-clicker with '-' and stop with '='
    print("Press '-' to start auto-clicking.")
    keyboard.wait('-')  # Wait until the space key is pressed
    start_clicking(interval)

    print("Auto-clicker stopped.")
#