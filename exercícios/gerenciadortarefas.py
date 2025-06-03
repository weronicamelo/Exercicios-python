tarefas = []
concluidas = []

tarefa1 = input("Digite a primeira tarefa: ")
tarefa2 = input("Digite a segunda tarefa: ")

tarefas.append(tarefa1)
tarefas.append(tarefa2)

print("\nTarefas pendentes:")
print(tarefas)

tarefaConcluida = input("\nQual tarefa você já concluiu? ")

try:
    tarefas.remove(tarefaConcluida)
    concluidas.append(tarefaConcluida)
    print(f"Tarefa '{tarefaConcluida}' removida com sucesso!")
except:
    print("Essa tarefa não está na lista.")

print("\nTarefas concluídas:")
if concluidas:
    print(concluidas)
else:
    print("Nenhuma tarefa concluída.")

print("\nTarefas pendentes:")
print(tarefas)

