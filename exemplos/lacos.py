# -------- For -------
# for i in range(5):
#     print(i)

# print(range(10))

# ---------------------------------------

# alunos = []
# notas = []

# for i in range(3):
#     nome = input(f"Digite o nome do {i+1}º aluno: ")
#     alunos.append(nome)
#     nota = float(input(f"Digite a nota do {i+1}º aluno: "))
#     notas.append(nota)

# print(alunos, notas)

# ---------------------------------------

# produtos = ["coca", "pepsi", "guaraná"]
# producao = [15000, 10000, 14000]

# tamanho = len(produtos)

# for i in range(tamanho):
#     print(f"A produção de {produtos[i]} é de {producao[i]}")

# ---------------------------------------

# produtos = ["coca", "pepsi", "guaraná"]
# producao = [15000, 10000, 14000]

# tamanho = len(produtos)

# for produto in produtos:
#     print(f"Produção de {produto}")

# ---------------------------------------

# produtos = ["coca", "pepsi", "guaraná"]
# producao = [15000, 10000, 14000]

# tamanho = len(produtos)

# for produto in produtos:
#     i = produtos.index(produto)
#     print(f"Produção de {produto} é {producao[i]}")

# ---------------------------------------

# vendas = [50, 100, 200, 300, 400, 500]
# meta = 300
# qtd__bateu_meta = 0

# for venda in vendas:
#     if venda >= meta:
#         qtd__bateu_meta += 1
        
# qtd_funcionarios = len(vendas)
# print("O percentual de funcionarios que bateram a meta foi de {:.1%}".format(qtd__bateu_meta/qtd_funcionarios))

# ---------------------------------------

# funcionarios = ["Maria", "João", "Pedro", "José"]
# for i, funcionario in enumerate(funcionarios):
#     print(f"O index {i} é o funcionário {funcionario}")

# ---------------------------------------

# estoque = [1500, 350, 200, 50, 870]
# produtos = ["coca", "pepsi", "dolly", "café", "guaraná"]
# nivel_minimo = 300

# for i, qtd in enumerate(estoque):
#     if qtd < nivel_minimo:
#         print(f"O produto {produtos[i]} está com o nível baixo: {qtd} unidades.")

# ---------------------------------------

# ------ While -------
# venda = input("Digite o nome do produto e tecle enter para registrar Para cancelar, tecla enter sem digitar nada.")
# vendas = []

# while venda != "":
#     vendas.append(venda)
#     venda = input("Digite o nome do produto e tecle enter para registrar Para cancelar, tecla enter sem digitar nada.")

# print(f"Registros finalizaodos. As vendas forma: {vendas}")

# ---------------------------------------

# while True:
#     print("Isso vai ser executado pelo menos uma vez.")

#     resposta = input("Deseja continuarr? (s/n): ").lower()

#     if reposta != "s":
#         break

# ---------------------------------------

# --------- Match case --------
while True:
    dia = int(input("Digite o número do dia da semana (1-7): "))

    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3: 
            print("Terça-Feira")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case 6:
            print("Sexta-Feira")
        case 7:
            print("Sábado")
        case _:
            print("Valor inválido!")
