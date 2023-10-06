class RedeSocialCliente:

    def __init__(self, cliente, rede_social):
        self.cliente = cliente
        self.rede_social = rede_social

    def verifica_rede_social(self):
        if self.rede_social == True:
            print("Rede social encontrada!")
        else:
            print("Rede social não encontrada!")