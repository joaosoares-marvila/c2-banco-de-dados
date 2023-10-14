class Produto:
    # --------- Construtor --------- 
    def __init__(self, 
                 codigo:int=None, 
                 descricao:str=None
                 ):
        self._codigo = codigo
        self._descricao = descricao

    # --------- Código --------- 
    @property
    def codigo(self) -> int:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self._codigo = codigo
    
    # --------- Código --------- 
    @property
    def descricao(self) -> int:
        return self._codigo

    @descricao.setter
    def descricao(self, descricao: int) -> None:
        self._descricao = descricao

    # --------- Representação --------- 
    def __repr__(self) -> str:
        return f"Codigo: {self.get_codigo()} | Descrição: {self.get_descricao()}"