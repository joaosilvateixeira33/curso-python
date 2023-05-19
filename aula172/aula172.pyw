import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

label = ttk.Label(
    root, 
    text="Este é um label\nCurso de Python Tkinter", 
    background="yellow", 
    foreground="red",
    padding=10,
    width=22,
    justify="left",
    anchor="n"
)
label.pack()

root.mainloop()