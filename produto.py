class Produto:
    
    def __init__(self, nome, descricao, data_fabricacao, e_ativo):
        self.nome = nome
        self.descricao = descricao  
        self.data_fabricacao = data_fabricacao
        self.e_ativo = e_ativo

    def verifica_disponibilidade(self):
        if self.e_ativo == True:
            print("Temos esse produto em estoque.")
        else:
            print("Produto em falta no estoque.")

