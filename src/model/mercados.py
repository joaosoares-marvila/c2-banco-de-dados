from abc import ABC, abstractmethod
from selenium.webdriver.chrome.options import Options
from selenium import webdriver



class Mercado:
    # --------- Construtor --------- 
    def __init__(self, codigo: int, nome: str) -> None:
        self._codigo = int(codigo)
        self._nome = nome
    
        # Driver
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        self.driver = webdriver.Chrome(options=options)

    # --------- Código --------- 
    @property
    def codigo(self) -> int:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self._codigo = codigo


    # --------- Nome --------- 
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome


    # --------- String --------- 
    def __str__(self) -> str:
        return f"Codigo: {self.codigo} | Nome: {self.nome}"


    # --------- Task para buscar produto --------- 
    @abstractmethod
    def busca_produto(self) -> tuple:
        """
        Método abstrato que deve ser implementado nas subclasses.

        Este método é responsável por executar a tarefa principal da classe que herda essa interface.
        Cada implementação concreta deve definir como a tarefa será realizada.

        Exemplo de uso (na implementação concreta):
        >>> class MeuMercado(Mercado):
        ...     def busca_produto(self):
        ...         # Implementação específica da tarefa para MeuMercado
        ...         pass  # Substitua 'pass' pela implementação real da tarefa.

        Returns:
            tuple: Uma tupla contendo (codigo_produto_mercado, valor_unitario, codigo_mercado).
        """
        return codigo_produto, titulo_produto, valor_unitario, codigo_mercado
