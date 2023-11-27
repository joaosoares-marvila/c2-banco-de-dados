import sys

import os
from pathlib import Path

diretorio_atual = Path(__file__).resolve()
diretorio_src = diretorio_atual.parent.parent

from conexion.mongo_queries import MongoQueries

class Relatorio:
    def __init__(self):

        self.mongo = MongoQueries()

    def get_relatorio_mercados(self):

        self.mongo.connect()

        # Execute a consulta e obtenha a coleção
        collection = self.mongo.db['mercados']

        # Use o método count_documents na coleção
        total_documentos = collection.count_documents({})
        
        if total_documentos == 0:
            print("Não foi encontrado nenhum documento")
        else:
            resultado_consulta = self.mongo.db['mercados'].find().sort("codigo", 1)

            # Loop pelos resultados
            for resultado in resultado_consulta:
                print(f"Código: {resultado['codigo']}, Nome: {resultado['nome']}")

        self.mongo.close()
        input("Pressione Enter para Sair do Relatório de Mercados")

    def get_relatorio_produtos_carrinho(self):

        self.mongo.connect()

        # Execute a consulta e obtenha a coleção
        collection = self.mongo.db['produtos_carrinho']
        
        # Use o método count_documents na coleção
        total_documentos = collection.count_documents({})
        
        if total_documentos == 0:
            print("Não foi encontrado nenhum documento")
        else:

            resultado_consulta = self.mongo.db['produtos_carrinho'].aggregate([
                {
                    "$lookup": {
                        "from": "produtos_mercados",
                        "localField": "codigo_produto_mercado",
                        "foreignField": "codigo",
                        "as": "produto_mercado"
                    }
                },
                {
                    "$unwind": "$produto_mercado"
                },
                {
                    "$lookup": {
                        "from": "produtos",
                        "localField": "produto_mercado.codigo_produto",
                        "foreignField": "codigo",
                        "as": "produto"
                    }
                },
                {
                    "$unwind": "$produto"
                },
                {
                    "$project": {
                        "_id": 0,
                        "codigo_carrinho": "$codigo",
                        "quantidade": "$quantidade",
                        "codigo_produto": "$produto.codigo",
                        "descricao_produto": "$produto.descricao",
                        "codigo_produto_mercado": "$produto_mercado.codigo",
                        "descricao_produto_mercado": "$produto_mercado.descricao",
                        "valor_unitario": "$produto_mercado.valor_unitario"
                    }
                },
                {
                    "$sort": {"codigo_carrinho": 1}
                }
            ])

            # Exibe os resultados
            for resultado in resultado_consulta:
                print(f"Código: {resultado['codigo_carrinho']}, "
                    f"Quantidade: {resultado['quantidade']}, "
                    f"Código Produto: {resultado['codigo_produto']}, "
                    f"Descrição Produto: {resultado['descricao_produto']}, "
                    f"Código Produto Mercado: {resultado['codigo_produto_mercado']}, "
                    f"Descrição Produto Mercado: {resultado['descricao_produto_mercado']}, "
                    f"Valor Unitário: {resultado['valor_unitario']}\n")

        self.mongo.close()

        input("Pressione Enter para Sair do Relatório de Produtos do Carrinho")

    def get_relatorio_produtos_mercados(self):
        
        self.mongo.connect()

        # Execute a consulta e obtenha a coleção
        collection = self.mongo.db['produtos_mercados']

        # Use o método count_documents na coleção
        total_documentos = collection.count_documents({})

        if total_documentos == 0:
            print("Não foi encontrado nenhum documento")
        else:
            # Consulta para buscar os produtos nos mercados no MongoDB e ordenar por descrição
            resultado_consulta = collection.aggregate([
                {
                    "$lookup": {
                        "from": "produtos",
                        "localField": "codigo_produto",
                        "foreignField": "codigo",
                        "as": "produto"
                    }
                },
                {
                    "$unwind": "$produto"
                },
                {
                    "$lookup": {
                        "from": "mercados",
                        "localField": "codigo_mercado",
                        "foreignField": "codigo",
                        "as": "mercado"
                    }
                },
                {
                    "$unwind": "$mercado"
                },
                {
                    "$project": {
                        "_id": 0,
                        "codigo": "$codigo",
                        "descricao": "$descricao",
                        "valor_unitario": "$valor_unitario",
                        "codigo_produto": "$produto.codigo",
                        "descricao_produto": "$produto.descricao",
                        "mercado": "$mercado.nome"
                    }
                },
                {
                    "$sort": {"descricao": 1}
                }
            ])

            # Exibe os resultados
            for resultado in resultado_consulta:
                print(f"Código: {resultado['codigo']}, "
                    f"Descrição: {resultado['descricao']}, "
                    f"Valor Unitário: {resultado['valor_unitario']}, "
                    f"Código Produto: {resultado['codigo_produto']}, "
                    f"Descrição Produto: {resultado['descricao_produto']}, "
                    f"Mercado: {resultado['mercado']}\n")

        input("Pressione Enter para Sair do Relatório de Produtos dos Mercados")

    def get_relatorio_produtos(self):

        self.mongo.connect()
        # Execute a consulta e obtenha a coleção
        collection = self.mongo.db['produtos']
        
        # Use o método count_documents na coleção
        total_documentos = collection.count_documents({})

        if total_documentos == 0:
            print("Não foi encontrado nenhum documento")
        else:

            resultado_consulta = collection.find().sort("codigo", 1)
            
            # Loop pelos resultados
            for resultado in resultado_consulta:
                print(f"Código: {resultado['codigo']}, Descrição: {resultado['descricao']}")

        self.mongo.close()
        input("Pressione Enter para Sair do Relatório de Produtos")

    def get_total_por_mercado(self):

        self.mongo.connect()

        resultado_consulta = self.mongo.db['produtos_carrinho'].aggregate([
            {
                "$lookup": {
                    "from": "produtos_mercados",
                    "localField": "codigo_produto_mercado",
                    "foreignField": "codigo",
                    "as": "produto_mercado"
                }
            },
            {
                "$unwind": "$produto_mercado"
            },
            {
                "$group": {
                    "_id": "$produto_mercado.codigo_mercado",
                    "total_gasto": {"$sum": {"$multiply": ["$quantidade", "$produto_mercado.valor_unitario"]}}
                }
            },
            {
                "$lookup": {
                    "from": "mercados",
                    "localField": "_id",
                    "foreignField": "codigo",
                    "as": "mercado"
                }
            },
            {
                "$unwind": "$mercado"
            },
            {
                "$project": {
                    "nome_mercado": "$mercado.nome",
                    "total_gasto": 1,
                    "_id": 0
                }
            }
        ])

        for resultado in resultado_consulta:
            print(f"Mercado: {resultado['nome_mercado']}, Total Gasto: {resultado['total_gasto']:.2f}")

        input("Pressione Enter para Sair do Relatório de Total por mercado")


        self.mongo.close()




