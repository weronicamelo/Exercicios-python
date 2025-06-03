texto = "senai"
print(texto.capitalize())

texto = "SeNaI"
print(texto.casefold())

texto = "senai@email.com.br"
print(texto.count('.'))

texto = "senai@email.com.br"
print(texto.count("email.com.br"))

texto = "123."
print(texto.isalnum())

texto = "Brócolis"
print(texto.isalpha())

texto = "10.0"
print(texto.replace(".", ","))

#Cria uma lista
texto = "senai@email.com.br"
print(texto.split("@"))

texto = "senai mariano ferraz"
print(texto.strip)

#Se algum texto começa com uma string específica
texto = "senai mariano ferraz"
print(texto.startswith("senai"))

texto = "senai mariano ferraz"
print(texto.upper())

