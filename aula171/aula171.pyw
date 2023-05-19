import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

label = ttk.Label(root, text="este é um label", background="yellow", foreground="red")
label.pack()

root.mainloop()