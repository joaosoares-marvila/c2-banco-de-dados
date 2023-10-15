import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.oracle_queries import OracleQueries
from tasks.extrabom import Extrabom
from tasks.perim import Perim
from model.produtos_mercados import ProdutoMercado

class Controller_Produto():
    '''
    Classe para gerenciar operações relacionadas a produtos de mercados especificos.
    '''
    def __init__(self):
        pass
    
    def verifica_existencia_produto_mercado(oracle: OracleQueries, codigo_produto_mercado: str) -> bool:
        """
        Verifica se um produto de mercado com um determinado código já existe no banco de dados.

        Args:
            oracle (OracleQueries): Instância da classe OracleQueries para realizar a consulta.
            codigo_produto_mercado (str): Código do produto de mercado a ser verificado.

        Returns:
            bool: True se o produto de mercado existe, False caso contrário.
        """
        df = oracle.sqlToDataFrame(f"SELECT COUNT(*) FROM produtos_mercados WHERE codigo = '{codigo_produto_mercado}'")

        if df.iloc[0, 0] > 0:
            return True
        else:
            return False


    def buscar_produtos_mercados(produto: Produto) -> tuple:
        """
        Busca produtos em mercados específicos e insere as informações no banco de dados.

        Args:
            produto (Produto): O produto a ser buscado.

        Returns:
            tuple: Uma tupla contendo as informações dos produtos encontrados nos mercados Perim e Extrabom.
        """
        
        # Mercados 
        perim = Perim()
        extrabom = Extrabom()

        # Produtos
        produto_perim : ProdutoMercado = perim.busca_produto(produto= produto)
        produto_extrabom : ProdutoMercado = extrabom.busca_produto(produto= produto)

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Insere os produtos no banco
        if produto_perim is not None:

            if not self.verifica_existencia_produto_mercado(oracle, produto_perim.codigo):
                oracle.write(f"insert into produtos_mercados (codigo, descricao, valor_unitario, codigo_produto, CODIGO_MERCADO) values ('{produto_perim.codigo}', '{produto_perim.descricao}', '{produto_perim.valor_unitario}', '{produto_perim.produto.codigo}', '{produto_perim.mercado.codigo}' )")
        
        
        if produto_extrabom is not None:

            if not self.verifica_existencia_produto_mercado(oracle, produto_extrabom.codigo):
                oracle.write(f"insert into produtos_mercados (codigo, descricao, valor_unitario, codigo_produto, CODIGO_MERCADO) values ('{produto_extrabom.codigo}', '{produto_extrabom.descricao}', '{produto_extrabom.valor_unitario}', '{produto_extrabom.produto.codigo}', '{produto_extrabom.mercado.codigo}' )")
        
        return produto_perim, produto_extrabom



if __name__ == "__main__":
    controler_produto = Controller_Produto()
    controler_produto.inserir_produto()

