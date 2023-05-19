import tkinter as tk

janela_base = tk.Tk()

janela_base.title("Minha aplicação GUI")

titulo_janela = janela_base.title()
lbl = tk.Label(janela_base, text=titulo_janela)
lbl.pack()

janela_base.mainloop()