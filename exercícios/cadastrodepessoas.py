pessoas = []

print("\n------ Cadastro de Pessoas ------")

for i in range(3):
    print(f"\nCadastro da {i + 1}ª pessoa")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = {"nome": nome, "idade": idade}

    pessoas.append(pessoa)

print("\nPessoas com mais de 18 anos:")
for pessoa in pessoas:
    if pessoa["idade"] > 18:
        print(pessoa["nome"])
