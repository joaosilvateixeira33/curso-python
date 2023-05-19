import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

label = ttk.Label(
    root, 
    text="Este é um label\nCurso de Python Tkinter", 
  # font="Arial 24 bold"
    font=("Verdana", 24, "italic")
)
label.pack()

root.mainloop()