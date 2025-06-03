# produtos = ["tv", "celular", "notebook"]
# vendas = [1500, 2000, 3000]

# i = produtos.index("celular")

# print("O valor de i é: ",i)
# print("O produto da posição i é: ", produtos[i])

# print("As vendas de {} foram de {} unidades.".format(produtos[1], vendas[1]))


# ---------------------------------------

# produtos = ["tv", "celular", "notebook"]
# vendas = [1500, 2000, 3000]

# produto = input("Digite o nome de um produto: ").lower()

# if produto in produtos: 
#     i = produtos.index(produto)
#     qtd_vendas = vendas[i]
#     print("Foram realizadas {} vendas de {}".format(qtd_vendas, produto))
# else:
#     print("Não existe vendas para {}.".format(produto))


# ---------------------------------------

# produtos = ["tv", "celular", "notebook"]
# vendas = [1500, 2000, 3000]

#Adicionar item na lista
# produtos.append("monitor")
# print(produtos)

#Remover item da lista
# produtos.remove("celular")
# print(produtos)


# ---------------------------------------

# produtos = ["tv", "celular", "notebook", "monitor"]
# vendas = [1500, 2000, 3000]

# #Alternativa para remover item da lista
# auxiliar = produtos.pop(1)
# print(auxiliar)
# print(produtos)


# ---------------------------------------

produtos = ["tv", "celular", "notebook", "monitor"]
vendas = [1500, 2000, 3000]

print("Os produtos são: ",produtos)
item_usuario = input("Qual item deseja remover: ")

try:
    produtos.remove(item_usuario)
    print("O produto {} foi excluído com sucesso.".format(item_usuario))
    print(produtos)
except:
    print("O produto {} não existe na lista.".format(item_usuario))
