class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

animais = [Animal(), Cachorro(), Gato()]

# marley = Cachorro()
# marley.falar()
#
# tom = Gato()
# tom.falar()
#
# joelinthon = Animal()
# joelinthon.falar()

for animal in animais:
    animal.falar()

