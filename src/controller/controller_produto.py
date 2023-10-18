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
    def inserir_produto(oracle: OracleQueries, descricao_produto: str) -> Produto:
        """
        Insere um novo produto no banco de dados, caso ainda não exista.

        Args:
            descricao_produto (str): A descrição do produto.

        Returns:
            Produto: O objeto Produto inserido ou existente.

        Raises:
            Exception: Em caso de erro ao executar a operação no banco de dados.
        """
        
        # Verifica se o produto já existe
        produto = ControllerProduto.busca_produto_descricao(oracle= oracle, descricao_produto= descricao_produto)
        
        if not produto:

            # Insere o produto no banco de dados
            try:
                oracle.write(f"INSERT INTO produtos (descricao) VALUES ('{descricao_produto}')")
                # Obtém o código e descrição do produto inserido
                data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE descricao = '{descricao_produto}'")
                codigo = data_frame_produto.iloc[0]['codigo']
                descricao = data_frame_produto.iloc[0]['descricao']
                produto = Produto(codigo=codigo, descricao=descricao)
            except Exception as e:
                raise Exception(f"Erro ao inserir produto: {e}")

        # Return
        return produto

    @staticmethod
    def busca_produto_descricao(oracle: OracleQueries, descricao_produto: str) -> Produto:
        """
        Busca um produto pelo seu nome/descrição.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.
            descricao_produto (str): A descrição do produto.

        Returns:
            Produto: O objeto Produto encontrado ou None se não existir.

        """
        # Executa a consulta SQL para buscar o produto
        data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE descricao = '{descricao_produto}'")

        if data_frame_produto.empty:
            return None
        else:
            # Extrai o código e descrição do produto e cria um objeto Produto
            codigo = data_frame_produto.iloc[0]['codigo']
            descricao = data_frame_produto.iloc[0]['descricao']
            produto = Produto(codigo=codigo, descricao=descricao)

            return produto

    @staticmethod
    def busca_produto_codigo(oracle: OracleQueries, codigo: int) -> Produto:
        """
        Busca um produto pelo seu código.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.
            codigo (int): O código do produto.

        Returns:
            Produto: O objeto Produto encontrado ou None se não existir.

        """
        # Executa a consulta SQL para buscar o produto
        data_frame_produto = oracle.sqlToDataFrame(f"SELECT * FROM produtos WHERE codigo = {codigo}")

        # Valida se a consulta retornou algo
        if data_frame_produto.empty:

            return None
        
        else:
        
            # Extrai o código e descrição do produto e cria um objeto Produto
            codigo = data_frame_produto.iloc[0]['codigo']
            descricao = data_frame_produto.iloc[0]['descricao']
            produto = Produto(codigo=codigo, descricao=descricao)

            return produto
       


if __name__ == "__main__":
    # controller_produto = ControllerProduto()
    # produtos_perim, produtos_extrabom = controller_produto.inserir_produto("Exemplo")
    # if produtos_perim and produtos_extrabom:
    #     print(f"Produtos encontrados: Perim - {produtos_perim}, Extrabom - {produtos_extrabom}")
    ...