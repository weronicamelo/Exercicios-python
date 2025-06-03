idade = int(input("Informe sua idade: "))

doenca = input("Possui alguma doença pré-existente? (s/n): ")

if idade < 18:
    if doenca == "s":
        mensalidade = 150
    if doenca == "n":
        mensalidade = 100

if idade >= 18:
    if idade <= 59:
        if doenca == "s":
            mensalidade = 250
        if doenca == "n":
            mensalidade = 200
    if idade >= 60:
        if doenca == "s":
            mensalidade = 350
        if doenca == "n":
            mensalidade = 300

print("Valor da mensalidade do plano de saúde: R$", mensalidade)

