from mercados import Mercado
from produtos import Produto
class ProdutoMercado():
    # --------- Construtor --------- 
    def __init__(self, produto: Produto, mercado: Mercado, preco: float) -> None:
        self._produto = produto
        self._mercado = mercado
        self._preco = preco

    # --------- Produto --------- 
    @property
    def produto(self) -> Produto:
        return self._produto

    @produto.setter
    def produto(self, produto: Produto) -> None:
        self._produto = produto
    
    # --------- Mercado --------- 
    @property
    def mercado(self) -> Mercado:
        return self._mercado

    @mercado.setter
    def mercado(self, mercado: Mercado) -> None:
        self._mercado = mercado
    
    # --------- Preço --------- 
    @property
    def preco(self) -> float:
        return self._preco

    @produto.setter
    def produto(self, produto: Produto) -> None:
        self._produto = produto

    # --------- Representação --------- 
    def __repr__(self) -> str:
        return f"Produto: {self.produto.codigo} - {self.produto._descricao} | Mercado: {self.mercado.nome} | Preço: {self.preco}"




