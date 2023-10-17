from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # CONTAGEM DOS REGISTROS
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="produtos")
        self.qry_total_mercados = config.QUERY_COUNT.format(tabela="mercados")
        self.qry_total_produtos_carrinho = config.QUERY_COUNT.format(tabela="produtos_carrinho")
        self.qry_total_produtos_mercados = config.QUERY_COUNT.format(tabela="produtos_mercados")


        # Nome(s) do(s) criador(es)
        self.created_by = "Cristian Menezes, Enzo Galão, Gabriel Schunk, Higor Soares, João Pedro Guidolini, João Vitor Marvila"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"


    
    def get_total_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]

    def get_total_mercados(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_mercados)["total_mercados"].values[0]

    def get_total_produtos_carrinho(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos_carrinho)["total_produtos_carrinho"].values[0]

    def get_total_produtos_mercados(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos_mercados)["total_produtos_mercados"].values[0]

    # ATUALIZAR TELA
    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA MERCADO                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:              {str(self.get_total_produtos()).rjust(5)}
        #      2 - MERCADOS:              {str(self.get_total_mercados()).rjust(5)}
        #      3 - PRODUTOS DO CARRINHO:     {str(self.get_total_pedidos()).rjust(5)}
        #      4 - PRODUTOS POR MERCADO:  {str(self.get_total_produtos_mercado()).rjust(5)}
        #
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        #
        ########################################################
        """