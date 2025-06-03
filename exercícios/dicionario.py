estoque = {}

for i in range(5):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    estoque[nome] = quantidade

print("\nProdutos com menos de 5 unidades:")
for produto in estoque:
    if estoque[produto] < 5:
        print(produto, " - ", estoque[produto], "unidades")
