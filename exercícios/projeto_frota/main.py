from carro import Carro
from moto import Moto
from caminhao import Caminhao

def adicionar_veiculo(frota):
    print("\nEscolha o tipo de veículo para adicionar:")
    print("1 - Carro")
    print("2 - Moto")
    print("3 - Caminhão")
    escolha = input("Digite a opção: ")

    try:
        if escolha == '1':
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano do carro: "))
            portas = int(input("Digite o número de portas do carro: "))
            novo_veiculo = Carro(marca, modelo, ano, portas)
            frota.append(novo_veiculo)
            print(f"Carro {modelo} adicionado com sucesso!")

        elif escolha == '2':
            marca = input("Digite a marca da moto: ")
            modelo = input("Digite o modelo da moto: ")
            ano = int(input("Digite o ano da moto: "))
            cilindrada = int(input("Digite a cilindrada da moto: "))
            nova_moto = Moto(marca, modelo, ano, cilindrada)
            frota.append(nova_moto)
            print(f"Moto {modelo} adicionada com sucesso!")

        elif escolha == '3':
            marca = input("Digite a marca do caminhão: ")
            modelo = input("Digite o modelo do caminhão: ")
            ano = int(input("Digite o ano do caminhão: "))
            capacidade = int(input("Digite a capacidade de carga do caminhão: "))
            novo_caminhao = Caminhao(marca, modelo, ano, capacidade)
            frota.append(novo_caminhao)
            print(f"Caminhão {modelo} adicionado com sucesso!")

        else:
            print("Opção inválida!")

    except ValueError:
        print("Por favor, digite um valor numérico válido para ano, portas ou cilindrada.")

def exibir_frota(frota):
    print("\n------Frota Atual------")
    if not frota:
        print("A frota está vazia!")
    else:
        for veiculo in frota:
            veiculo.exibir_info()
            print("\n")

def ligar_veiculos(frota):
    print("\nLigando os veículos...")
    if not frota:
        print("A frota está vazia! Não há veículos para ligar.")
    else:
        for veiculo in frota:
            veiculo.ligar()

def menu():
    frota = [
        Carro("Fusca", "Volkswagen", 1985, 4),
        Moto("CB 500", "Honda", 2020, 500),
        Caminhao("Scania", "R 450", 2018, 20)
    ]

    while True:
        print("\n------Menu------")
        print("1 - Adicionar Veículo")
        print("2 - Exibir Frota")
        print("3 - Ligar Veículos")
        print("4 - Sair")
        opcao = input("Digite a opção: ")

        if opcao == '1':
            adicionar_veiculo(frota)
        elif opcao == '2':
            exibir_frota(frota)
        elif opcao == '3':
            ligar_veiculos(frota)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente!.")

if __name__ == "__main__":
    menu()
