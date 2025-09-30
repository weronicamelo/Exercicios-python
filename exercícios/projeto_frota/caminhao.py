from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.__capacidade_carga = capacidade_carga

    def ligar(self):
        print("Caminhão pesado em movimento!")

    def exibir_info(self):
        super().exibir_info()
        print(f"Capacidade de carga: {self.__capacidade_carga}")

    def get_capacidade_carga(self):
        return self.__capacidade_carga

    def set_capacidade_carga(self, capacidade_carga):
        self.__capacidade_carga = capacidade_carga

