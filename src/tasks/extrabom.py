# Loguru
from loguru import logger

# Não me orgulho dessa importação :(
import sys
sys.path.append('c:\\Users\\joaos\\Desktop\\Banco de dados\\c2-banco-de-dados\\src')
from model.mercados import Mercado
from model.produtos import Produto

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
    - run(driver: webdriver.Chrome): Executa a tarefa principal de automação no mercado Extrabom.

    Exemplo de uso:
    >>> extrabom = Extrabom()
    >>> extrabom.run(webdriver.Chrome(options))
    """

    def __init__(self) -> None:

        super().__init__(
            codigo = 2,
            url = 'https://www.extrabom.com.br/busca/?q=',
            nome = 'ExtraBom'
        )
        
    def busca_produto(self, produto: Produto) -> None:

        # --------- Iniciando task ---------
        try:

            self.driver.get(f'{self.url}{produto.descricao}')


            # --------- Busca produto ---------
            # Recupera url do produto
            url_produto = busca_elemento_XPATH(self.driver, '//*[@id="conteudo"]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/a').get_attribute('href')
            self.driver.get(url_produto)
            
            # Recupera titulo do produto
            descricao_produto = busca_elemento_XPATH(self.driver, '//*[@id="conteudo"]/div[2]/div/div/div/div[2]/div/h1').text

            # Recupera preco do produto
            valor_unitario_produto = busca_elemento_CLASS(self.driver, 'valor').text
            valor_unitario_produto = formata_preco(valor_unitario_produto)
            
            # Recupera o codigo do produto
            codigo_produto = url_produto.split('/')[-2]

            # Instancia o produto
            produto_mercado = ProdutoMercado(codigo=codigo_produto, descricao=descricao_produto, produto=produto, mercado=self, valor_unitario=valor_unitario_produto)

            return produto_mercado

        except:
            return None

if __name__ == '__main__':
    

    # ExtaBom
    extrabom = Extrabom()
    extrabom.busca_produto(produto='Feijão')


