nome = input("Digite seu nome: ")

try:
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))

    #media = (nota1 + nota2) / 2 
    aluno = [nome, [nota1,nota2]]
    media = (aluno[1][0]+aluno[1][1])/2
    #print(aluno[0][2])

    print("A média do aluno {} é {}".format(nome, media))

except:
    print("Valor inválido!")




