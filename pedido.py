class Pedido:
    
    def __init__(self, preco_total, status):
        self.preco_total = preco_total
        self.status = status

    def mostra_preço_do_pedido(self):
        print("O seu pedido vai custar R$ %i:{self.preco_total}")
        
