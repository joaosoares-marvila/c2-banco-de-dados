MENU_PRINCIPAL = """ --- MENU PRINCIPAL ---
[1] ADICIONAR PRODUTO AO CARRINHO
[2] ALTERAR PRODUTO DO CARRINHO
[3] REMOVER PRODUTO DO CARRINHO 
[4] RELATORIOS
[0] SAIR
"""

MENU_RELATORIOS = """ --- RELATORIOS ---
[1] PRODUTOS
[2] MERCADOS
[3] PRODUTOS DOS MERCADOS
[4] PRODUTOS DO CARRINHO
"""


QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("cls")
