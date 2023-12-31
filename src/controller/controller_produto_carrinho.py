import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from model.produtos_carrinho import ProdutoCarrinho
from controller.controller_produto import ControllerProduto
from controller.controller_produto_mercado import ControllerProdutoMercado
from conexion.oracle_queries import OracleQueries

from pandas import DataFrame


class ControllerProdutoCarrinho:
    def __init__(self):
        pass

    @staticmethod
    def adicionar_produto():
        """
        Permite ao usuário adicionar um produto ao carrinho de compras, escolhendo a quantidade e o mercado.

        Esta função inicia a conexão com o banco de dados, permite ao usuário inserir o nome do produto,
        busca informações sobre o produto nos mercados Perim e ExtraBom, oferece opções com base na disponibilidade
        e permite que o usuário escolha o mercado e a quantidade desejados para adicionar ao carrinho.

        A função executa as seguintes etapas:
        1. Inicializa a conexão com o banco de dados.
        2. Solicita ao usuário que insira a descrição do produto desejado.
        3. Valida se o usuário digitou alguma descrição.
        4. Insere o produto no carrinho de compras, permitindo ao usuário escolher o mercado e a quantidade.
        5. Fecha a conexão com o banco de dados.

        """
        # Inicializa a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicitar ao usuário que insira a descrição do produto que deseja buscar
        descricao_produto = input("Digite o nome do produto que deseja inserir: ")

        # Valida se o usuário digitou algo
        if descricao_produto:

            # Retorna um objeto Produto
            produto = ControllerProduto.inserir_produto(oracle=oracle, descricao_produto=descricao_produto)

            # Busca informações sobre o produto nos mercados Perim e ExtraBom
            produto_perim, produto_extrabom = ControllerProdutoMercado.busca_produtos_mercados(oracle=oracle, produto=produto)

            # Produto encontrado em ambos os mercados
            if produto_perim and produto_extrabom:

                # Menu de opções
                print(f'\nForam encontrados produtos em ambos os mercados referentes ao produto "{produto.descricao}".')
                print(f' [1] \t {str(produto_perim)}')
                print(f' [2] \t {str(produto_extrabom)}')
                print(f' [0] - \t Sair')

                # Usuário escolhe a opção desejada
                opcao = input('Selecione a opção desejada: ').strip()

                # Valida a opção escolhida pelo usuário
                if opcao == '1':  # Produto do mercado Perim

                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                    # Insira o produto no carrinho (mercado Perim)
                    oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_perim.codigo}, {quantidade})")
                    print(f'{quantidade} unidades do produto {produto_perim.descricao} foram adicionadas ao carrinho.')
                
                elif opcao == '2':  # Produto do mercado ExtraBom
                    
                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                    # Insira o produto no carrinho (mercado ExtraBom)
                    oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_extrabom.codigo}, {quantidade})")
                    print(f'{quantidade} unidades do produto {produto_extrabom.descricao} foram adicionadas ao carrinho.')
                
                elif opcao == '0':  # Sair do menu
                    
                    print('Saindo do menu de produtos.')
                
                else:  # Opção inválida

                    print('Opção inválida. Voltando para a tela inicial.')

            # Produto encontrado apenas no mercado Perim
            elif produto_perim:

                # Menu de opções
                print(f'Foram encontrados produtos apenas no mercado Perim referentes ao produto {str(produto)}.')
                print(f' [1] \t {str(produto_perim)}')
                print(f' [0] - \t Sair')

                # Usuário escolhe a opção desejada
                opcao = input('Selecione a opção desejada: ').strip()

                # Valida a opção escolhida pelo usuário
                if opcao == '1':  # Produto do mercado Perim

                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                    # Insira o produto no carrinho (mercado Perim)
                    oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_perim.codigo}, {quantidade})")
                    print(f'{quantidade} unidades do produto {produto_perim.descricao} foram adicionadas ao carrinho.')
                
                elif opcao == '0':  # Sair do menu

                    print('Saindo do menu de produtos.')
                
                else:  # Opção inválida

                    print('Opção inválida. Voltando para a tela inicial.')

            # Produto encontrado apenas no mercado ExtraBom
            elif produto_extrabom:

                # Menu de opções
                print(f'Foram encontrados produtos apenas no mercado ExtraBom referentes ao produto {str(produto)}.')
                print(f' [1] - \t {str(produto_extrabom)}')
                print(f' [0] - \t Sair')

                # Usuário escolhe a opção desejada
                opcao = input('Selecione a opção desejada: ').strip()

                if opcao == '1':  # Produto do mercado ExtraBom
                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                    # Insira o produto no carrinho (mercado Perim)
                    oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_extrabom.codigo}, {quantidade})")
                    print(f'{quantidade} unidades do produto {produto_extrabom.descricao} foram adicionadas ao carrinho.')
                
                elif opcao == '0':  # Sair do menu
                    print('Saindo do menu de produtos.')
                
                else:  # Opção inválida
                    print('Opção inválida. Voltando para a tela inicial.')

            # Não foi encontrado nenhum produto em ambos os mercados
            else:
                print(f'Não foi encontrado nenhum produto referente a {str(produto)}.')
                print('Voltando para a tela inicial.')

        oracle.close()

    @staticmethod
    def alterar_carrinho():
        """
        Permite ao usuário fazer alterações em um produto do carrinho de compras, incluindo a modificação da quantidade ou a escolha de um produto diferente do mercado.

        Esta função inicia a conexão com o banco de dados, exibe as opções disponíveis ao usuário e permite as alterações desejadas no produto do carrinho.

        A função executa as seguintes etapas:
        1. Inicializa a conexão com o banco de dados.
        2. Valida se há produtos no carrinho de compras.
        3. Lista todos os produtos no carrinho.
        4. Permite que o usuário escolha um produto no carrinho com base em seu código.
        5. Oferece opções para alterar a quantidade do produto ou escolher um produto diferente do mercado.
        6. Executa as alterações escolhidas pelo usuário.
        7. Fecha a conexão com o banco de dados.

        """

        # Inicializa a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Valida se foi encontrado algum produto no carrinho de compras
        produtos_carrinho = ControllerProdutoCarrinho.get_produtos_carrinho(oracle=oracle)

        if produtos_carrinho is not None:

            # Lista todos os produtos presentes no carrinho de compras
            ControllerProdutoCarrinho.lista_todos_produtos(oracle=oracle)

            # Usuário escolhe a opção desejada
            codigo_pruto_escolhido = int(input('\nDigite o código do produto que deseja alterar: '))

            # DataFrame do produto escolhido
            produto_escolhido = ControllerProdutoCarrinho.get_produto_por_codigo(oracle=oracle, codigo=codigo_pruto_escolhido)

            # Valida se foi encontrado algum produto no carrinho de compras com o código determinado
            if produto_escolhido is not None:
                
                # Converte o DataFrame em variáveis
                codigo_produto_carrinho = produto_escolhido.iloc[0]['codigo']
                codigo_produto = produto_escolhido.iloc[0]['codigo_produto']
                codigo_produto_mercado = produto_escolhido.iloc[0]['codigo_produto_mercado']
                quantidade = produto_escolhido.iloc[0]['quantidade']

                # Exibe opções
                print('\n[1] Alterar quantidade')
                print('[2] - Alterar produto (mercado)')
                print('[0] Sair')
                
                # Usuário escolhe a opção desejada
                opcao = input("\nDigite o número da opção desejada: ")
                
                if opcao == '1':  # Alterar quantidade
                
                    # Nova quantidade do produto que já está presente no carrinho
                    nova_quantidade = int(input('Digite a quantidade desejada: '))
                    
                    # Verifica se a quantidade é maior que zero
                    if quantidade > 0:  
                        
                        oracle.write(f'UPDATE produtos_carrinho SET quantidade = {nova_quantidade} WHERE codigo = {codigo_produto_carrinho}')
                        print('\nProduto atualizado! Voltando para a tela inicial...')
                    
                    else:

                        print('\nNão é possível definir a quantidade como 0, volte ao menu principal e retire o produto do seu carrinho')

                elif opcao == '2':  # Alterar produto (mercado)
                    
                    # Instancia um objeto Produto
                    produto = ControllerProduto.busca_produto_codigo(oracle=oracle, codigo=codigo_produto)
                    
                    # Instancia dois objetos ProdutoMercado referentes aos mercados Perim e ExtraBom
                    produto_perim, produto_extrabom = ControllerProdutoMercado.busca_produtos_mercados_db(oracle=oracle, produto=produto)

                    # Mensagem informativa
                    print('\nProdutos disponíveis: ')
                    
                    # Os produtos de ambos os mercados estão disponíveis
                    if produto_extrabom and produto_perim:
                        
                        # Menu de opções
                        print(f'[1] {str(produto_perim)}')
                        print(f'[2] {str(produto_extrabom)}')
                        print(f'[3] Cancela alteração')
                    
                        # Usuário escolhe a opção desejada
                        opcao = input('Digite o código do produto que deseja: ')
                        
                        if opcao == '1':  # Produto Perim

                            oracle.write(f"UPDATE produtos_carrinho SET codigo_produto_mercado = '{produto_perim.codigo}' WHERE codigo = {codigo_pruto_escolhido}")
                            print(f"\nCarrinho alterado.")
                        
                        elif opcao == '2':  # Produto ExtraBom
                            oracle.write(f"UPDATE produtos_carrinho SET codigo_produto_mercado = '{produto_extrabom.codigo}' WHERE codigo = {codigo_pruto_escolhido}")
                            print(f"\nCarrinho alterado.")
                        
                        elif opcao == '3':  # Cancela alteração
                            print("\nVoltando para o menu inicial...")
                        
                        else:  # Opção inválida
                            print("\nOpção inválida, voltando para o menu inicial...")

                    # Apenas o produto do mercado Perim está disponível
                    elif produto_perim:
                        
                        # Menu de opções
                        print(f'[1] {str(produto_perim)}')
                        print(f'[2] Cancela alteração')
                        
                        # Usuário escolhe a opção desejada
                        opcao = input('Digite o código do produto que deseja: ')

                        if opcao == '1':  # Produto Perim
                        
                            oracle.write(f"UPDATE produtos_carrinho SET codigo_produto_mercado = '{produto_perim.codigo}' WHERE codigo = {codigo_pruto_escolhido}")
                            print(f"\nCarrinho alterado.")
                        
                        elif opcao == '2':  # Cancela alteração
                        
                            print("\nVoltando para o menu inicial...")
                        
                        else:  # Opção inválida
                        
                            print("\nOpção inválida, voltando para o menu inicial...")

                    # Apenas o produto do mercado ExtraBom está disponível
                    elif produto_extrabom:

                        # Menu de opções
                        print(f'[1] - {str(produto_extrabom)}')
                        print(f'[2] - Cancela alteração')
                        
                        # Usuário escolhe a opção desejada
                        opcao = input('Digite o código do produto que deseja: ')

                        if opcao == '1':  # Produto ExtraBom

                            oracle.write(f"UPDATE produtos_carrinho SET codigo_produto_mercado = '{produto_extrabom.codigo}' WHERE codigo = {codigo_pruto_escolhido}")
                            print(f"\nCarrinho alterado.")
                        
                        elif opcao == '2':  # Cancela alteração

                            print("\nVoltando para o menu inicial...")
                        
                        else:  # Opção inválida
                        
                            print("\nOpção inválida, voltando para o menu inicial...")

                elif opcao  == '0':  # Sair do menu
                    
                    print('\nVoltando ao menu inicial...')

                else:  # Código inválido

                    print('\nCódigo inválido. Voltando ao menu inicial...')

            else:  # Código inválido
                print('\nCódigo inválido. Voltando ao menu inicial...')

        else:
            print('\nNão foi encontrado nenhum produto no carrinho de compras.')

        oracle.close()

    @staticmethod
    def excluir_produto():
        """
        Permite ao usuário excluir um produto do carrinho de compras.

        Esta função interage com o usuário para listar os produtos no carrinho, permitir a escolha de um produto e,
        em seguida, confirmar a exclusão desse produto.

        Args:
            Nenhum (usa uma conexão existente em OracleQueries).

        Returns:
            Nenhum.
        """
        # Inicializa a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Valida se foi encontrado algum produto no carrinho de compras
        produtos_carrinho = ControllerProdutoCarrinho.get_produtos_carrinho(oracle=oracle)

        if produtos_carrinho is not None:
            # Lista todos os produtos presentes no carrinho de compras
            ControllerProdutoCarrinho.lista_todos_produtos(oracle=oracle)

            # Usuário escolhe a opção desejada
            codigo_pruto_escolhido = int(input('\nDigite o código do produto que deseja retirar do carrinho: '))

            # Obtém informações sobre o produto selecionado
            produto_escolhido = ControllerProdutoCarrinho.get_produto_por_codigo(oracle=oracle, codigo=codigo_pruto_escolhido)

            # Valida se foi encontrado algum produto no carrinho de compras com o código determinado
            if produto_escolhido is not None:
                # Confirmação da exclusão
                print(f"\nVocê realmente deseja retirar o produto {produto_escolhido.iloc[0]['descricao_produto_mercado']} do seu carrinho?")
                confirma_exclusao = input(f"Digite 'sim' para confirmar: ")

                if confirma_exclusao.lower().strip() == 'sim':
                    # Exclui o produto do carrinho
                    oracle.write(f"DELETE FROM produtos_carrinho WHERE codigo = {produto_escolhido.iloc[0]['codigo']}")
                    print("\nProduto retirado com sucesso!")
                else:
                    print('\nRetirada cancelada. Voltando ao menu inicial...')
            else:
                print('\nProduto não encontrado, voltando ao menu inicial...')
        else:
            print('\nNão há produtos no carrinho, voltando ao menu inicial...')

        # Fecha a conexão com o banco de dados
        oracle.close()

    @staticmethod
    def lista_todos_produtos(oracle=OracleQueries) -> bool:
        """
        Lista todos os produtos presentes no carrinho de compras.

        Esta função obtém os produtos no carrinho de compras, formata as informações e imprime a lista na tela.

        Args:
            oracle (OracleQueries, optional): Objeto de conexão Oracle. Defaults to OracleQueries.

        Returns:
            bool: True se há produtos no carrinho, False caso contrário.
        """

        # Busca produtos presentes no carrinho de compras
        produtos_carrinho = ControllerProdutoCarrinho.get_produtos_carrinho(oracle=oracle)

        if len(produtos_carrinho) > 0:

            # Mensagem informativa
            print("Produtos presentes no carrinho de compras:\n")

            # Itera os produtos presentes no carrinho de compras
            for index, row in produtos_carrinho.iterrows():
                codigo = row['codigo']
                descricao_produto_mercado = row['descricao_produto_mercado']
                valor_unitario = row['valor_unitario']
                quantidade = row['quantidade']
                total = valor_unitario * quantidade

                # Imprimindo os valores formatados
                print(f"Código: {codigo:<5} | Produto: {descricao_produto_mercado:<30} | Valor unitário: {valor_unitario:<8.2f} | Quantidade: {quantidade:<5} | Total:{total:<10.2f}")

            return True

        else:

            print("Não há nenhum produto presente no carrinho de compras.")

            return False

    @staticmethod
    def get_produtos_carrinho(oracle: OracleQueries) -> DataFrame:
        """
        Obtém os produtos presentes no carrinho de compras.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.

        Returns:
            DataFrame: DataFrame contendo informações sobre os produtos no carrinho.

        Os campos retornados no DataFrame:
        - codigo: Código do produto no carrinho de compras.
        - quantidade: Quantidade do produto no carrinho.
        - codigo_produto: Código do produto.
        - descricao_produto: Descrição do produto.
        - codigo_produto_mercado: Código do produto no mercado.
        - descricao_produto_mercado: Descrição do produto no mercado.
        - valor_unitario: Valor unitário do produto no mercado.

        Retorna None se não houver nenhum produto no carrinho.
        """
        produtos_carrinho = oracle.sqlToDataFrame(query='SELECT pc.codigo as codigo, pc.quantidade, p.codigo as codigo_produto, p.descricao as descricao_produto, pm.codigo as codigo_produto_mercado, pm.descricao as descricao_produto_mercado, pm.valor_unitario FROM produtos_carrinho pc INNER JOIN produtos_mercados pm ON pc.codigo_produto_mercado = pm.codigo INNER JOIN produtos p ON pm.codigo_produto = p.codigo')

        if len(produtos_carrinho) > 0:
            return produtos_carrinho
        else:
            return None


    @staticmethod
    def get_produto_por_codigo(oracle: OracleQueries, codigo: int) -> DataFrame:
        """
        Obtém um produto específico do carrinho de acordo com o código.

        Args:
            oracle (OracleQueries): Objeto de conexão Oracle.
            codigo (int): O código do produto a ser recuperado.

        Returns:
            DataFrame: DataFrame contendo informações sobre o produto no carrinho.

        Os campos retornados no DataFrame:
        - codigo: Código do produto no carrinho de compras.
        - quantidade: Quantidade do produto no carrinho.
        - codigo_produto: Código do produto.
        - descricao_produto: Descrição do produto.
        - codigo_produto_mercado: Código do produto no mercado.
        - descricao_produto_mercado: Descrição do produto no mercado.
        - valor_unitario: Valor unitário do produto no mercado.

        Retorna None se o produto não for encontrado no carrinho.
        """
        
        produtos_carrinho = oracle.sqlToDataFrame(f'SELECT pc.codigo as codigo, pc.quantidade, p.codigo as codigo_produto, p.descricao as descricao_produto, pm.codigo as codigo_produto_mercado, pm.descricao as descricao_produto_mercado, pm.valor_unitario FROM produtos_carrinho pc INNER JOIN produtos_mercados pm ON pc.codigo_produto_mercado = pm.codigo INNER JOIN produtos p ON pm.codigo_produto = p.codigo WHERE pc.codigo = {codigo}')

        if len(produtos_carrinho) > 0:
            return produtos_carrinho
        else: 
            return None


if __name__ == "__main__":
    ControllerProdutoCarrinho.adicionar_produto()
    # ControllerProdutoCarrinho.alterar_carrinho()
    # ControllerProdutoCarrinho.excluir_produto()
    ...