import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.oracle_queries import OracleQueries
from model.produtos import Produto
from controller.controller_produto_mercado import ControllerProdutoMercado


class ControllerProduto:
    def __init__(self):
        pass

    @staticmethod
    def inserir_produto(descricao_produto: str) -> Produto:
        '''
        Insere um novo produto no banco de dados.

        Args:
            descricao_produto (str): Descrição do produto a ser inserido.

        Returns:
            tuple: Uma tupla contendo as informações do produto encontrado nos mercados Perim e Extrabom.
        '''
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        if not ControllerProduto.__verifica_existencia_produto(oracle, descricao_produto):
            oracle.write(f"INSERT INTO produtos (descricao) VALUES ('{descricao_produto}')")

        data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE descricao = '{descricao_produto}'")
        
        codigo__ = data_frame_produto.iloc[0]['codigo']
        descricao__ = data_frame_produto.iloc[0]['descricao']
        produto = Produto(codigo=codigo__,descricao= descricao__)

        return produto

    @staticmethod
    def __verifica_existencia_produto(oracle: OracleQueries, descricao_produto: str) -> bool:
        '''
        Verifica se um produto com uma determinada descrição já existe no banco de dados.

        Args:
            oracle (OracleQueries): Instância da classe OracleQueries para realizar a consulta.
            descricao_produto (str): Descrição do produto a ser verificado.

        Returns:
            bool: True se o produto existe, False caso contrário.
        '''
        df = oracle.sqlToDataFrame(f"SELECT COUNT(*) FROM produtos WHERE descricao = '{descricao_produto}'")

        if df.iloc[0, 0] > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    controller_produto = ControllerProduto()
    produtos_perim, produtos_extrabom = controller_produto.inserir_produto("Exemplo")
    if produtos_perim and produtos_extrabom:
        print(f"Produtos encontrados: Perim - {produtos_perim}, Extrabom - {produtos_extrabom}")
