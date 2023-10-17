import json
import oracledb
from pandas import DataFrame

class OracleQueries:
    '''
    Classe para auxiliar na conexão com o Banco de Dados Oracle usando a biblioteca oracledb.
    '''

    def __init__(self, can_write: bool = False):
        '''
        Inicializa a classe OracleQueries.

        Args:
            can_write (bool): Define se a conexão permite operações de escrita no banco de dados.

        Attributes:
            can_write (bool): Indica se a conexão permite operações de escrita.
            host (str): O endereço do servidor Oracle.
            port (int): A porta em que o Oracle está escutando.
            service_name (str): O nome do serviço do banco de dados Oracle.
            sid (str): O ID do serviço.

        '''
        self.can_write = can_write
        self.host = "localhost"
        self.port = 1521
        self.service_name = 'XEPDB1'
        self.sid = 'xe'

        with open(r"c:\Users\joaos\Desktop\Banco de dados\c2-banco-de-dados\src\conexion\passphrase\authentication.oracle", "r") as f:
            self.user, self.passwd = f.read().split(',')

    def __del__(self):
        '''
        Executado quando o objeto é destruído. Fecha a conexão se estiver aberta.
        '''
        if hasattr(self, 'conn'):
            self.close()

    def connect(self):
        '''
        Realiza a conexão com o banco de dados Oracle.

        Returns:
            cursor: Um objeto cursor para executar comandos no banco de dados.

        '''
        if not hasattr(self, 'conn'):
            # dsn = f'{self.user}/{self.passwd}@{self.host}:{self.port}/{self.service_name}'
            # dsn = oracledb.makedsn(self.host, self.port, service_name=self.service_name if self.service_name else self.sid)
            self.conn = oracledb.connect(user=self.user, password=self.passwd, dsn=f'{self.host}/{self.sid}', mode=oracledb.SYSDBA)
            self.cur = self.conn.cursor()
        return self.cur

    def sqlToDataFrame(self, query: str) -> DataFrame:
        '''
        Executa uma consulta e retorna os resultados em um DataFrame do Pandas.

        Args:
            query (str): A consulta SQL a ser executada.

        Returns:
            DataFrame: Um DataFrame com os resultados da consulta.

        '''
        cur = self.connect()
        cur.execute(query)
        rows = cur.fetchall()
        columns = [col[0].lower() for col in cur.description]
        return DataFrame(rows, columns=columns)

    def sqlToMatrix(self, query: str) -> tuple:
        '''
        Executa uma consulta e retorna uma matriz (lista de listas) e uma lista com os nomes das colunas.

        Args:
            query (str): A consulta SQL a ser executada.

        Returns:
            tuple: Uma tupla contendo a matriz de resultados e a lista de nomes das colunas.

        '''
        cur = self.connect()
        cur.execute(query)
        rows = cur.fetchall()
        matrix = [list(row) for row in rows]
        columns = [col[0].lower() for col in cur.description]
        return matrix, columns

    def sqlToJson(self, query: str):
        '''
        Executa uma consulta e retorna os resultados em formato JSON.

        Args:
            query (str): A consulta SQL a ser executada.

        Returns:
            str: Uma string JSON representando os resultados.

        '''
        cur = self.connect()
        cur.execute(query)
        columns = [col[0].lower() for col in cur.description]
        cur.rowfactory = lambda *args: dict(zip(columns, args))
        rows = cur.fetchall()
        return json.dumps(rows, default=str)

    def write(self, query: str):
        '''
        Executa uma consulta de escrita no banco de dados.

        Args:
            query (str): A consulta SQL de escrita a ser executada.

        Raises:
            Exception: Se a conexão não permite operações de escrita.

        '''
        if not self.can_write:
            raise Exception('Não é possível escrever usando esta conexão')


        cur = self.connect()
        cur.execute(query)
        self.conn.commit()
       

    def close(self):
        '''
        Fecha a conexão com o banco de dados.

        '''
        if hasattr(self, 'cur'):
            self.cur.close()
            del self.cur
        if hasattr(self, 'conn'):
            self.conn.close()
            del self.conn

    def executeDDL(self, query: str):
        '''
        Executa um comando DDL (Data Definition Language) no banco de dados.

        Args:
            query (str): O comando DDL a ser executado.

        '''
        cur = self.connect()
        cur.execute(query)
