class Pessoa:
    def __init__(meuObjeto, nome, idade) -> None:
       meuObjeto.nome = nome
       meuObjeto.idade = idade
    
    def myFunc(abc):
        print("Ola meu nome é " + abc.nome)

p1 = Pessoa("Danny", 35)
p1.myFunc()
