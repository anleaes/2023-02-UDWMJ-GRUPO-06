class Categoria:

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def imprime_informacoes_categorias(self):
        print("A categoria do produto é %s e a descricao é %s.{self.nome}: {self.descricao}")