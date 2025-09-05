import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Simple Clock")

# Create a label to show the time
label = tk.Label(root, font=("Arial", 30), bg="black", fg="white")
label.pack(pady=20)

# Function to update the time every second
def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # Get current time
    label.config(text=current_time)  # Show it on the label
    root.after(1000, update_time)  # Call this function again after 1 second

# Start the clock
update_time()

# Keep the window running
root.mainloop()
