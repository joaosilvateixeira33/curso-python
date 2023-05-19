import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

btn1 = ttk.Button(
    root, 
    text="sair Lambda",
    command=lambda: root.quit()
)

btn1.state(["!disabled"])
btn1.pack()

root.mainloop()