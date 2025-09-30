from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.__num_portas = num_portas

    def ligar(self):
        print("Carro ligado!")

    def exibir_info(self):
        super().exibir_info()
        print(f"Número de Portas: {self.__num_portas}")

    def get_num_portas(self):
        return self.__num_portas

    def set_num_portas(self, num_portas):
       self.__num_portas = num_portas
