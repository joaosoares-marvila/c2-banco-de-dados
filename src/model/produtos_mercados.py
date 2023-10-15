import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.mercados import Mercado
from model.produtos import Produto

class ProdutoMercado():
    # --------- Construtor --------- 
    def __init__(self, produto: Produto, mercado: Mercado, codigo: str, descricao: str, valor_unitario: float) -> None:
        self._codigo = codigo
        self._descricao = descricao
        self._produto = produto
        self._mercado = mercado
        self._valor_unitario = float(valor_unitario)

    # --------- Código --------- 
    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: str) -> None:
        self._codigo = codigo

    # --------- Descrição --------- 
    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self._descricao = descricao

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
    
    # --------- Valor unitário --------- 
    @property
    def valor_unitario(self) -> float:
        return self._valor_unitario

    @valor_unitario.setter
    def valor_unitario(self, valor_unitario: float) -> None:
        self._valor_unitario = valor_unitario

    # --------- String --------- 
    def __str__(self) -> str:
        return f"Mercado: {self.mercado.nome} | Produto: {self.descricao} Valor unitário: {self.valor_unitario}"




