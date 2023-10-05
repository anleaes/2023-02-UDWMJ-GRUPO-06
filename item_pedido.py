class ItemPedido:

    def __init__(self, quantidade, preco_unitario, Pedido, produto):
       self.quantidade = quantidade
       self.preco_unitario = preco_unitario
       self.Pedido = Pedido
       self.produto = produto

    def mostra_qual_o_produto_e_o_preço(self):
        print("O item selecionado foi %s ele custará %i")
