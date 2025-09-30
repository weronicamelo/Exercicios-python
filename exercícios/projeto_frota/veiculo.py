import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def ligar(self):
        print("Veículo está ligado!")

    def exibir_info(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Ano: {self.__ano}")

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano


