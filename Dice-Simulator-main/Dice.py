import tkinter as tk
import random
import time
from tkinter import messagebox

# Dice faces as unicode
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

roll_history = []

def roll_dice():
    roll_button.config(state=tk.DISABLED)
    dice_label.config(text="Rolling...")
    window.update()
    
    # Animation
    for _ in range(10):
        temp = random.randint(1, 6)
        dice_label.config(text=dice_faces[temp], font=("Helvetica", 100))
        window.update()
        time.sleep(0.1)

    result = random.randint(1, 6)
    dice_label.config(text=dice_faces[result], font=("Helvetica", 100))
    roll_history.append(result)
    history_listbox.insert(tk.END, f"Roll {len(roll_history)}: {result}")
    roll_button.config(state=tk.NORMAL)

def clear_history():
    roll_history.clear()
    history_listbox.delete(0, tk.END)

# Main window
window = tk.Tk()
window.title("Dice Simulator")
window.geometry("300x400")

dice_label = tk.Label(window, text="🎲", font=("Helvetica", 100))
dice_label.pack(pady=10)

roll_button = tk.Button(window, text="Roll Dice", font=("Helvetica", 14), command=roll_dice)
roll_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear History", command=clear_history)
clear_button.pack()

history_label = tk.Label(window, text="Roll History:")
history_label.pack()

history_listbox = tk.Listbox(window)
history_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

window.mainloop()
