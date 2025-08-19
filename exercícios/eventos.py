eventos = []

def cadastrar_evento():
    nome_evento = input("Digite o nome do evento: ")
    cidade = input("Digite a cidade: ")
    local = input("Digite o local: ") 
    categoria = input("Digite qual é a categoria do evento: ")

    evento = {
        'nome': nome_evento,
        'cidade' : cidade,
        'local' : local,
        'categoria' : categoria
    }

    eventos.append(evento)

def menu():
    while True:
        print("\n --- Menu ---")
        print("1 - Cadastrar evento")
        print("2 - Consultar evento por cidade")
        print("3 - Consultar evento por local")
        print("4 - Consultar evento por categoria")
        print("5 - Mostrar os eventos")
        print("6 - Alterar evento")
        print("7 - Excluir evento")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            consulta_cidade()
        elif opcao == "3":
            consulta_local()
        elif opcao == "4":
            consulta_categoria()
        elif opcao == "5":
            mostrar_eventos()
        elif opcao == "6":
            alterar_evento()
        elif opcao == "7":
            excluir_evento()
        elif opcao == "8":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.") 

def consulta_categoria():
    consulta_categoria = ("Digite a categoria que deseja consultar: ")

    busca_eventos = []
    for evento in eventos:
        if consulta_categoria in evento['categoria']:
            busca_eventos.append(evento)
    
    if busca_eventos:
        for evento in busca_eventos:
            print(f"Nome: {evento['nome']} \nLocal: {evento['local']} \nCategoria: {evento['categoria']} \nCidade: {evento['cidade']}")

def consulta_cidade():
    consulta_cidade = input("Digite a cidade: ")

    busca_eventos = []
    for evento in eventos:
        if consulta_cidade in evento['cidade']:
            busca_eventos.append(evento)
    
    if busca_eventos:
        for evento in busca_eventos:
            print(f"Nome: {evento['nome']} \nLocal: {evento['local']} \nCategoria: {evento['categoria']} \nCidade: {evento['cidade']}")
    else:
        print("Não existe nenhum evento cadastrado nessa cidade!")

def consulta_local():
    consulta_local = input("Digite o local: ")

    busca_eventos = []
    for evento in eventos:
        if consulta_local in evento['local']:
            busca_eventos.append(evento)
    
    if busca_eventos:
        for evento in busca_eventos:
            print(f"Nome: {evento['nome']}, Local: {evento['local']}, Categoria: {evento['categoria']}, Cidade: {evento['cidade']}")
    else:
        print("Não existe nenhum evento cadastrado nesse local!")

def mostrar_eventos():
    if eventos:
        print("\nLista de todos os eventos cadastrados")
        for evento in eventos:
            print(f"Nome: {evento['nome']} \nLocal: {evento['local']} \nCategoria: {evento['categoria']} \nCidade: {evento['cidade']}")
    else:
        print("Não existe nenhum evento cadastrado!")

def alterar_evento():
    nome_evento = input("Digite o nome do evento que deseja alterar: ")

    evento_encontrado = False
    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower():
            evento_encontrado = True
            print(f"Evento encontrado: {evento['nome']}")
            
            print("\nO que você deseja alterar?")
            print("1 - Cidade")
            print("2 - Local")
            print("3 - Categoria")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nova_cidade = input(f"Nova cidade (atualmente {evento['cidade']}): ")
                evento['cidade'] = nova_cidade if nova_cidade else evento['cidade']
            elif escolha == "2":
                novo_local = input(f"Novo local (atualmente {evento['local']}): ")
                evento['local'] = novo_local if novo_local else evento['local']
            elif escolha == "3":
                nova_categoria = input(f"Nova categoria (atualmente {evento['categoria']}): ")
                evento['categoria'] = nova_categoria if nova_categoria else evento['categoria']
            else:
                print("Opção inválida. Nenhuma alteração foi feita.")
                break

            print("Evento alterado com sucesso!")
            break

    if not evento_encontrado:
        print("Evento não encontrado.")


def excluir_evento():
    nome_evento = input("Digite o nome do evento que deseja excluir: ")

    evento_encontrado = False
    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower():
            evento_encontrado = True
            eventos.remove(evento)
            print(f"Evento '{nome_evento}' excluído com sucesso!")
            break

    if not evento_encontrado:
        print("Evento não encontrado.")

menu()