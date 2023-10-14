from produtos_mercados import ProdutoMercado

class Carrinho:
    # --------- Construtor --------- 
    def __init__(self) -> None:
        self.produtos = []

    # --------- Adiciona produto --------- 
    def adiciona_produto(self, produto_mercado: ProdutoMercado) -> None:
        """
        Adiciona um produto ao carrinho.

        Args:
            produto_mercado (ProdutoMercado): O produto a ser adicionado ao carrinho.
        """
        self.produtos.append(produto_mercado)

    # --------- Remove produto --------- 
    def remove_produto(self, produto_mercado: ProdutoMercado) -> None:
        """
        Remove um produto do carrinho.

        Args:
            produto_mercado (ProdutoMercado): O produto a ser removido do carrinho.
        """
        self.produtos.remove(produto_mercado)
