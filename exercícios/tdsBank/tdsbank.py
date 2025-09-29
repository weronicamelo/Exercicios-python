from random import randint
from datetime import datetime
import pytz

class ContaCorrente():
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        data_hora_BR = datetime.now(fuso_BR)
        return  data_hora_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, agencia, numero_conta):
        self._nome = nome
        self._cpf = cpf
        self.__saldo = 0
        self.limite = None
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        saldo_aux = format(self.__saldo, '_.2f')
        saldo_aux = saldo_aux.replace(".", ",")
        saldo_aux = saldo_aux.replace("_", ".")
        print(f"Seu saldo é R$: {saldo_aux}")
        print(self.__saldo)

    def depositar(self, valor):
        self.__saldo += valor
        self.transacoes.append(("Depósito", valor, self.__saldo, ContaCorrente._data_hora()))

    def limite_conta(self):
        self.limite = -5000
        return self.limite

    def sacar(self, valor):
        if self.__saldo - valor <= self.limite_conta():
            print("Saldo insuficiente")
            self.consultar_saldo()
        else:
            self.__saldo -= valor
            print("Saque realizado com sucesso")
            self.transacoes.append(("Saque", valor, self.__saldo, ContaCorrente._data_hora()))
            self.consultar_saldo()

    def consultar_transacoes(self):
        print("\nHistórico de Transações:")
        for transacao in self.transacoes:
            print(transacao)

    def pedir_emprestimo(self, valor):
        sucess = self.agencia.emprestar_dinheiro(valor, self._cpf, 0)
        if sucess:
            self.__saldo += valor
            self.transacoes.append(("Empréstimo", valor, self.__saldo, ContaCorrente._data_hora()))

    def transferir(self, valor, conta_destino):
        if self.__saldo - valor < self.limite_conta():
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor
            self.transacoes.append(("Transferência", valor, self.__saldo, ContaCorrente._data_hora()))
            conta_destino.__saldo += valor
            conta_destino.transacoes.append(("Transferência - Entrada", valor, conta_destino.__saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        data_hora_BR = datetime.now(fuso_BR)
        return data_hora_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(100000000000000, 999999999999999)
        self.titular = titular
        self.validade = "{}/{}".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4 )
        self.cod_seguranca = randint(100, 999)
        self.limite = 5000
        self.__senha = "1234"
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

        @property
        def senha(self):
            return self.__senha

        @senha.setter
        def senha(self, valor):
            if len(valor) == 4 and valor.isnumeric():
                self.__senha = valor
            else:
                print("Nova senha invalida!")




