import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.mongo_queries import MongoQueries
from model.produtos import Produto
from controller.controller_produto_mercado import ControllerProdutoMercado


class ControllerProduto:
    def __init__(self):
        self.mongo = MongoQueries()

     
    def inserir_produto(self, descricao_produto: str) -> Produto:
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
        ctrl_produto = ControllerProduto()
        produto = ctrl_produto.busca_produto_descricao(descricao_produto= descricao_produto)
        
        if not produto:

            # Insere o documento no DB
            try:
                self.mongo.connect()
                
                # Obtém o próximo valor para o campo "codigo"
                ultimo_documento = self.mongo.db['produtos'].find_one(sort=[("codigo", -1)])

                # Calcula o próximo código (incrementando 1 ao último código se existir, caso contrário, inicia em 1)
                proximo_codigo = (ultimo_documento["codigo"] + 1) if ultimo_documento else 1


                resultado_insercao = self.mongo.db['produtos'].insert_one({
                    "codigo": proximo_codigo,
                    "descricao": descricao_produto
                })

                produto = Produto(codigo=proximo_codigo, descricao=descricao_produto)

                self.mongo.close()


            
            except Exception as e:
                raise Exception(f"Erro ao inserir produto: {e}")

        # Return
        return produto

     
    def busca_produto_descricao(self, descricao_produto: str) -> Produto:
        """
        Busca um produto pelo seu nome/descrição.

        Args:
            descricao_produto (str): A descrição do produto.

        Returns:
            Produto: O objeto Produto encontrado ou None se não existir.

        """

        self.mongo.connect()
        # Executa a consulta
        resultado_consulta = self.mongo.db['produtos'].find_one({
            "descricao": descricao_produto
        })

        if resultado_consulta:
            # Extrai o código e descrição do produto e cria um objeto Produto
            codigo = resultado_consulta["codigo"]
            descricao = resultado_consulta["descricao"]
            produto = Produto(codigo=codigo, descricao=descricao)
    
            self.mongo.close()
            return produto
        
        self.mongo.close()
        return None


     
    def busca_produto_codigo(self, codigo: int) -> Produto:
        """
        Busca um produto pelo seu código.

        Args:
            codigo (int): O código do produto.

        Returns:
            Produto: O objeto Produto encontrado ou None se não existir.

        """

        self.mongo.connect()
        # Executa a consulta
        resultado_consulta = self.mongo.db['produtos'].find_one({
            "codigo": codigo
        })

        if resultado_consulta:
            # Extrai o código e descrição do produto e cria um objeto Produto
            codigo = resultado_consulta["codigo"]
            descricao = resultado_consulta["descricao"]
            produto = Produto(codigo=codigo, descricao=descricao)
        
            self.mongo.close()
            return produto
        
        self.mongo.close()
        return None

if __name__ == "__main__":
    # controller_produto = ControllerProduto()
    # produtos_perim, produtos_extrabom = controller_produto.inserir_produto("Exemplo")
    # if produtos_perim and produtos_extrabom:
    #     print(f"Produtos encontrados: Perim - {produtos_perim}, Extrabom - {produtos_extrabom}")
    ...