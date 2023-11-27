from src.utils import config
from src.utils.splash_screen import SplashScreen
from src.controller.controller_produto_carrinho import ControllerProdutoCarrinho
from src.controller.controller_mercado import ControllerMercado 
from src.controller.controller_produto import ControllerProduto
from src.controller.controller_produto_mercado import ControllerProdutoMercado
from src.reports.relatorios import Relatorio

# DECLARANDO OBJS
tela_inicial = SplashScreen()
relatorio = Relatorio()
produto_ca = ControllerProduto()
mercado = ControllerMercado()
produtos_carrinho = ControllerProdutoCarrinho()
produto_mercado = ControllerProdutoMercado()

# CHAMADA MENU PRODUTOS
def menu_principal(opcao:int=0):

    if opcao == 1:
        adicionar_produto = produtos_carrinho.adicionar_produto()
    elif opcao == 2:
        editar_produto = produtos_carrinho.alterar_carrinho()
    elif opcao == 3:
        remover_produto = produtos_carrinho.excluir_produto()

# CHAMADA MENU RELATÓRIOS
def relatorios(opcao:int=0):

    if opcao == 1:
        relatorio.get_relatorio_produtos()
    elif opcao == 2:
        relatorio.get_relatorio_mercados()
    elif opcao == 3:
        relatorio.get_relatorio_produtos_mercados()
    elif opcao == 4:
        relatorio.get_relatorio_produtos_carrinho()
    elif opcao == 5:
        relatorio.get_total_por_mercado()

    input()
        
# MÉTODO PRINCIPAL
def run():

    print(tela_inicial.get_updated_screen())
    config.clear_console(1)

    while True:

        # Menu principal
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-4]: "))
        config.clear_console(1)

        # Adicionar novo produto ao carrinho
        if opcao == 1:

            while True:

                menu_principal(opcao=opcao)
                config.clear_console()
                
                print(tela_inicial.get_updated_screen())
                config.clear_console()

                continuar = input('Deseja inserir mais algum registro? digite "SIM" para inserir, digite "NAO" para voltar ao menu de opções: ')

                if continuar.lower() == 'nao':
                    config.clear_console()
                    break

        # Alterar produtos
        elif opcao == 2:
            
            while True:

                menu_principal(opcao=opcao)
                config.clear_console()
                
                print(tela_inicial.get_updated_screen())
                config.clear_console()

                continuar = input('Deseja atualizar mais algum registro? digite "SIM" para atualizar, digite "NAO" para voltar ao menu de opções: ')

                if continuar.lower() == 'nao':
                    config.clear_console()
                    break

        # Remover produtos
        elif opcao == 3:
            
            while True:
                menu_principal(opcao=opcao)
                config.clear_console()
                
                print(tela_inicial.get_updated_screen())
                config.clear_console()

                continuar = input('Deseja remover mais algum registro? digite "SIM" para remover, digite "NAO" para voltar ao menu de opções: ')

                if continuar.lower() == 'nao':
                    config.clear_console()
                    break

        # Relatórios
        elif opcao == 4:
            while True:
                print(config.MENU_RELATORIOS)
                opcao_relatorio = int(input("Escolha uma opção [0-5]: "))
                config.clear_console()

                relatorios(opcao=opcao_relatorio)
                config.clear_console()
                
                print(tela_inicial.get_updated_screen())
                config.clear_console()

                continuar = input('Deseja remover mais algum registro? digite "SIM" para remover, digite "NAO" para voltar ao menu de opções: ')

                if continuar.lower() == 'nao':
                    config.clear_console()
                    break

        # Sair do sistema
        elif opcao == 0:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Encerrando o sistema...")
            exit(0)

        else:
            print("Opção incorreta!")
            exit(1)

if __name__ == "__main__":
    run()