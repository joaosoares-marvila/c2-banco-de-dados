import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.oracle_queries import OracleQueries
from model.mercados import Mercado
from model.produtos_mercados import ProdutoMercado

class ControllerMercado:
    def __init__(self):
        pass

    @staticmethod
    def busca_mercado_codigo(oracle: OracleQueries, codigo: int) -> Mercado:
        """
        Busca informações de mercado pelo código.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.
            codigo (int): O código do mercado a ser buscado.

        Returns:
            Mercado or None: Um objeto Mercado com as informações do mercado encontrado, ou None se não for encontrado.
        """
        mercado = oracle.sqlToDataFrame(f"SELECT codigo, nome FROM mercados WHERE codigo = {codigo}")

        if len(mercado) > 0:
            return Mercado(codigo=mercado.iloc[0]['codigo'], nome=mercado.iloc[0]['nome'])
        else:
            return None
