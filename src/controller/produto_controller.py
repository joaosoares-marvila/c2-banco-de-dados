import oracledb
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.oracle_queries import OracleQueries
from model.produtos import Produto
from controller.produto_mercado_controller import buscar_produtos_mercados

class Controller_Produto():
    '''
    Classe para gerenciar operações relacionadas a produtos.
    '''
    def __init__(self):
        pass
  
    def inserir_produto(self):
        '''
        Insere um novo produto no banco de dados.

        Returns:
            tuple: Uma tupla contendo as informações do produto encontrado nos mercados Perim e Extrabom.
        '''
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        descricao_produto = input("Digite o nome do produto que deseja inserir: ")
        
        if not self.verifica_existencia_produto(oracle, descricao_produto):
            # Insere um novo produto caso ele não esteja presente no banco
            oracle.write(f"insert into produtos (descricao_produto) values ('{descricao_produto}')")

        data_frame_produto = oracle.sqlToDataFrame(f"select * from produtos where descricao_produto = '{descricao_produto}'")
        produto = Produto(data_frame_produto.codigo.value[0], data_frame_produto.descricao.value[0])

        produto_perim, produto_extrabom = buscar_produtos_mercados(produto)

        return produto_perim, produto_extrabom
    

    def verifica_existencia_produto(oracle: OracleQueries, descricao_produto: str) -> bool:
        '''
        Verifica se um produto com uma determinada descrição já existe no banco de dados.

        Args:
            oracle (OracleQueries): Instância da classe OracleQueries para realizar a consulta.
            descricao_produto (str): Descrição do produto a ser verificado.

        Returns:
            bool: True se o produto existe, False caso contrário.
        '''
        df = oracle.sqlToDataFrame(f"SELECT COUNT(*) FROM produtos WHERE descricao_produto = '{descricao_produto}'")

        if df.iloc[0, 0] > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    controler_produto = Controller_Produto()
    controler_produto.inserir_produto()