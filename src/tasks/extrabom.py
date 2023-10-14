# Loguru
from loguru import logger

# Não me orgulho dessa importação :(
import sys
sys.path.append('c:\\Users\\joaos\\Desktop\\Banco de dados\\c2-banco-de-dados\\src')
from model.mercados import Mercado
from model.produtos import Produto


# Utils
from tasks.utils.utils import (
    config,
    busca_elemento_XPATH,
    busca_elemento_CLASS,
    formata_preco
)

configuracoes = config()

class Extrabom(Mercado):
    """
    Classe que representa a automatização de tarefas relacionadas ao mercado Extrabom.

    Esta classe herda da classe Mercado e implementa a tarefa específica do mercado Extrabom.
    Ela busca produtos de referência na plataforma e coleta informações relevantes, como URL, título e preço.

    Attributes:
    - nome (str): O nome do mercado (Extrabom).
    - url (str): A URL base do mercado Extrabom.
    - produtos_referencia (list): Uma lista de produtos de referência para buscar no mercado.

    Methods:
    - run(driver: webdriver.Chrome): Executa a tarefa principal de automação no mercado Extrabom.

    Exemplo de uso:
    >>> extrabom = Extrabom()
    >>> extrabom.run(webdriver.Chrome(options))
    """

    def __init__(self) -> None:

        super().__init__(
            codigo = 1,
            url = configuracoes['EXTRABOM']['URL'],
            nome = 'ExtraBom'
        )
        
    def busca_produto(self, produto: str) -> None:

        # --------- Iniciando task ---------
        self.driver.get(f'{self.url}{produto}')


        # --------- Busca produto ---------
        # Recupera url do produto
        url_produto = busca_elemento_XPATH(self.driver, configuracoes['EXTRABOM']['XPATH_URL_PRODUTO']).get_attribute('href')
        self.driver.get(url_produto)
        
        # Recupera titulo do produto
        titulo_produto = busca_elemento_XPATH(self.driver, configuracoes['EXTRABOM']['XPATH_TITULO_PRODUTO']).text

        # Recupera preco do produto
        valor_unitario_produto = busca_elemento_CLASS(self.driver, configuracoes['EXTRABOM']['CLASS_VALOR_UNITARIO_PRODUTO']).text
        valor_unitario_produto = formata_preco(valor_unitario_produto)
        

        codigo_produto = url_produto.split('/')[-2]

        logger.info(f'Titulo: {titulo_produto}')
        logger.info(f'Código: {codigo_produto}')
        logger.info(f'Preço: {valor_unitario_produto}')
        logger.info(f'url: {url_produto}\n')

        return codigo_produto, titulo_produto, valor_unitario_produto, self.codigo


if __name__ == '__main__':
    
    
    # ExtaBom
    extrabom = Extrabom()
    extrabom.busca_produto(produto='Feijão')


