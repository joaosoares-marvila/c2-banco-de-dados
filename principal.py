from src.utils import config
from src.utils import splash_screen
from src.controller.controller_produto_carrinho import ControllerProdutoCarrinho
from src.controller.controller_mercado import ControllerMercado 
from src.controller.controller_produto import ControllerProduto
from src.controller.controller_produto_mercado import ControllerProdutoMercado
from sec.reports import relatorios

# DECLARANDO OBJS
tela_inicial = splash_screen()
relatorio = relatorio()
produto_ca = ControllerProduto()
mercado = ControllerMercado()
produtos_carrinho = ControllerProdutoCarrinho()
produto_mercado = ControllerProdutoMercado()

# CHAMADA MENU PRODUTOS
def carrinho(opcao_produtos:int=0):

    if opcao_produtos == 1:
        adicionar_produto = produtos_carrinho.adicionar_produto()          
    elif opcao_produtos == 2:
        remover_produto = produtos_carrinho.excluir_produto()
    elif opcao_produtos == 3:
        editar_produto = produtos_carrinho.alterar_carrinho()
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




def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-4]: "))
        config.clear_console(1)

        # MENU PRODUTOS
        if opcao == 1: #adicionar produtos

            print(config.MENU_PRODUTOS)
            opcao_produtos = int(input("Escolha uma opção [0-4]: "))
            config.clear_console(1)

            reports(opcao_produtos)

            config.clear_console(1)

        # MENU RELATÓRIOS
        elif opcao == 2: # alterar produtos

            print(config.MENU_RELATORIOS)
            opcao_relatorios = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            relatorio(opcao_relatorios=opcao_relatorios)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        # MENU ENTIDADES
        elif opcao == 3: # Remover produtos

            print(config.MENU_ENTIDADES)
            opcao_entidades = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            entidades(opcao_entidades=opcao_entidades)

            config.clear_console()

        #SAIR DO SISTEMA
        elif opcao == 4: # sair

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Encerrando o sistema...")
            exit(0)

        else:
            print("Opção incorreta!")
            exit(1)

if __name__ == "__main__":
    run()