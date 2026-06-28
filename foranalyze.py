import tkinter as tk
from tkinter import Label
root = tk.Tk()
root.title("This is Analysis Tool")
root.configure(bg="black")
root.geometry('800x400')

intro = tk.Label(
    root,
    text="Analyzer",
    font=("Arial", 24),
    fg="blue",
    bg = "light blue"
)
intro.pack()
root.mainloop()