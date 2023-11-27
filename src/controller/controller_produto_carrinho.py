import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas
from model.produtos_carrinho import ProdutoCarrinho
from controller.controller_produto import ControllerProduto
from controller.controller_produto_mercado import ControllerProdutoMercado
from conexion.mongo_queries import MongoQueries

from pandas import DataFrame


class ControllerProdutoCarrinho:
    def __init__(self):
        self.mongo = MongoQueries()

    def adicionar_produto(self):
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

        # Abre a conexão com o Mongo
        self.mongo.connect()

        # Solicitar ao usuário que insira a descrição do produto que deseja buscar
        descricao_produto = input("Digite o nome do produto que deseja inserir: ")

        ctrl_produto = ControllerProduto()
        ctrl_produto_mercado = ControllerProdutoMercado()

        # Valida se o usuário digitou algo
        if descricao_produto:
            
            # Retorna um objeto Produto
            produto = ctrl_produto.inserir_produto(descricao_produto=descricao_produto)

            # Busca informações sobre o produto nos mercados Perim e ExtraBom
            produto_perim, produto_extrabom = ctrl_produto_mercado.busca_produtos_mercados(produto=produto)

            # Obtém o próximo valor para o campo "codigo"
            ultimo_documento = self.mongo.db['produtos_carrinho'].find_one(sort=[("codigo", -1)])

            # Calcula o próximo código (incrementando 1 ao último código se existir, caso contrário, inicia em 1)
            proximo_codigo = (ultimo_documento["codigo"] + 1) if ultimo_documento else 1

            # Produto encontrado em ambos os mercados
            if produto_perim and produto_extrabom:

                # Menu de opções
                print(f'\nForam encontrados produtos em ambos os mercados referentes ao produto "{produto.descricao}".')
                print(f' [1] \t {str(produto_perim)}')
                print(f' [2] \t {str(produto_extrabom)}')
                print(f' [0] \t Sair')

                # Usuário escolhe a opção desejada
                opcao = input('Selecione a opção desejada: ').strip()

                # Produto do mercado Perim
                if opcao == '1':  

                    # Input de unidades(quantidade)
                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))

                    # Insere o produto no carrinho (mercado Perim)
                    self.mongo.db["produtos_carrinho"].insert_one({
                        "codigo": proximo_codigo,
                        "codigo_produto_mercado": produto_perim.codigo, 
                        "quantidade": quantidade
                    })

                    # Exibe mesagem de x produtos adicionados ao carrinho
                    print(f'{quantidade} unidades do produto {produto_perim.descricao} foram adicionadas ao carrinho.')

                # Produto do mercado ExtraBom
                elif opcao == '2':

                    # Input de unidades(quantidade)
                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))

                    # Insere o produto no carrinho (mercado ExtraBom)
                    self.mongo.db["produtos_carrinho"].insert_one({
                        "codigo": proximo_codigo,
                        "codigo_produto_mercado": produto_extrabom.codigo, 
                        "quantidade": quantidade
                    })

                    # Exibe mesagem de x produtos adicionados ao carrinho
                    print(f'{quantidade} unidades do produto {produto_extrabom.descricao} foram adicionadas ao carrinho.')

                # Sair do menu
                elif opcao == '0':

                    print('Saindo do menu de produtos.')

                # Opção inválida
                else:

                    print('Opção inválida. Voltando para a tela inicial.')

            # Produto encontrado apenas no mercado Perim
            elif produto_perim:

                # Menu de opções
                print(f'Foram encontrados produtos apenas no mercado Perim referentes ao produto {str(produto)}.')
                print(f' [1] \t {str(produto_perim)}')
                print(f' [0] \t Sair')

                # Usuário escolhe a opção desejada
                opcao = input('Selecione a opção desejada: ').strip()

                # Produto do mercado Perim
                if opcao == '1':

                    # Input de unidades(quantidade)
                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))

                    # Insere o produto no carrinho (mercado ExtraBom)
                    self.mongo.db["produtos_carrinho"].insert_one({
                        "codigo": proximo_codigo,
                        "codigo_produto_mercado": produto_perim.codigo, 
                        "quantidade": quantidade
                    })

                    # Exibe mesagem de x produtos adicionados ao carrinho
                    print(f'{quantidade} unidades do produto {produto_perim.descricao} foram adicionadas ao carrinho.')

                # Sair do menu
                elif opcao == '0':

                    print('Saindo do menu de produtos.')
                
                # Opção inválida
                else:

                    print('Opção inválida. Voltando para a tela inicial.')

            # Produto encontrado apenas no mercado ExtraBom
            elif produto_extrabom:

                # Menu de opções
                print(f'Foram encontrados produtos apenas no mercado ExtraBom referentes ao produto {str(produto)}.')
                print(f' [1] \t {str(produto_extrabom)}')
                print(f' [0] \t Sair')

                # Usuário escolhe a opção desejada
                opcao = input('Selecione a opção desejada: ').strip()

                # Produto do mercado ExtraBom
                if opcao == '1':  
                    
                    # Input de unidades(quantidade)
                    quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))

                    # Insere o produto no carrinho (mercado ExtraBom)
                    self.mongo.db["produtos_carrinho"].insert_one({
                        "codigo": proximo_codigo,
                        "codigo_produto_mercado": produto_extrabom.codigo, 
                        "quantidade": quantidade
                    })

                    # Exibe mesagem de x produtos adicionados ao carrinho
                    print(f'{quantidade} unidades do produto {produto_extrabom.descricao} foram adicionadas ao carrinho.')

                # Sair do menu
                elif opcao == '0':  

                    print('Saindo do menu de produtos.')
                
                # Opção inválida
                else:
                    print('Opção inválida. Voltando para a tela inicial.')

            # Não foi encontrado nenhum produto em ambos os mercados
            else:
                print(f'Não foi encontrado nenhum produto referente a {str(produto)}.')
                print('Voltando para a tela inicial.')

        self.mongo.close()



    def alterar_carrinho(self):
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

        self.mongo.connect()

        ctrl_produto_carrinho = ControllerProdutoCarrinho()
        ctrl_produto = ControllerProduto()
        ctrl_produto_mercado = ControllerProdutoMercado()
        

        # Valida se foi encontrado algum produto no carrinho de compras
        produtos_carrinho = ctrl_produto_carrinho.verifica_produtos_carrinho()

        if produtos_carrinho:

            # Lista todos os produtos presentes no carrinho de compras
            ctrl_produto_carrinho.lista_todos_produtos()

            # Usuário escolhe a opção desejada
            codigo_pruto_escolhido = int(input('\nDigite o código do produto que deseja alterar: '))

            # DataFrame do produto escolhido
            produto_escolhido = ctrl_produto_carrinho.get_produto_por_codigo(codigo=codigo_pruto_escolhido)

            # Valida se foi encontrado algum produto no carrinho de compras com o código determinado
            if produto_escolhido is not None:
                
                # Converte o DataFrame em variáveis
                codigo_produto_carrinho = produto_escolhido['codigo']
                codigo_produto = produto_escolhido['codigo_produto']
                codigo_produto_mercado = produto_escolhido['codigo_produto_mercado']
                quantidade = produto_escolhido['quantidade']

                # Exibe opções
                print('\n[1] Alterar quantidade')
                print('[2]  Alterar produto (mercado)')
                print('[0] Sair')
                
                # Usuário escolhe a opção desejada
                opcao = input("\nDigite o número da opção desejada: ")
                
                if opcao == '1':  # Alterar quantidade
                
                    # Nova quantidade do produto que já está presente no carrinho
                    nova_quantidade = int(input('Digite a quantidade desejada: '))
                    
                    # Verifica se a quantidade é maior que zero
                    if quantidade > 0:  
                        
                        self.mongo.db['produtos_carrinho'].update_one(
                            {"codigo": codigo_produto_carrinho},
                            {"$set": {"quantidade": nova_quantidade}}
                        )

                        ctrl_produto_carrinho.exibe_produto_atualizado(codigo_produto_carrinho)
                   
                    else:

                        print('\nNão é possível definir a quantidade como 0, volte ao menu principal e retire o produto do seu carrinho')

                elif opcao == '2':  # Alterar produto (mercado)
                    

                    # Instancia um objeto Produto
                    produto = ctrl_produto.busca_produto_codigo(codigo=codigo_produto)
                    
                    # Instancia dois objetos ProdutoMercado referentes aos mercados Perim e ExtraBom
                    produto_perim, produto_extrabom = ctrl_produto_mercado.busca_produtos_mercados_db(produto=produto)

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
                        
                        # Produto Perim
                        if opcao == '1':  
                            
                            self.mongo.db['produtos_carrinho'].update_one(
                                {"codigo": codigo_pruto_escolhido},
                                {"$set": {"codigo_produto_mercado": produto_perim.codigo}}
                            )
                            
                            print(f"\nCarrinho alterado.")
                        
                        # Produto ExtraBom
                        elif opcao == '2':

                            self.mongo.db['produtos_carrinho'].update_one(
                                {"codigo": codigo_pruto_escolhido},
                                {"$set": {"codigo_produto_mercado": produto_extrabom.codigo}}
                            )
                            
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
                            
                            self.mongo.db['produtos_carrinho'].update_one(
                                {"codigo": codigo_pruto_escolhido},
                                {"$set": {"codigo_produto_mercado": produto_perim.codigo}}
                            )
                            
                            print(f"\nCarrinho alterado.")
                        
                        elif opcao == '2':  # Cancela alteração
                        
                            print("\nVoltando para o menu inicial...")
                        
                        else:  # Opção inválida
                        
                            print("\nOpção inválida, voltando para o menu inicial...")

                    # Apenas o produto do mercado ExtraBom está disponível
                    elif produto_extrabom:

                        # Menu de opções
                        print(f'[1] {str(produto_extrabom)}')
                        print(f'[2] Cancela alteração')
                        
                        # Usuário escolhe a opção desejada
                        opcao = input('Digite o código do produto que deseja: ')

                        # Produto ExtraBom
                        if opcao == '1':
                            
                            self.mongo.db['produtos_carrinho'].update_one(
                                {"codigo": codigo_pruto_escolhido},
                                {"$set": {"codigo_produto_mercado": produto_extrabom.codigo}}
                            )

                            print(f"\nCarrinho alterado.")

                        # Cancela alteração
                        elif opcao == '2':

                            print("\nVoltando para o menu inicial...")
                        
                        # Opção inválida
                        else:
                        
                            print("\nOpção inválida, voltando para o menu inicial...")

                elif opcao  == '0':  # Sair do menu
                    
                    print('\nVoltando ao menu inicial...')

                else:  # Código inválido

                    print('\nCódigo inválido. Voltando ao menu inicial...')

            else:  # Código inválido
                print('\nCódigo inválido. Voltando ao menu inicial...')

        else:
            print('\nNão foi encontrado nenhum produto no carrinho de compras.')
        
        self.mongo.close()


    def excluir_produto(self):
        """
        Permite ao usuário excluir um produto do carrinho de compras.

        Esta função interage com o usuário para listar os produtos no carrinho, permitir a escolha de um produto e,
        em seguida, confirmar a exclusão desse produto.

        Args:
            Nenhum.

        Returns:
            Nenhum.
        """

        self.mongo.connect()

        ctrl_produto_carrinho = ControllerProdutoCarrinho()


        # Valida se foi encontrado algum produto no carrinho de compras
        produtos_carrinho = ctrl_produto_carrinho.verifica_produtos_carrinho()

        if produtos_carrinho:
            # Lista todos os produtos presentes no carrinho de compras
            ctrl_produto_carrinho.lista_todos_produtos()

            # Usuário escolhe a opção desejada
            codigo_pruto_escolhido = int(input('\nDigite o código do produto que deseja retirar do carrinho: '))

            # Obtém informações sobre o produto selecionado
            produto_escolhido = ctrl_produto_carrinho.get_produto_por_codigo(codigo=codigo_pruto_escolhido)

            # Valida se foi encontrado algum produto no carrinho de compras com o código determinado
            if produto_escolhido is not None:
                # Confirmação da exclusão
                print(f"\nVocê realmente deseja retirar o produto {produto_escolhido['descricao_produto_mercado']} do seu carrinho?")
                confirma_exclusao = input(f"Digite 'sim' para confirmar: ")

                if confirma_exclusao.lower().strip() == 'sim':
                    # Exclui o produto do carrinho
                    self.mongo.db['produtos_carrinho'].delete_one(
                                {"codigo": produto_escolhido['codigo']},
                            )
                    
                    print("\nProduto retirado com sucesso!")
                else:
                    print('\nRetirada cancelada. Voltando ao menu inicial...')
            else:
                print('\nProduto não encontrado, voltando ao menu inicial...')
        else:
            print('\nNão há produtos no carrinho, voltando ao menu inicial...')
        
        self.mongo.close()


     
    def lista_todos_produtos(self) -> bool:
        """
        Lista todos os produtos presentes no carrinho de compras.

        Esta função obtém os produtos no carrinho de compras, formata as informações e imprime a lista na tela.

        Args:
            Nenhum.

        Returns:
            bool: True se há produtos no carrinho, False caso contrário.
        """

        # Busca produtos presentes no carrinho de compras

        ctrl_produto_carrinho = ControllerProdutoCarrinho()

        produtos_carrinho = ctrl_produto_carrinho.verifica_produtos_carrinho()

        if produtos_carrinho:

            # Mensagem informativa
            print("Produtos presentes no carrinho de compras:\n")

            self.mongo.connect()

            collection = self.mongo.db['produtos_carrinho']
            
            resultado_consulta = collection.aggregate([
                {
                    "$lookup": {
                        "from": "produtos_mercados",
                        "localField": "codigo_produto_mercado",
                        "foreignField": "codigo",
                        "as": "produto_mercado"
                    }
                },
                {
                    "$unwind": "$produto_mercado"
                },
                {
                    "$lookup": {
                        "from": "produtos",
                        "localField": "produto_mercado.codigo_produto",
                        "foreignField": "codigo",
                        "as": "produto"
                    }
                },
                {
                    "$unwind": "$produto"
                },
                {
                    "$addFields": {
                        "total": {
                            "$multiply": ["$produto_mercado.valor_unitario", "$quantidade"]
                        }
                    }
                },
                {
                    "$project": {
                        "codigo": 1,
                        "quantidade": 1,
                        "codigo_produto": "$produto.codigo",
                        "descricao_produto": "$produto.descricao",
                        "codigo_produto_mercado": "$produto_mercado.codigo",
                        "descricao_produto_mercado": "$produto_mercado.descricao",
                        "valor_unitario": "$produto_mercado.valor_unitario",
                        "total": 1
                    }
                }
            ])



            # Itera os produtos presentes no carrinho de compras
            for resultado in resultado_consulta:
                codigo = resultado['codigo']
                descricao_produto_mercado = resultado['descricao_produto_mercado']
                valor_unitario = resultado['valor_unitario']
                quantidade = resultado['quantidade']
                total = resultado['total']

                # Imprimindo os valores formatados
                print(f"Código: {codigo:<5} | Produto: {descricao_produto_mercado:<30} | Valor unitário: {valor_unitario:<8.2f} | Quantidade: {quantidade:<5} | Total:{total:<10.2f}")

            return True

        else:

            print("Não há nenhum produto presente no carrinho de compras.")

            return False

     
    def verifica_produtos_carrinho(self) -> bool:
        """
        Obtém os produtos presentes no carrinho de compras.

        Args:
            Nenhum.

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


        # produtos_carrinho = oracle.sqlToDataFrame(query='SELECT pc.codigo as codigo, pc.quantidade, p.codigo as codigo_produto, p.descricao as descricao_produto, pm.codigo as codigo_produto_mercado, pm.descricao as descricao_produto_mercado, pm.valor_unitario FROM produtos_carrinho pc INNER JOIN produtos_mercados pm ON pc.codigo_produto_mercado = pm.codigo INNER JOIN produtos p ON pm.codigo_produto = p.codigo')

        self.mongo.connect()
        collection = self.mongo.db['produtos_carrinho']
        total_documentos = collection.count_documents({})

        if total_documentos > 0:
            self.mongo.close()
            return True
        
        self.mongo.close()
        return False


     
    def get_produto_por_codigo(self, codigo: int) -> DataFrame:
        """
        Obtém um produto específico do carrinho de acordo com o código.

        Args:
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
        
        self.mongo.connect()
        
        collection = self.mongo.db["produtos_carrinho"]

        total_documentos = collection.count_documents({"codigo": codigo})

        if total_documentos > 0:
            resultado_consulta = collection.aggregate([
                {
                    "$match": {
                        "codigo": codigo
                    }
                },
                {
                    "$lookup": {
                        "from": "produtos_mercados",
                        "localField": "codigo_produto_mercado",
                        "foreignField": "codigo",
                        "as": "produto_mercado"
                    }
                },
                {
                    "$unwind": "$produto_mercado"
                },
                {
                    "$lookup": {
                        "from": "produtos",
                        "localField": "produto_mercado.codigo_produto",
                        "foreignField": "codigo",
                        "as": "produto"
                    }
                },
                {
                    "$unwind": "$produto"
                },
                {
                    "$project": {
                        "codigo": "$codigo",
                        "quantidade": "$quantidade",
                        "codigo_produto": "$produto.codigo",
                        "descricao_produto": "$produto.descricao",
                        "codigo_produto_mercado": "$produto_mercado.codigo",
                        "descricao_produto_mercado": "$produto_mercado.descricao",
                        "valor_unitario": "$produto_mercado.valor_unitario"
                    }
                }
            ])

            for documento in resultado_consulta:
                dados_produto_carrinho = {
                    'codigo': documento['codigo'],
                    'codigo_produto': documento['codigo_produto'],
                    'codigo_produto_mercado': documento['codigo_produto_mercado'],
                    'quantidade': documento['quantidade'],
                    'descricao_produto_mercado': documento['descricao_produto_mercado']
                }
            
            self.mongo.close()

            return dados_produto_carrinho
        
        self.mongo.close()
        return None

    def exibe_produto_atualizado(self, codigo_produto):
        
        ctrl_produto_carrinho = ControllerProdutoCarrinho()
        produto_atualizado = ctrl_produto_carrinho.get_produto_por_codigo(codigo=codigo_produto)
                        
        print('\nProduto atualizado!')
        print(f"Código: {produto_atualizado['codigo']}, "
                f"Quantidade: {produto_atualizado['quantidade']}, "
                f"Código Produto: {produto_atualizado['codigo_produto']}, "
                f"Código Produto Mercado: {produto_atualizado['codigo_produto_mercado']}, "
                f"Descrição Produto Mercado: {produto_atualizado['descricao_produto_mercado']}, ")

if __name__ == "__main__":
    # ControllerProdutoCarrinho.adicionar_produto()
    # ControllerProdutoCarrinho.alterar_carrinho()
    # ControllerProdutoCarrinho.excluir_produto()
    ...