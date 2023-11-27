import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas
from conexion.mongo_queries import MongoQueries
from model.mercados import Mercado

class ControllerMercado:
    def __init__(self):
        self.mongo = MongoQueries()

    def busca_mercado_codigo(self, codigo: int) -> Mercado:
        """
        Busca informações de mercado pelo código.

        Args:
            codigo (int): O código do mercado a ser buscado.

        Returns:
            Mercado or None: Um objeto Mercado com as informações do mercado encontrado, ou None se não for encontrado.
        """

        # Abre a conexão com o Mongo
        self.mongo.connect()
        
        # Consulta
        resultado_consulta = self.mongo.db["mercados"].find_one(
            {"codigo":codigo}, # Condicional
            {"codigo": 1, "nome": 1, "_id": 0} # Campos que serão buscados
        )

        # Fecha a conexão com o Mongo
        self.mongo.close()
        
        return Mercado(codigo=resultado_consulta['codigo'], nome=resultado_consulta['nome'])

