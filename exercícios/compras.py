compras = []

contador = 0

print("Adicione 3 itens à sua lista de compras.")

while contador < 3:
    item = input(f"Digite o item {contador + 1}: ")
    compras.append(item)
    contador += 1

print("\nLista de compras atual:")
print(compras)

remover = input("\nDigite o nome de um item que você deseja remover da lista: ")

try:
    compras.remove(remover)
    print(f"\nO item '{remover}' foi removido com sucesso.")
except:
    print(f"\nO item '{remover}' não está na lista, por isso não pôde ser removido.")

print("\nSua lista de compras final:")
print(compras)
