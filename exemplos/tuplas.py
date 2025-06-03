# vendas = ("João", "01/01/2025",  "25/08/2002", 2000, "Estagiário")

# print(vendas)

# vendas = ("Maria")

# print(vendas)


# ---------------------------------------

# vendas = ("João", "01/01/2025",  "25/08/2002", 2000, "Estagiário")

# nome, data_admissao, data_nascimento, salario, cargo = vendas

# print(nome)
# print(data_admissao)
# print(data_nascimento)
# print(salario)
# print(cargo)

# print(vendas)


# ---------------------------------------

#enumerate gera uma tupla
# vendas = [100,200,300]
# funcionaios = ["João", "Maria", "José"]

# for i, item in enumerate(vendas):
#     print(item)


# ---------------------------------------

# vendas = [100,200,300]
# funcionaios = ["João", "Maria", "José"]

# for i, venda in enumerate(vendas):
#     print(f"O funcionário{funcionaios[i]} vendeu {venda}.)


# ---------------------------------------

#  -------- Exemplo prático ---------

vendas = [
    ("25/11/2024", "Galaxy S24 Ultra", "Preto", "256GB", 400, 7000),
    ("25/11/2024", "Galaxy S24 Ultra", "Rose", "256GB", 200, 7000),
    ("25/11/2024", "IPhone 15 Pro Max", "Preto", "256GB", 350, 9000),
    ("25/11/2024", "IPhone 15 Pro Max", "Preto", "512GB", 250, 14000),
    ("26/11/2024", "Galaxy S24 Ultra", "Preto", "256GB", 317, 7000),
    ("26/11/2024", "Galaxy S24 Ultra", "Rose", "256GB", 212, 7000),
    ("26/11/2024", "IPhone 15 Pro Max", "Preto", "256GB", 150, 9000),
    ("26/11/2024", "IPhone 15 Pro Max", "Preto", "512GB", 50, 14000)
]

faturamento = 0
qtd_mais_vendido = 0

for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item

    if data == "25/11/2024" and produto == "IPhone 15 Pro Max":
        faturamento += unidades_vendidas * valor_unitario

    if data == "26/11/2024":
        if unidades_vendidas > qtd_mais_vendido:
            produto_mais_vendido = produto
            qtd_mais_vendido = unidades_vendidas

print(f"O faturamento do IPhone no dia 25/11/2024 foi de R$ {faturamento:,}")
print(f"O produto mais vendido no dia {data} foi o {produto} com {qtd_mais_vendido} unidades.")

