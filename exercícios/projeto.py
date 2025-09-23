class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.membros = []

    def adicionar_membro(self, funcionario):
        for membro in self.membros:
            if membro == funcionario:
                return
        self.membros.append(funcionario)

    def remover_membro(self, funcionario):
        for membro in self.membros:
            if membro == funcionario:
                self.membros.remove(membro)
                print("\nO funcionário(a) " + membro.nome + " foi removido!")
                return

    def listar_membros(self):
        print("\nProjeto:", self.nome)
        print("Descrição:", self.descricao)
        print("\nMembros do Projeto:")
        for membro in self.membros:
            print(f"Nome:", membro.nome, "Cargo:", membro.cargo, "Salário: R$", membro.salario)

    def custo_total(self):
        total = 0
        for membro in self.membros:
            total += membro.salario
        return total

funcionario1 = Funcionario("Mário da Silva,", "Gerente,", 20000)
funcionario2 = Funcionario("Luana da Costa,", "Arquiteta de Software,", 15000)
funcionario3 = Funcionario("Vitor de Oliveira,", "Analista de TI,", 10000)

projeto = Projeto("Projeto Hanks", "Desenvolvimento de um sistema para uma empresa imobiliária")
projeto.adicionar_membro(funcionario1)
projeto.adicionar_membro(funcionario2)
projeto.adicionar_membro(funcionario3)

projeto.listar_membros()
projeto.remover_membro(funcionario2)

print("\nCusto total do Projeto: R$ ", projeto.custo_total())