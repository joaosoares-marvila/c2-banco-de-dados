from utils import config
from utils import splash_screen
from controller import carrinho_controller
from controller import mercado_controller
from controller import produto_controller
from controller import produto_mercado_controller
from reports import relatorio

# DECLARANDO OBJS
tela_inicial = splash_screen()
relatorio = relatorio()
produto = produto_controller()
mercado = mercado_controller()
carrinho = carrinho_controller()
produto_mercado = produto_mercado_controller()

# CHAMADA MENU PRODUTOS
def produtos(opcao_produtos:int=0):

    if opcao_produtos == 1:
        novo_produto = produto.inserir_produto()           
    elif opcao_produtos == 2:
        remover = produto.remover_produto()
    elif opcao_produtos == 3:
        editar_produto = produto.editar_produto()
    elif opcao_produtos == 4:
        procurar_produto = produto.procurar_produto()

# CHAMADA MENU RELATÓRIOS
def reports(opcao_relatorios:int=0):

    if opcao_relatorios == 1:
        relatorio.get_relatorio_produtos()
    elif opcao_relatorios == 2:
        relatorio.get_relatorio_mercados()
    elif opcao_relatorios == 3:
        relatorio.get_relatorio_pedidos()
    elif opcao_relatorios == 4:
        relatorio.get_relatorio_pedidos_mercado()

# CHAMADA MENU ENTIDADES
def entidades(opcao_entidades:int=0):

    if opcao_entidades == 1:
        produto.get_relatorio_produtos()
    elif opcao_entidades == 2:
        mercado.get_relatorio_mercados()
    elif opcao_entidades == 3:
        carrinho.get_relatorio_pedidos()
    elif opcao_entidades == 4:
        produto_mercado.get_relatorio_pedidos_mercado()

# CHAMADA DE PEDIDOS -> FALTA CRIAR O CONTROLLER, VOU DEIXAR VAZIO E DPS EU TERMINO
# def pedidos(opcao_excluir:int=0):



def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-4]: "))
        config.clear_console(1)
        
        # MENU PRODUTOS
        if opcao == 1:
            
            print(config.MENU_PRODUTOS)
            opcao_produtos = int(input("Escolha uma opção [0-4]: "))
            config.clear_console(1)

            reports(opcao_produtos)

            config.clear_console(1)

        # MENU RELATÓRIOS
        elif opcao == 2:
            
            print(config.MENU_RELATORIOS)
            opcao_relatorios = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            relatorio(opcao_relatorios=opcao_relatorios)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        # MENU ENTIDADES
        elif opcao == 3:

            print(config.MENU_ENTIDADES)
            opcao_entidades = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            entidades(opcao_entidades=opcao_entidades)

            config.clear_console()

        #SAIR DO SISTEMA
        elif opcao == 4:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Encerrando o sistema...")
            exit(0)

        else:
            print("Opção incorreta!")
            exit(1)

if __name__ == "__main__":
    run()