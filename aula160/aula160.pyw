import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

tk.Label(root, text="Label classico").pack()
ttk.Label(root, text="Label Temático").pack()

tk.Button(root, text="botao classico").pack()
ttk.Button(root, text="botao Temático").pack()

root.mainloop()
