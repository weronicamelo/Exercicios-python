
idade = int(input("Digite sua idade: "))

if idade < 18:
    classificado = "Menor de idade!"
elif idade >= 18 and idade <= 59:
    classificado = "Adulto"
elif idade >= 60:
    classificado = "Idoso"
else: 
    classificado = "Inválido"

print(f"Você é classificado como: {classificado}")