nome1 = input("Digite o 1º nome: ")
nome2 = input("Digite o 2º nome: ")
nome3 = input("Digite o 3º nome: ")
nome4 = input("Digite o 4º nome: ")
nome5 = input("Digite o 5º nome: ")

nomes = [nome1, nome2, nome3, nome4, nome5]

print("\nOs nomes que começam com a letra 'A':")
for nome in nomes:
    if nome.lower().startswith('a'):
        print(nome)
