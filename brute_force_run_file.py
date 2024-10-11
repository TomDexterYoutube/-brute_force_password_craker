import pyautogui
import time
import os
import threading
import tkinter as tk
from tqdm import tqdm

delay = float(input("delay /"))

with tqdm(total=10, desc="Starting", unit="sec", unit_scale=True) as pbar:
    for _ in range(10):  # Iterate 10 times for 10 seconds.
        time.sleep(1)  # Sleep for one second.
        pbar.update(1)  # Update the progress bar by one unit.

# Global variable to control typing
is_paused = False
stop_typing = False

def toggle_pause():
    global is_paused
    is_paused = not is_paused
    pause_button.config(text="Resume" if is_paused else "Pause")

def stop_typing_simulation():
    global stop_typing
    stop_typing = True

def type_text(file_path):
    global is_paused, stop_typing

    # Get the size of the file in bytes for the progress bar
    file_size = os.path.getsize(file_path)

    # Set the pyautogui typewrite delay to 0 for maximum speed
    pyautogui.PAUSE = 0  # Disable the pause after each call

    # Open the file in read mode
    with open(file_path, "r", encoding='utf-8') as file:
        # Initialize progress bar with file size (in bytes)
        with tqdm(total=file_size, desc="Typing Progress", unit="B", unit_scale=True) as pbar:
            while True:
                if stop_typing:
                    break
                
                while is_paused:  # Wait while paused
                    time.sleep(delay)  # Sleep briefly to prevent high CPU usage

                # Read file in chunks (1 character at a time)
                char = file.read(1)  # Read one character
                if not char:  # Stop when end of file is reached
                    break

                # Use pyautogui to simulate typing
                if char == " ":
                    pyautogui.press("space")  # Simulate space key press
                elif char == "\n":
                    pyautogui.press("enter")  # Simulate enter key press
                else:
                    pyautogui.write(char)  # Use write for more complex characters

                # Update progress bar based on the number of bytes processed
                pbar.update(1)  # Increment by one byte (character)

                # Introduce a short delay to avoid overwhelming the input system
                time.sleep(0.000005)

    # Send an "Enter" key at the end to finalize input
    pyautogui.press("enter")

# Create the GUI window
root = tk.Tk()
root.title("Typing Simulator Control")

# Create Pause/Resume button
pause_button = tk.Button(root, text="Pause", command=toggle_pause)
pause_button.pack(pady=10)

# Create Stop button
stop_button = tk.Button(root, text="Stop", command=stop_typing_simulation)
stop_button.pack(pady=10)

# Start the typing simulation in a separate thread
file_path = "data.txt"
typing_thread = threading.Thread(target=type_text, args=(file_path,))
typing_thread.start()

# Start the GUI main loop
root.mainloop()
