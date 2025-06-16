def verificar_disponibilidade(reservas, sala, horario):
    for reserva in reservas:
        if reserva[0] == sala and reserva[1] == horario:
            return "Sala não está disponível!"
    return "Sala está disponível!"

def adicionar_reserva(reservas, sala, horario):
    mensagem = verificar_disponibilidade(reservas, sala, horario)
    if mensagem == "Sala está disponível!":
        reservas.append((sala, horario))
        print(f"Reserva confirmada para a sala {sala} às {horario}.")
    else:
        print(f"A {sala} já está reservada às {horario}.")

def menu():
    reservas = [("Sala 1", "14h"), ("Sala 2", "15h"), ("Sala 3", "16h")]

    escolha = ""
    while escolha != "3":
        print("\nReservas: ", reservas)
        print("\n--- Menu de Reservas ---")
        print("1 - Verificar disponibilidade")
        print("2 - Adicionar reserva")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            sala = input("Digite o nome da sala: ")
            horario = input("Digite o horário: ")
            print(verificar_disponibilidade(reservas, sala, horario))

        elif escolha == "2":
            sala = input("Digite o nome da sala: ")
            horario = input("Digite o horário: ")
            adicionar_reserva(reservas, sala, horario)

        elif escolha == "3":
            print("Saindo do sistema de reservas!")

        else:
            print("Opção inválida!")

menu()
