# init é o método inicializador da classe
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def dizer_oi(self):
        print(f"Oi, meu nome é {self.nome}")

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

print(pessoa1.nome)
pessoa1.nome = "José"

pessoa1.dizer_oi()