from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.__cilindradas = cilindradas

    def ligar(self):
        print("Moto roncando!")

    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindradas: {self.__cilindradas}")

    def get_cilindradas(self):
        return self.__cilindradas

    def set_cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas