class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Carrinho:
    def __init__(self):
        self.produtos = {}

    def adicionar(self, produto, quantidade):
        if produto.estoque >= quantidade:
            if produto in self.produtos:
                self.produtos[produto] += quantidade
            else:
                self.produtos[produto] = quantidade
            print(f"O produto foi adicionado ao carrinho: {produto.nome}")
        else:
            print(f"Produto insuficiente no estoque! {produto.nome}")

    def remover(self, produto):
        if produto in self.produtos:
            self.produtos[produto] = 0
            print(f"{produto.nome} removido do carrinho.")
        else:
            print(f"{produto.nome} não está no carrinho.")

    def finalizar_compra(self):
        print("\nFinalizar a compra:")
        total = 0

        for produto, quantidade in self.produtos.items():
            if quantidade > 0:
                subtotal = produto.preco * quantidade
                print(f"{produto.nome} - {quantidade}x R${produto.preco:.2f} = R${subtotal:.2f}")
                total += subtotal
                produto.estoque -= quantidade

        if total == 0:
            print("Carrinho está vazio ou todos os itens foram removidos.")
        else:
            print(f"Total da compra: R${total:.2f}")
            print("Compra finalizada com sucesso.")

        for produto in self.produtos:
            self.produtos[produto] = 0

produto1 = Produto("Refrigerante", 10, 800)
produto2 = Produto("Bolacha de maizena", 5, 654)
produto3 = Produto("Macarrão", 4.5, 100)

carrinho = Carrinho()

carrinho.adicionar(produto1, 7)
carrinho.adicionar(produto2, 10)
carrinho.adicionar(produto3, 50)

carrinho.remover(produto1)

carrinho.finalizar_compra()

print("\nAtualização do estoque:")
print(f"{produto1.nome}: {produto1.estoque} unidades")
print(f"{produto2.nome}: {produto2.estoque} unidades")
print(f"{produto3.nome}: {produto3.estoque} unidades")
