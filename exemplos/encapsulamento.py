# Encapsulamento - é tornar  um atriuto privado que só vai ser acessado pela própria classe
# self faz referência a própria instância da classe
class ContaBancaria:
    def __init__(self, titular, __saldo):
        self.nome = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valr > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria('Vitoria', 50000)
conta.depositar(100)
conta.sacar(50)
print(conta.ver__saldo())


