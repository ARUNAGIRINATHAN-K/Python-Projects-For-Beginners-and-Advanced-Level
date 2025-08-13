import os
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
import PyPDF2

def count_words(text):
    return len(text.split())

def read_pdf(file_path):
    try:
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading PDF:\n{e}")
        return ""

def read_docx(file_path):
    try:
        text = ""
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading DOCX:\n{e}")
        return ""

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])
    if file_path:
        file_label.config(text=f"Selected File: {file_path}")
        if file_path.lower().endswith('.pdf'):
            content = read_pdf(file_path)
        elif file_path.lower().endswith('.docx'):
            content = read_docx(file_path)
        else:
            messagebox.showerror("Unsupported Format", "Please select a PDF or DOCX file.")
            return
        
        word_count = count_words(content)
        result_label.config(text=f"Word Count: {word_count}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Word Count from PDF/DOCX")
root.geometry("500x200")
root.resizable(False, False)

# Widgets
title_label = tk.Label(root, text="Word Counter", font=("Arial", 18))
title_label.pack(pady=10)

file_label = tk.Label(root, text="No file selected", wraplength=480)
file_label.pack()

browse_button = tk.Button(root, text="Browse File", command=browse_file)
browse_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
