import tkinter as tk
from tkinter import filedialog

def create_frame(master, **kwargs):
    frame = tk.Frame(master, **kwargs)
    frame.pack(**kwargs)
    return frame

def create_button(master, text, command, **kwargs):
    button = tk.Button(master, text=text, command=command, **kwargs)
    button.pack(**kwargs)
    return button

def create_label(master, text, **kwargs):
    label = tk.Label(master, text=text, **kwargs)
    label.pack(**kwargs)
    return label

def create_entry(master, **kwargs):
    entry = tk.Entry(master, **kwargs)
    entry.pack(**kwargs)
    return entry

def get_file_name():
    file_name = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    if file_name:
        label['text'] = file_name
    else:
        label['text'] = "No file selected"

root = tk.Tk()

frame = create_frame(root, fill="both")

label = create_label(frame, text="Select a file:", foreground="steelblue")
entry = create_entry(frame)

button = create_button(frame, text="Browse", command=get_file_name)
button = create_button(frame, text="Quit", command=root.quit)

root.mainloop()