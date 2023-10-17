import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.oracle_queries import OracleQueries
from tasks.extrabom import Extrabom
from tasks.perim import Perim
from model.produtos_mercados import ProdutoMercado
from model.produtos import Produto

class ControllerProdutoMercado():
    '''
    Classe para gerenciar operações relacionadas a produtos de mercados especificos.
    '''
    def __init__(self):
        pass
    
    @staticmethod
    def __verifica_existencia_produto_mercado(oracle: OracleQueries, codigo: str) -> bool:
        """
        Verifica se um produto de mercado com um determinado código já existe no banco de dados.

        Args:
            oracle (OracleQueries): Instância da classe OracleQueries para realizar a consulta.
            codigo_produto_mercado (str): Código do produto de mercado a ser verificado.

        Returns:
            bool: True se o produto de mercado existe, False caso contrário.
        """
        df = oracle.sqlToDataFrame(f"SELECT COUNT(*) FROM produtos_mercados WHERE codigo = '{codigo}'")

        if df.iloc[0, 0] > 0:
            return True
        else:
            return False

    @staticmethod
    def busca_produtos_mercados(oracle: OracleQueries, produto: Produto) -> tuple:
        """
        Busca produtos em mercados específicos e insere as informações no banco de dados.

        Args:
            produto (Produto): O produto a ser buscado.

        Returns:
            tuple: Uma tupla contendo as informações dos produtos encontrados nos mercados Perim e Extrabom.
        """
        
        print("Buscando produtos...")

        # Mercados 
        perim = Perim()
        extrabom = Extrabom()

        # Produtos
        produto_perim : ProdutoMercado = perim.busca_produto(produto= produto)
        produto_extrabom : ProdutoMercado = extrabom.busca_produto(produto= produto)
        
        # Insere os produtos no banco
        if produto_perim is not None:

            if not ControllerProdutoMercado.__verifica_existencia_produto_mercado(oracle, produto_perim.codigo):
                
                print('Inserindo produto Perim')

                query = f"insert into produtos_mercados (codigo, descricao, valor_unitario, codigo_produto, CODIGO_MERCADO) values ('{produto_perim.codigo}', '{produto_perim.descricao}', {produto_perim.valor_unitario}, {produto_perim.produto.codigo}, {produto_perim.mercado.codigo} )"
                
                print(query)
                
                oracle.write(query)

                print('Inseriu')
        
        
        if produto_extrabom is not None:

            if not ControllerProdutoMercado.__verifica_existencia_produto_mercado(oracle, produto_extrabom.codigo):
                oracle.write(f"insert into produtos_mercados (codigo, descricao, valor_unitario, codigo_produto, CODIGO_MERCADO) values ('{produto_extrabom.codigo}', '{produto_extrabom.descricao}', '{produto_extrabom.valor_unitario}', '{produto_extrabom.produto.codigo}', '{produto_extrabom.mercado.codigo}' )")
        

        return produto_perim, produto_extrabom



    @staticmethod
    def busca_produtos_mercados_db(oracle: OracleQueries, produto: Produto) -> tuple:
        """
        Busca os produtos em mercados específicos no banco de dados.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.
            produto (Produto): O produto a ser buscado.

        Returns:
            tuple: Uma tupla contendo os produtos encontrados nos mercados.

        """
        # DataFrame
        data_frame_produtos_mercados = oracle.sqlToDataFrame(f'SELECT * FROM produtos_mercados WHERE codigo_produto = {codigo_produto} ORDER BY codigo_mercado')

        # Perim
        dados_produto_perim = data_frame_produtos_mercados.iloc[0]
        perim = ControllerMercado.busca_mercado_codigo(dados_produto_perim['codigo_mercado']) 
        
        produto_perim = ProdutoMercado(
            produto=produto,
            mercado=perim, 
            codigo=dados_produto_perim['codigo'], 
            descricao=dados_produto_perim['descricao'],
            valor_unitario=dados_produto_perim['valor_unitario']
        )
        
        # ExtraBom
        dados_produto_extrabom = data_frame_produtos.iloc[1]
        extrabom = ControllerMercado.busca_mercado_codigo(dados_produto_extrabom['codigo_mercado']) 
        
        produto_extrabom = ProdutoMercado(
            produto=produto,
            mercado=extrabom, 
            codigo=dados_produto_extrabom['codigo'], 
            descricao=dados_produto_extrabom['descricao'],
            valor_unitario=dados_produto_extrabom['valor_unitario']
        )

        # Return
        return produto_perim, produto_extrabom

    @staticmethod
    def get_produto_por_codigo(oracle: OracleQueries, codigo: str) -> ProdutoMercado:
                """
        Obtém um produto específico do carrinho de acordo com o codigo.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.

        Returns:
            DataFrame: DataFrame contendo informações sobre os produtos no carrinho.

            Campos de retorno:
            - codigo: Código do produto no carrinho de compras.
            - quantidade: Quantidade do produto no carrinho.
            - codigo_produto: Código do produto.
            - descricao_produto: Descrição do produto.
            - codigo_produto_mercado: Código do produto no mercado.
            - descricao_produto_mercado: Descrição do produto no mercado.
            - valor_unitario: Valor unitário do produto no mercado.

            Se não houver nenhum produto no carrinho, retorna None.
        """
        
        produtos_carrinho = oracle.sqlToDataFrame('SELECT ')

        if len(produtos_carrinho) > 0:
            return produtos_carrinho
        else: 
            return None



