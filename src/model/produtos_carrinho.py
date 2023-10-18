class ProdutoCarrinho:
    def __init__(self, codigo, codigo_produto_mercado, quantidade):
        self._codigo = codigo
        self._codigo_produto_mercado = codigo_produto_mercado
        self._quantidade = quantidade

    @property
    def codigo(self):
        return self._codigo_produto_carrinho

    @codigo.setter
    def codigo(self, codigo_produto_carrinho):
        self._codigo_produto_carrinho = codigo_produto_carrinho

    @property
    def codigo_produto_mercado(self):
        return self._codigo_produto_mercado

    @codigo_produto_mercado.setter
    def codigo_produto_mercado(self, codigo_produto_mercado):
        self._codigo_produto_mercado = codigo_produto_mercado

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    def __str__(self):
        return f"Código: {self._codigo_produto_carrinho} | Código Produto Mercado: {self._codigo_produto_mercado} | Quantidade: {self._quantidade}"
