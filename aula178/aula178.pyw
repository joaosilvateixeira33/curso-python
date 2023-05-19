import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

def executar():
    root.quit()

btn1 = ttk.Button(
    root, 
    text="sair",
    command=executar
)
btn1.pack()

btn2 = ttk.Button(
    root, 
    text="sair Lambda",
    command=lambda: root.quit()
)
btn2.pack()

root.mainloop()