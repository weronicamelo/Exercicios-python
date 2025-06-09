lista = []

for i in range(6):
    numero = float(input("Digite um número: "))
    lista.append(numero)

media = sum(lista) / 6

num_maior = 0
for n in lista:
    if n > media:
        num_maior += 1

maior = lista[0]
menor = lista[0]
for n in lista:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print("A média dos números é:", media)
print("Números que são maiores que a média:", num_maior)
print("Maior número:", maior)
print("Menor número:", menor)
