cpf_clientes = ["111.111.111-11", "222.222.222.-22", "222.222.222.-22"]

print("Existem {} CPFs na lista.".format(len(cpf_clientes)))

set_cpf = set(cpf_clientes)
cpf_unicos = list(set_cpf)

print(cpf_unicos)
print("Porém são {} clientes diferentes.".format(len(cpf_unicos)))

