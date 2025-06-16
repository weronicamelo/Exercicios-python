# def calcular_media(nota1,nota2):
# #def calcular_media():
#     # nota1 = float(input("Digite a nota 1: "))
#     # nota2 = float(input("Digite a nota 2: "))
#     media = (nota1 + nota2)/2

#     return print(f"A média das notas é {media}")

# calcular_media(10,9)


# ---------------------------------------

# def operacoes_basicas(num1, num2):
#     soma = num1 + num2
#     diferenca = num1 - num2
#     mult = num1 * num2
#     divisao = num1 / num2
#     return(soma, diferenca, mult, divisao)

#     print(operacoes_basicas(10,2))


# ---------------------------------------

# def descobrir_servidor(email):
#     try:
#         posicao_a = email.index("@")
#     except:
#         raise ValueError("E-mail não possui @, digite novamente.")
#     else:
#         servidor = email[posicao_a:]
#         if "gmail" in servidor:
#             return "gmail"
#         elif "hotmail" in servidor or "outlook" in servidor:
#             servidor "outlook"
#         elif "yahoo" in servidor:
#             return "yahoo"
#         else:
#             return "Outro"

# email = input("Digite seu e-mail: ")
# print(descobrir_servidor(email))


# ---------------------------------------

# def calcular_media(*notas):
#     soma = 0
#     for nota in notas:
#         soma += nota
#         return soma / (len(notas))

# print(calcular_media(10,9))
# print(calcular_media(10,9,8,7,6,5))


# ---------------------------------------

def preco_final(preco, **adicionais):
    print(adicionais)
    if "desconto" in adicionais:
        preco *= (1-adicionais["desconto"])
    if "garantia_extra" in adicionais:
        preco += adicionais ["garantia_extra"]
    if "imposto" in adicionais:
        preco *= (1-adicionais["imposto"])

    return preco

preco = float(input("Digite o valor da venda: R$ "))
desconto = float(input("Digite o valor do desconto (0% a 100%): "))
garantia = int(input("Você deseja adicionar garantia extra?\n1.Sim\n2.Não"))
imposto = float(input("Digite o valor do imposto sobre o produto (0% a 100%): "))

desconto /= 100
imposto /= 100
if garantia == 1:
    garantia = preco * 0.15
else:
    garantia = 0

print(preco_final(preco, desconto=desconto, garantia_extra=garantia, imposto=imposto))