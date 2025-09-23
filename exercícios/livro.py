class Livro:
    def __init__(self, titulo, ano_publicacao, autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print("O livro está emprestado")
        else:
            self.disponivel = True
            print("O livro está disponível para empréstimo")

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
        else:
            print("Livro disponível")

    def exibir_info(self):
        print("\n----- Informações sobre o Livro -----")
        print(f"Título: {self.titulo}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Autor: {self.autor}")

        if self.disponivel:
            print("Está disponível!")
        else:
            print("Não está disponível!")

livro1 = Livro("Entendendo algoritmos", "2017", "Aditya Y.Bhargava")
livro2 = Livro("A biblioteca da meia noite", "2021", "Matt Haig")
livro3 = Livro("O sol é para todos", "2006", "Harper Lee")

livro1.exibir_info()
livro2.exibir_info()
livro3.exibir_info()

livro1.emprestar()
livro1.exibir_info()

livro1.devolver()
livro1.exibir_info()