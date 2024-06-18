import tkinter as tk
from tkinter import filedialog, messagebox
import os
import image_converter
def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry.delete(0, tk.END)
        entry.insert(0, directory)

def convert_files():
    directory = entry.get()
    if not os.path.isdir(directory):
        messagebox.showerror("Error", "Invalid directory. Please select a valid directory.")
        return

    image_converter.convert_image(directory)
    messagebox.showinfo("Info", "Files have been converted.")

# Create the main window
root = tk.Tk()
root.title("HEIC to JPG Converter")

# Create and place the widgets
label = tk.Label(root, text="Select the directory containing HEIC files:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_files)
convert_button.pack(pady=20)

# Run the main event loop
root.mainloop()
