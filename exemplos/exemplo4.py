idade = int(input("Digite sua idade: "))

if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

#o f indica para a função print que quando tem uma variável para exibir dentro das chaves
print(f"Você é classificado como: {categoria}")