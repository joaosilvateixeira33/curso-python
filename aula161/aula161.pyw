import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

# usando construtor
ttk.Label(root, text="Olá, mundo!").pack()

# usando dicionario
lbl1= ttk.Label(root)
lbl1["text"] = "Outro Olá, mundo"
lbl1.pack()

# usando método config
lbl2 = ttk.Label(root)
lbl2.config(text="Mais um olá, mundo")
lbl2.pack()

root.mainloop()
