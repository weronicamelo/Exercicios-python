class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} diz: Au au!")

class Gato(Animal):
    def falar(self):
        super().falar()
        print(f"{self.nome} diz: Miau!")

mel = Cachorro('Mel')
mel.falar()

mimo = Gato('Mimo')
mimo.falar()