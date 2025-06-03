# mais_vendidos = {"tech": "IPhone", "lazer": "Bola de futebol", "livro": "O Python"}

# tech = mais_vendidos["tech"]
# print(mais_vendidos.get("tech"))


# ---------------------------------------

# vendas_vendedores = {}
# vendas_vendedores["José"] = 100
# print(vendas_vendedores)

# vendas_vendedores.update({"José": 150, "Gabriel": 20})
# print(vendas_vendedores)

# #Para exluir um item da lista
# del vendas_vendedores["José"]
# print(vendas_vendedores)

# #Outra maneira de excluir um item
# jose = vendas_vendedores.pop("José")
# print(vendas_vendedores)
# print(jose)

# #Apaga o dicionario inteiro
# vendas_vendedores.clear()
# print(vendas_vendedores)


# ---------------------------------------

# vendas = {"janeiro": 1000, "fevereiro": 2000, "março": 3000}

# for chave in vendas:
#     print(f"No mês {chave} vendemos {vendas[chave]} unidades.")


# ---------------------------------------
    
# vendas = {"janeiro": 1000, "fevereiro": 2000, "março": 3000}

# for mes, venda in vendas.items():
#     print(f"{mes}: {venda} unidades.")


# ---------------------------------------

#listas que vão conter todas as chaves e valores
vendas = {"janeiro": 1000, "fevereiro": 2000, "março": 3000}

print(vendas.keys())
print(vendas.values())
