import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
from src.conexion.mongo_queries import MongoQueries
import json

LIST_OF_COLLECTIONS = ["mercados", "produtos_carrinho", "produtos_mercados", "produtos"]

logger = logging.getLogger(name="C3-BANCO-DE-DADOS")
logger.setLevel(level=logging.WARNING)
mongo = MongoQueries()

def createCollections(drop_if_exists:bool=False):
    """
        Lista as coleções existentes, verificar se as coleções padrão estão entre as coleções existentes.
        Caso exista e o parâmetro de exclusão esteja configurado como True, irá apagar a coleção e criar novamente.
        Caso não exista, cria a coleção.
        
        Parameter:
                  - drop_if_exists: True  -> apaga a tabela existente e recria
                                    False -> não faz nada
    """
    mongo.connect()
    existing_collections = mongo.db.list_collection_names()
    for collection in LIST_OF_COLLECTIONS:
        if collection in existing_collections:
            if drop_if_exists:
                mongo.db.drop_collection(collection)
                logger.warning(f"{collection} droped!")
                mongo.db.create_collection(collection)
                logger.warning(f"{collection} created!")
        else:
            mongo.db.create_collection(collection)
            logger.warning(f"{collection} created!")
    mongo.close()

def insert_many(data:json, collection:str):
    mongo.connect()
    mongo.db[collection].insert_many(data)
    mongo.close()


if __name__ == "__main__":
    logging.warning("Starting")
    dados_mercados = [
        {"codigo": 1, "nome": "Perim"},
        {"codigo": 2, "nome": "ExtraBom"}
    ]
    createCollections(drop_if_exists=True)
    insert_many(data=dados_mercados, collection= 'mercados')
    logging.warning("End")