nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia: {media:.2f}")

if media < 5:
    print("Situação: Reprovado!")
elif 5 <= media < 7:
    print("Situação: Recuperação!")
else:
    print("Situação: Aprovado!")
