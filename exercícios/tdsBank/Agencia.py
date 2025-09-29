from random import randint
from tdsbank import ContaCorrente

class Agencia:
    def __init__(self, numero, telefone, cpnj):
        self.numero = numero
        self.telefone = telefone
        self.cpnj = cpnj
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 2000000:
            print(f"Caixa abaixo do nível recomendado. Caixa atual R$ {self.caixa}")
        else:
            print(f"O nível do caixa está OK! Caixa atual R$ {self.caixa}")

    def emprestar_dinheiro(self, valor, conta_pessoa, juros):
        if self.caixa > valor:
            print("Emprestimo realizado com sucesso!")
            self.caixa -= valor
            self.emprestimos.append((valor, conta_pessoa, juros))
            return True
        else:
            print("Não foi possível realizar o emprestimo! Valor não disponível")
            return False

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):
    def __init__(self, numero, site, telefone, cpnj):
        self.site = site
        super().__init__(numero, telefone, cpnj)
        self.caixa = 100000000
        self.caixa_paypal = 0

    def depositar_playpal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(randint(1001,9999), telefone, cnpj)
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(randint(1001,9999), telefone, cnpj)
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("Cliente não possui o patrimonio mínimo ncessário!")

agencia1 = Agencia(123, 4002822, 13454359678596)

# print("\nAgência Virtual: ")
agencia_virtual = AgenciaVirtual("1456", "www.agencia.com", "40020922", "1234567890123")
# print(agencia_virtual.__dict__)
#
# print("\nAgência Comum: ")
agencia_comum = AgenciaComum(4445489, 123456544789052)
# agencia_comum.verificar_caixa()
# print(agencia_comum.__dict__)

# print("\nAgência Premium: ")
agencia_premium = AgenciaPremium(4447689, 12345647564894)
# agencia_premium.verificar_caixa()
# print(agencia_premium.__dict__)

# print("\n")
#
# agencia_virtual.depositar_playpal(25000)
# print(f"Caixa virtual: R$ {agencia_virtual.caixa}")
# print(f"Caixa paypal: R$ {agencia_virtual.caixa_paypal}")

if __name__ == '__main__':
    agencia1.adicionar_cliente("José", 82588913452, 10000000)
    print("clientes agencia1: ", agencia1.clientes)

    agencia_comum.adicionar_cliente("José", 82588913452, 10000000)
    print("clientes agencia comum: ", agencia1.clientes)

    agencia_virtual.adicionar_cliente("José", 82588913452, 10000000)
    print("clientes agencia virtual: ", agencia1.clientes)

    agencia_premium.adicionar_cliente("José", 82588913452, 10000000)
    print("clientes agencia premium: ", agencia1.clientes)


