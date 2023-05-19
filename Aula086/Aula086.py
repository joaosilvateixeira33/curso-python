class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
    def nomeCompleto(self):
        print(self.nome, self.sobrenome)

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome):
        # Pessoa.__init__(self, nome, sobrenome)
        super().__init__(nome, sobrenome)

p1 = Estudante("Gabriel", "Artigas")
p1.nomeCompleto()
