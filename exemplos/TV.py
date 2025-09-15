import os

class TV():

    def __init__(self, cor, tamanho):
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "SBT"
        self.volume = 30
        self.modelo = "Smart TV 8K"

    cor = "Preta"
    tamanho = 80
    canal = 4
    volume = 30
    modelo = "Smart TV 8K"

    def mudar_canal(self, canal ):
        self.canal = canal

    def mudar_volume(self):
        self.volume = volume

    def ligar_desligar(self):
        self.ligada = not self.ligada

    # def ligar_desligar(self):
    #     if self.ligada:
    #         self.ligada = False
    #
    #     else:
    #         self.ligada = True

minhaTV = TV("preta", "55")

def menu():
    while True:
        print("\nSua TV")
        print("Canal atual: ", minhaTV.canal)
        print("Volume atual: ", minhaTV.volume)
        print("Estado Atual: ", minhaTV.ligada)

        print("\n1. Mudar Canal")
        print("2. Mudar Volume")
        print("3. Ligar/Desligar")
        print("4. Sair")

        opcao = int(input("Digite sua opcao: "))
        os.system('cls')

        if opcao == 1:
            if minhaTV.ligada:
                canal = input("Digite o canal da TV: ")
                minhaTV.mudar_canal(canal)
            else:
                print("Ação indisponível, ligue a TV para executtá-la")
        elif opcao == 2:
            if minhaTV.ligada:
                volume = int(input("Digite o volume da TV: "))
                minhaTV.mudar_canal(volume)
            else:
                print("Ação indisponível, ligue a TV para executtá-la")
        elif opcao == 3:
            minhaTV.ligar_desligar()
            if minhaTV.ligada:
                print("\nTV ligada com sucesso!")
            else:
                print("\nTV desligada com sucesso!")
        elif opcao == 4:
            print("\nSaindo...")
            break
        else:
            print("Opcao invalida, digite novamente!")

menu()




