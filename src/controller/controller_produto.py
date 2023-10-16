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

        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        produto = ControllerProduto.busca_produto_descricao(oracle, descricao_produto)
        
        if not produto:
            oracle.write(f"INSERT INTO produtos (descricao) VALUES ('{descricao_produto}')")
            data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE descricao = '{descricao_produto}'")
            codigo = data_frame_produto.iloc[0]['codigo']
            descricao = data_frame_produto.iloc[0]['descricao']
            produto = Produto(codigo=codigo,descricao= descricao)

        return produto

    @staticmethod
    def busca_produto_descricao(oracle: OracleQueries, descricao_produto: str) -> Produto:

        data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE descricao = '{descricao_produto}'")

        if data_frame_produto.empty():
            return None
        
        else:
            codigo = data_frame_produto.iloc[0]['codigo']
            descricao = data_frame_produto.iloc[0]['descricao']
            produto = Produto(codigo=codigo,descricao= descricao)

            return produto
            

    def busca_produto_codigo(oracle: OracleQueries, codigo: int) -> Produto:
        
        data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE codigo = {codigo}")

        if data_frame_produto.empty():
            return None

        else:
            codigo = data_frame_produto.iloc[0]['codigo']
            descricao = data_frame_produto.iloc[0]['descricao']
            produto = Produto(codigo=codigo,descricao= descricao)
            
            return produto
       


if __name__ == "__main__":
    controller_produto = ControllerProduto()
    produtos_perim, produtos_extrabom = controller_produto.inserir_produto("Exemplo")
    if produtos_perim and produtos_extrabom:
        print(f"Produtos encontrados: Perim - {produtos_perim}, Extrabom - {produtos_extrabom}")
