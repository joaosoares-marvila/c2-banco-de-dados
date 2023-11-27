import pymongo
import os
from pathlib import Path

class MongoQueries:
    def __init__(self):
        
        diretorio_atual = Path(__file__).resolve()
        diretorio_conexion = diretorio_atual.parent
        diretorio_autentication = os.path.join(diretorio_conexion, 'passphrase', 'authentication.mongo')

        with open(diretorio_autentication, "r") as f:
            self.user, self.passwd = f.read().split(',')

        self.host = "cluster0.jmc01ub.mongodb.net"
        self.connection_string = f"mongodb+srv://{self.user}:{self.passwd}@{self.host}/?retryWrites=true&w=majority"


    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        uri = "mongodb+srv://labdatabase:<password>@cluster0.jmc01ub.mongodb.net/?retryWrites=true&w=majority"

        self.mongo_client = pymongo.MongoClient(self.connection_string)
        self.db = self.mongo_client["labdatabase"]

    def close(self):
        self.mongo_client.close()