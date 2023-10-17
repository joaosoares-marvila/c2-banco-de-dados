from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # CONTAGEM DOS REGISTROS
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="produtos")
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="mercados")
        self.qry_total_fornecedores = config.QUERY_COUNT.format(tabela="carrinho")
        self.qry_total_pedidos = config.QUERY_COUNT.format(tabela="produtos_mercado")

    # FUNCS
    def get_total_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]

    def get_total_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_mercados)["total_mercados"].values[0]

    def get_total_fornecedores(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_pedidos)["total_pedidos"].values[0]
    
    def get_total_fornecedores(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos_mercado)["total_produtos_mercado"].values[0]

    # ATUALIZAR TELA
    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA MERCADO                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:              {str(self.get_total_produtos()).rjust(5)}
        #      2 - MERCADOS:              {str(self.get_total_mercados()).rjust(5)}
        #      3 - PEDIDOS(CARRINHO):     {str(self.get_total_pedidos()).rjust(5)}
        #      4 - PRODUTOS POR MERCADO:  {str(self.get_total_produtos_mercado()).rjust(5)}
        #
        ########################################################
        """