from Agencia import Agencia, AgenciaComum, AgenciaVirtual, AgenciaPremium
from tdsbank import ContaCorrente, CartaoCredito

conta_pessoa = ContaCorrente("Maria", "123.456.789-10", "0001", "123456")

cartao_pessoa = CartaoCredito("Maria", conta_pessoa)

print(cartao_pessoa.conta_corrente.numero_conta)

print(cartao_pessoa.numero,"\n",
      cartao_pessoa.titular,"\n",
      cartao_pessoa.validade,"\n",
      cartao_pessoa.cod_seguranca,"\n",
      cartao_pessoa.limite)

agencia1 = Agencia(1234, 40028922, 12345678901234)

agencia1.caixa = 2000000

print(agencia1.__dict__)

agencia1.verificar_caixa()
agencia1.emprestar_dinheiro(5000000, 12345678900, 0.1)

agencia1.adicionar_cliente("Mariano", 12345678900, 870500)
print(agencia1.clientes)

conta_teste = ContaCorrente("teste", "123.457.489-10", agencia1, "1234")
conta_teste.consultar_saldo()
agencia1.verificar_caixa()
conta_teste.pedir_emprestimo(50000)
print(agencia1.emprestimos)
conta_teste.consultar_saldo()
agencia1.verificar_caixa()
conta_teste.consultar_transacoes()

# print(cartao_pessoa.__dict__)
#
# cartao_pessoa.senha = "3567"
# print(cartao_pessoa.senha)

# cartao_pessoa.numero = "1234 5678 9012 3456"
#
# print(conta_pessoa.cartoes)
# print(conta_pessoa.cartoes[0].validade)


#conta_pessoa.depositar(1000)

# conta_pessoa2 = ContaCorrente("Vitoria", "123.465.789-11", "0001", "123457")
# conta_pessoa.depositar(1200)
#
# conta_pessoa.transferir(350, conta_pessoa2)
#
# conta_pessoa.consultar_transacoes()
# conta_pessoa2.consultar_transacoes()
#
# #Sald via metodo
# conta_pessoa.consultar_saldo()
#
# #Tentando mudar o saldo de forma incorreta
# conta_pessoa2.__saldo = 10000
# print(conta_pessoa2.__saldo)

# conta_pessoa.consultar_saldo()
#
# conta_pessoa.depositar(1200)
# conta_pessoa.consultar_saldo()
#
# conta_pessoa.sacar(1000)
# conta_pessoa.consultar_saldo()
#
# conta_pessoa.sacar(4000)
# conta_pessoa.consultar_saldo()
#
# conta_pessoa.consultar_transacoes()

#print(conta_pessoa.data_hora())

#print("O CPF do titular é: ", conta_pessoa.cpf)