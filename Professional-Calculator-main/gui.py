import tkinter as tk
from calculator_logic import calculate

def run_calculator():
    def on_click(event):
        if event.widget["text"] == "=":
            result = calculate(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif event.widget["text"] == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, event.widget["text"])

    root = tk.Tk()
    root.title("Professional Calculator")

    entry = tk.Entry(root, font="Arial 20")
    entry.pack(fill="both", ipadx=8, ipady=8)

    button_texts = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C", "(", ")", "**"]
    ]

    for row in button_texts:
        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both")
        for char in row:
            btn = tk.Button(frame, text=char, font="Arial 18", height=2, width=4)
            btn.pack(side="left", expand=True, fill="both")
            btn.bind("<Button-1>", on_click)

    root.mainloop()
