from tkinter import *
import tkinter

"""
Widget Template:
    w = Label(root, text='GeeksForGeeks.org!')\
    w.grid(padx=(padding from left side, padding from right side),
           pady=(padding from top, padding from bottom))
    w.pack()
"""
import tkinter as tk
from tkinter import messagebox

class DisplayFunctions:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Math Trials')
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        # Initialize a container for dynamic content
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

    def widgetDestroy(self):
        # Destroy all widgets in the container
        for widget in self.container.winfo_children():
            widget.destroy()

    def textDisplay(self, text, size="header1", top_pady=10, bottom_pady=10):
        if size == "header1":
            text_size = 25 
        elif size == "header2":
            text_size = 15 
        else:
            text_size = 12    
        
        label = tk.Label(self.container, text=text, font=("Arial", text_size))
        label.pack(pady=(top_pady, bottom_pady))

    def buttonMake(self, name, command, color="#ffffff", size="header2", height=2, width=20, top_pady=5, bottom_pady=5):
        if size == "header1":
            text_size = 25 
        elif size == "header2":
            text_size = 15 
        else:
            text_size = 12

        button = tk.Button(
            self.container, 
            text=name, 
            bg=color, 
            font=("Arial", text_size), 
            width=width, 
            height=height, 
            command=command
        )
        button.pack(pady=(top_pady, bottom_pady))
        return button

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def TkRun(self):
        self.root.mainloop()