import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.mongo_queries import MongoQueries
from tasks.extrabom import Extrabom
from tasks.perim import Perim
from model.produtos_mercados import ProdutoMercado
from model.produtos import Produto
from controller.controller_mercado import ControllerMercado

class ControllerProdutoMercado():
    '''
    Classe para gerenciar operações relacionadas a produtos de mercados especificos.
    '''
    def __init__(self):
        self.mongo = MongoQueries()
        pass
    
     
    def __verifica_existencia_produto_mercado(self, codigo: str) -> bool:
        """
        Verifica se um produto de mercado com um determinado código já existe no banco de dados.

        Args:
            codigo_produto_mercado (str): Código do produto de mercado a ser verificado.

        Returns:
            bool: True se o produto de mercado existe, False caso contrário.
        """

        self.mongo.connect()

        # Executa a consulta
        quantidade_documentos = self.mongo.db['produtos_mercados'].count_documents({
            "codigo": codigo
        })


        existe = quantidade_documentos > 0
        self.mongo.close()

        return existe

     
    def busca_produtos_mercados(self, produto: Produto) -> tuple:
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

            if not self.__verifica_existencia_produto_mercado(codigo=produto_perim.codigo):
                
                self.mongo.connect()
                
                self.mongo.db['produtos_mercados'].insert_one({
                    "codigo": produto_perim.codigo,
                    "descricao": produto_perim.descricao,
                    "valor_unitario": produto_perim.valor_unitario,
                    "codigo_produto": produto_perim.produto.codigo,
                    "codigo_mercado": produto_perim.mercado.codigo
                })

                self.mongo.close()

        
        if produto_extrabom is not None:

            if not self.__verifica_existencia_produto_mercado(codigo=produto_extrabom.codigo):
                
                self.mongo.connect()

                self.mongo.db['produtos_mercados'].insert_one({
                    "codigo": produto_extrabom.codigo,
                    "descricao": produto_extrabom.descricao,
                    "valor_unitario": produto_extrabom.valor_unitario,
                    "codigo_produto": produto_extrabom.produto.codigo,
                    "codigo_mercado": produto_extrabom.mercado.codigo
                })
            
                self.mongo.close()

        return produto_perim, produto_extrabom



    def busca_produtos_mercados_db(self, produto: Produto) -> tuple:
        """
        Busca os produtos em mercados específicos no banco de dados.

        Args:
            produto (Produto): O produto a ser buscado.

        Returns:
            tuple: Uma tupla contendo os produtos encontrados nos mercados.

        """
        self.mongo.connect()

        # Consulta
        resultado_consulta = self.mongo.db['produtos_mercados'].find({
            "codigo_produto": produto.codigo
        }).sort("codigo_mercado", 1)

        # Inicializa variáveis
        produto_perim = None
        produto_extrabom = None

        # Loop pelos resultados
        for i, resultado in enumerate(resultado_consulta):

            mercado_codigo = resultado["codigo_mercado"]
            mercado = self.mongo.db['mercado'].find_one({"codigo": mercado_codigo})

            produto_mercado = {
                "codigo": resultado["codigo"],
                "descricao": resultado["descricao"],
                "valor_unitario": resultado["valor_unitario"]
            }

            ctrl_mercado = ControllerMercado()

            if i == 0:
                
                perim = ctrl_mercado.busca_mercado_codigo(codigo=resultado['codigo_mercado']) 
                
                produto_perim = ProdutoMercado(
                    produto=produto,
                    mercado=perim,
                    codigo=resultado['codigo'], 
                    descricao=resultado['descricao'],
                    valor_unitario=resultado['valor_unitario']
                )

            elif i == 1:
                
                extrabom = ctrl_mercado.busca_mercado_codigo(codigo=resultado['codigo_mercado']) 
                
                produto_perim = ProdutoMercado(
                    produto=produto,
                    mercado=extrabom,
                    codigo=resultado['codigo'], 
                    descricao=resultado['descricao'],
                    valor_unitario=resultado['valor_unitario']
                )

        self.mongo.close()

       # Return
        return produto_perim, produto_extrabom

    #  
    # def get_produto_por_codigo(oracle: OracleQueries, codigo: str) -> ProdutoMercado:
    #     """
    #     Obtém um produto específico do carrinho de acordo com o codigo.

    #     Args:
    #         oracle (OracleQueries): Objeto de conexão Oracle.

    #     Returns:
    #         DataFrame: DataFrame contendo informações sobre os produtos no carrinho.

    #         Campos de retorno:
    #         - codigo: Código do produto no carrinho de compras.
    #         - quantidade: Quantidade do produto no carrinho.
    #         - codigo_produto: Código do produto.
    #         - descricao_produto: Descrição do produto.
    #         - codigo_produto_mercado: Código do produto no mercado.
    #         - descricao_produto_mercado: Descrição do produto no mercado.
    #         - valor_unitario: Valor unitário do produto no mercado.

    #         Se não houver nenhum produto no carrinho, retorna None.
    #     """
        
    #     produtos_carrinho = oracle.sqlToDataFrame('SELECT ')

    #     if len(produtos_carrinho) > 0:
    #         return produtos_carrinho
    #     else: 
    #         return None



