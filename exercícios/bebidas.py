# def com_alcool(bebida):
#     bebida = bebida.upper()
#     if "BEB" in bebida:
#         return True
#     else:
#         return False
    
# produtos = ["BEB4589", "BEB2019", "BEB4738", "BSA1234", "BSA3984", "BSA8972"]

# for produto in produtos:
#     if com_alcool(produto):
#         print(f"Enviar {produto} para o setor de bebidas alcólicas.")


# ---------------------------------------

# def categoria(bebida, cod_categoria):
#     bebida = bebida.upper()
#     if cod_categoria in bebida:
#         return True
#     else:
#         return False
    
# produtos = ["BEB4589", "BEB2019", "BEB4738", "BSA1234", "BSA3984", "BSA8972"]

# #Utilizando passagem em ordem
# for produto in produtos:
#     if categoria(produto, "BEB"):
#         print(f"Enviar {produto} para o setor de bebidas alcólicas.")
#     elif categoria(produto, "BSA"):
#         print(f"Enviar {produto} para setor de bebidas não alcólicas.")

# #Utilizando passagem com palavra-chave
# for produto in produtos:
#     if categoria(cod_categoria="BEB", bebida=produto):
#         print(f"Enviar {produto} para o setor de bebidas alcólicas.")
#     elif categoria(cod_categoria="BSA", bebida=produto):
#         print(f"Enviar {produto} para setor de bebidas não alcólicas.")


# ---------------------------------------

def operacoes_basicas(num1, num2):
    soma = num1 + num2
    diferenca = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2

    return(soma, diferenca, mult, divisao)

soma, sub, mult, div = operacoes_basicas(2,2)
print(operacoes_basicas(10,2))

