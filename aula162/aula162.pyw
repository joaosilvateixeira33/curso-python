import tkinter as tk
from tkinter import ttk

def botao_clicado():
    lbl1.config(text="Botao clicado", background="blue", foreground="white")
    root.config(background="blue")

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

ttk.Button(root, text="Clique me!", command=botao_clicado).pack()
lbl1= ttk.Label(root, text=None)
lbl1.pack()

root.mainloop()
