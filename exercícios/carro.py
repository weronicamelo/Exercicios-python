class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.nivel_combustivel = 100
        self.farol = False

    def andar(self):
        if self.nivel_combustivel > 0:
            self.nivel_combustivel -= 2
            print("O carro está andando... ")
            if self.nivel_combustivel == 20:
                print("Atenção: Reserva do combustível!")
            elif self.nivel_combustivel == 0:
                print("O combustível acabou!")
        else:
            print("Não tem combustível suficiente!")
        carro1.menu_carro()

    def buzinar(self):
        print("Carro buzinado!")
        carro1.menu_carro()

    def ligar_farol(self):
        if self.farol == False:
            self.farol = True
            print("O farol do carro está ligado!")
        else:
            self.farol = False
            print("O farol do carro está desligado!")
        carro1.menu_carro()

    def menu_carro(self):
        print("\n----- Informações sobre o veículo -----")
        print(f"Cor: {self.cor}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Nível combustível: {self.nivel_combustivel}")

        if self.farol:
            print("Estado do farol: Ligado")
        else:
            print("Estado do farol: Desligado")

    def menu_acoes(self):
        print("----- Menu de ações do veículo -----")
        print("1 - Andar")
        print("2 - Buzinar")
        print("3 - Ligar Farol/Desligar Farol")
        print("4 - Sair")

        while True:
            try:
                opcao = input("Escolha uma das opções: ")
                if opcao == "1":
                    self.andar()
                elif opcao == "2":
                    self.buzinar()
                elif opcao == "3":
                    self.ligar_farol()
                elif opcao == "4":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("A opção não existe no menu de opções!")

carro1 = Carro("Vermelho", "Fiat", "Argo")
carro1.menu_carro()
carro1.menu_acoes()
