import tkinter as tk

janela_base = tk.Tk()

janela_base.title("Minha aplicação GUI")

# dimensoes da aplicação
largura_janela = 600
altura_janela = 500

# obter dimensoes de tela
largura_tela = janela_base.winfo_screenwidth()
altura_tela = janela_base.winfo_screenheight()

# Obter ponto central
centro_x = int(largura_tela / 2 - largura_janela / 2)
centro_y = int(altura_tela / 2 - altura_janela / 2)

# Posição da janela no centro da tela
janela_base.geometry(f"{largura_janela}x{altura_janela}+{centro_x}+{centro_y}")

janela_base.mainloop()