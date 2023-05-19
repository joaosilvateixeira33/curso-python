class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def myFunc(self):
        print(f"Olá, meu nome é {self.nome}")