# Não me orgulho dessa importação :(
import sys

import os
from pathlib import Path

diretorio_atual = Path(__file__).resolve()
diretorio_src = diretorio_atual.parent.parent

sys.path.append(diretorio_src)
from model.mercados import Mercado
from model.produtos import Produto
from model.produtos_mercados import ProdutoMercado

# Utils
from tasks.utils.utils import (
    busca_elemento_XPATH,
    busca_elemento_CLASS,
    formata_preco
)

class Extrabom(Mercado):
    """
    Classe que representa a automatização de tarefas relacionadas ao mercado Extrabom.

    Esta classe herda da classe Mercado e implementa a tarefa específica do mercado Extrabom.
    Ela busca produtos de referência na plataforma e coleta informações relevantes, como URL, título e preço.

    Attributes:
    - nome (str): O nome do mercado (Extrabom).
    - url (str): A URL base de pesquisa do mercado Extrabom.
    - produtos_referencia (list): Uma lista de produtos de referência para buscar no mercado.

    Methods:
    - busca_produto(produto: Produto) -> ProdutoMercado: Busca um produto no mercado Extrabom e retorna um objeto ProdutoMercado.

    Exemplo de uso:
    >>> extrabom = Extrabom()
    >>> extrabom.busca_produto(produto)
    """

    def __init__(self) -> None:
        super().__init__(
            codigo = 2,
            nome = 'ExtraBom'
        )
        
    def busca_produto(self, produto: Produto) -> ProdutoMercado:
        """
        Busca um produto no mercado Extrabom e retorna um objeto ProdutoMercado.

        Args:
        - produto (Produto): O produto a ser buscado no mercado.

        Returns:
        - ProdutoMercado: O objeto ProdutoMercado com informações do produto encontrado no mercado Extrabom.
        """
        try:
            self.driver.get(f'{"https://www.extrabom.com.br/busca/?q="}{produto.descricao}')

            # --------- Busca produto ---------
            # Recupera url do produto
            url_produto = busca_elemento_XPATH(self.driver, '//*[@id="conteudo"]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/a').get_attribute('href')
            self.driver.get(url_produto)
            
            # Recupera título do produto
            descricao_produto = busca_elemento_XPATH(self.driver, '//*[@id="conteudo"]/div[2]/div/div/div/div[2]/div/h1').text

            # Recupera preço do produto
            valor_unitario_produto = busca_elemento_CLASS(self.driver, 'valor').text
            valor_unitario_produto = formata_preco(valor_unitario_produto)
            
            # Recupera o código do produto
            codigo_produto = url_produto.split('/')[-2]

            # Instancia o objeto ProdutoMercado
            produto_mercado = ProdutoMercado(codigo=codigo_produto, descricao=descricao_produto, produto=produto, mercado=self, valor_unitario=valor_unitario_produto)

            return produto_mercado

        except Exception as e:
            print(e)
            return None

if __name__ == '__main__':
    # Extrabom
    # extrabom = Extrabom()
    # produto = Produto(descricao='Feijão')  # Substitua 'Feijão' pelo nome do produto desejado
    # produto_mercado = extrabom.busca_produto(produto)
    # if produto_mercado:
    #     print(f"Produto encontrado no mercado Extrabom: {produto_mercado.descricao}")
    # else:
    #     print("Produto não encontrado no mercado Extrabom.")
    ...