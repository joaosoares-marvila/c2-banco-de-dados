import oracledb
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion.oracle_queries import OracleQueries


class Controller_Produto():
    def __init__(self):
        pass


    def inserir_produto(self):
        un = 'sys'
        cs = 'localhost:1521/xe'
        pw = '123mudar'

        with oracledb.connect(user=un, password=pw, dsn=cs, mode=oracledb.SYSDBA) as connection:
            with connection.cursor() as cursor:
                descricao_produto = input("Digite o nome do produto que deseja inserir: ")

                if self.verifica_existencia_produto(connection, descricao_produto):
                    cursor.execute("INSERT INTO PRODUTOS (descricao) VALUES (:descricao_produto)", descricao_produto=descricao_produto)

                # cursor.execute(f"SELECT * FROM PRODUTOS WHERE descricao_produto = '{descricao_produto}'")
                cursor.execute("SELECT * FROM PRODUTOS WHERE descricao = :descricao_produto", descricao_produto=descricao_produto)
                result = cursor.fetchall()
                for row in result:
                    print(row)

                cursor.execute("SELECT * FROM PRODUTOS")
                result = cursor.fetchall()
                for row in result:
                    print(row)

                connection.commit()




    def verifica_existencia_produto(self, connection, descricao_produto):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT codigo FROM produtos WHERE descricao = '{descricao_produto}'")
            result = cursor.fetchall()
            return not result


if __name__ == "__main__":
    controler_produto = Controller_Produto()
    controler_produto.inserir_produto()
