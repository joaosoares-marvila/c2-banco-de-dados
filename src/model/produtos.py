class Produto:
    # --------- Construtor --------- 
    def __init__(self, 
                 codigo:int=None, 
                 descricao:str=None
                 ):
        self._codigo = int(codigo)
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
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self._descricao = descricao

    # --------- String --------- 
    def __str__(self) -> str:
        return f"Descrição: {self.descricao}"