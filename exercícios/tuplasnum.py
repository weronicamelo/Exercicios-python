num_par = []
numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

print(f"\nVocê digitou os números: {numeros}")

print(f"O número 9 apareceu {numeros.count(9)} vez(es).")

numero = 0
while numero < 4:
    if numeros[numero] == 3:
        print(f"O número 3 apareceu na posição {numero+1}.")
        break
    numero += 1
else:
    print("O número 3 não foi digitado.")

for n in numeros:
    if n % 2 == 0:
        num_par.append(n)

if num_par == []:
    print("Nenhum número par foi digitado.")
else:
    print(f"Números pares digitados: {num_par}")
