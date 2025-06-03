notas = []
nome = []

nome1 = input("Digite o nome do primeiro aluno: ")
nota1 = float(input("Digite a nota do primeiro aluno: "))
nome.append(nome1)
notas.append(nota1)

nome2 = input("Digite o nome do segundo aluno: ")
nota2 = float(input("Digite a nota do segundo aluno: "))
nome.append(nome2)
notas.append(nota2)


nome3 = input("Digite o nome do terceiro aluno: ")
nota3 = float(input("Digite a nota do terceiro aluno: "))
nome.append(nome3)
notas.append(nota3)

print("Notas dos alunos\n")
print("Aluno 1 - ", nome1, ":", nota1)
print("Aluno 2 - ", nome2, ":", nota2)
print("Aluno 3 - ", nome3,  ":", nota3)

trocar_nota = input("Digite o nome do aluno para atualizar a nota: ") 

try:
    index = nome.index(trocar_nota)
    nota_atualizada = float(input("Digite a nota para atualizar: "))
    notas[index] = nota_atualizada
except:
    print("O nome não existe na lista.")

print("Nomes e notas dos alunos\n")
print(f"Aluno 1 -  {nome[0]} : {notas[0]}")
print(f"Aluno 2 -  {nome[1]} : {notas[1]}")
print(f"Aluno 3 -  {nome[2]} : {notas[2]}")




