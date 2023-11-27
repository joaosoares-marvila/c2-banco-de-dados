MENU_PRINCIPAL = """ --- MENU PRINCIPAL ---
[1] ADICIONAR PRODUTO AO CARRINHO
[2] ALTERAR PRODUTO DO CARRINHO
[3] REMOVER PRODUTO DO CARRINHO 
[4] RELATORIOS
[0] SAIR
"""

MENU_RELATORIOS = """ --- RELATORIOS ---
[1] PRODUTOS
[2] MERCADOS
[3] PRODUTOS DOS MERCADOS
[4] PRODUTOS DO CARRINHO
[5] TOTAL POR MERCADO
"""

# Consulta de contagem de registros por tabela
def query_count(collection_name: str):

   import sys
   import os
   sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
   
   from conexion.mongo_queries import MongoQueries
   import pandas as pd

   mongo = MongoQueries()
   mongo.connect()

   my_collection = mongo.db[collection_name]
   total_documentos = my_collection.count_documents({})
   mongo.close()
   df = pd.DataFrame({f"total_{collection_name}": [total_documentos]})
   return df

def clear_console(wait_time:int=3):
   '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
   '''

   import platform
   import os
   from time import sleep
   
   sleep(wait_time)
   sistema_operacional = platform.system()
   
   if sistema_operacional == 'Windows':
      os.system("cls")
   else:
      os.system("clear")