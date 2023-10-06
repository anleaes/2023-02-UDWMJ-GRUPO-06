class RedeSocial:

    def __init__(self,nome,descricao):
       self.nome = nome  
       self.descricao = descricao


    def verifica_nome(self):
        if self.nome == str:
            print("Nome registrado!")
        else:
            print("Nome não registrado!")