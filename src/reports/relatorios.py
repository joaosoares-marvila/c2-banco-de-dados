import sys

import os
from pathlib import Path

diretorio_atual = Path(__file__).resolve()
diretorio_src = diretorio_atual.parent.parent

from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):

        relatorio_mercados = os.path.join(diretorio_src, 'sql', 'relatorio_mercados.sql')
        relatorio_produtos_carrinho = os.path.join(diretorio_src, 'sql', 'relatorio_produtos_carrinho.sql')
        relatorio_produtos_mercados = os.path.join(diretorio_src, 'sql', 'relatorio_produtos_mercados.sql')
        relatorio_produtos = os.path.join(diretorio_src, 'sql', 'relatorio_produtos.sql')

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open(relatorio_mercados) as f:
            self.query_relatorio_mercados = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open(relatorio_produtos_carrinho) as f:
            self.query_relatorio_produtos_carrinho = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open(relatorio_produtos_mercados) as f:
            self.query_relatorio_produtos_mercados = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open(relatorio_produtos) as f:
            self.query_relatorio_produtos = f.read()

    def get_relatorio_mercados(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_mercados))
        input("Pressione Enter para Sair do Relatório de Mercados")

    def get_relatorio_produtos_carrinho(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos_carrinho))
        input("Pressione Enter para Sair do Relatório de Produtos do Carrinho")

    def get_relatorio_produtos_mercados(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos_mercados))
        input("Pressione Enter para Sair do Relatório de Produtos dos Mercados")

    def get_relatorio_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para Sair do Relatório de Produtos")