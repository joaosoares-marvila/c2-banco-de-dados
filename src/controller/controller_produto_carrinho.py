import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from model.produtos_carrinho import ProdutoCarrinho
from controller.controller_produto import ControllerProduto
from controller.controller_produto_mercado import ControllerProdutoMercado
from conexion.oracle_queries import OracleQueries

class ControllerProdutoCarrinho:
    def __init__(self):
        pass

    @staticmethod
    def adicionar_produto():
        
        # Solicitar ao usuário que insira a descrição do produto que deseja buscar
        descricao_produto = input("Digite o nome do produto que deseja inserir: ")

        if descricao_produto:

            # Chama o método inserir_produto da classe ControllerProduto
            produto = ControllerProduto.inserir_produto(descricao_produto=descricao_produto)
            
            if produto:

                # Busca informações sobre o produto em diferentes mercados
                produto_perim, produto_extrabom = ControllerProdutoMercado.busca_produtos_mercados(produto=produto)


                # Inicialize a conexão com o banco de dados
                oracle = OracleQueries(can_write=True)
                oracle.connect()


                # Produto encontrado em ambos os mercados
                if produto_perim and produto_extrabom:
                    print(f'Foram encontrados produtos em ambos os mercados referentes ao produto {str(produto)}.')
                    print(f' 1 - \t {str(produto_perim)}')
                    print(f' 2 - \t {str(produto_extrabom)}')
                    print(f' 0 - \t Sair')

                    opcao = input('Selecione a opção desejada: ').strip()

                    if opcao == '1':
                        quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                        # Insira o produto no carrinho (mercado Perim)
                        oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_perim.codigo}, {quantidade})")
                        print(f'{quantidade} unidades do produto {produto_perim.descricao} foram adicionadas ao carrinho.')
                    
                    elif opcao == '2':
                        quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                        # Insira o produto no carrinho (mercado ExtraBom)
                        oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_extrabom.codigo}, {quantidade})")
                        print(f'{quantidade} unidades do produto {produto_extrabom.descricao} foram adicionadas ao carrinho.')
                    
                    elif opcao == '0':
                        print('Saindo do menu de produtos.')
                    
                    else:
                        print('Opção inválida. Voltando para a tela inicial.')


                # Produto encontrado apenas no mercado Perim
                elif produto_perim:
                    print(f'Foram encontrados produtos apenas no mercado Perim referentes ao produto {str(produto)}.')
                    print(f' 1 - \t {str(produto_perim)}')
                    print(f' 0 - \t Sair')

                    opcao = input('Selecione a opção desejada: ').strip()

                    if opcao == '1':
                        quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                        # Insira o produto no carrinho (mercado Perim)
                        oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_perim.codigo}, {quantidade})")
                        print(f'{quantidade} unidades do produto {produto_perim.descricao} foram adicionadas ao carrinho.')
                    
                    elif opcao == '0':
                        print('Saindo do menu de produtos.')
                    
                    else:
                        print('Opção inválida. Voltando para a tela inicial.')


                # Produto encontrado apenas no mercado ExtraBom
                elif produto_extrabom:
                    print(f'Foram encontrados produtos apenas no mercado ExtraBom referentes ao produto {str(produto)}.')
                    print(f' 1 - \t {str(produto_extrabom)}')
                    print(f' 0 - \t Sair')

                    opcao = input('Selecione a opção desejada: ').strip()

                    if opcao == '1':
                        quantidade = int(input('Digite quantas unidades você gostaria de adicionar ao carrinho: '))
                        # Insira o produto no carrinho (mercado Perim)
                        oracle.write(f"insert into produtos_carrinho (CODIGO_PRODUTO_MERCADO, QUANTIDADE) VALUES ({produto_extrabom.codigo}, {quantidade})")
                        print(f'{quantidade} unidades do produto {produto_extrabom.descricao} foram adicionadas ao carrinho.')
                    
                    elif opcao == '0':
                        print('Saindo do menu de produtos.')
                    
                    else:
                        print('Opção inválida. Voltando para a tela inicial.')


                # Produto não encontrado
                else:
                    print(f'Não foi encontrado nenhum produto referente a {str(produto)}.')
                    print('Voltando para a tela inicial.')




    @staticmethod
    def alterar_carrinho():
        
        ControllerProdutoCarrinho.lista_todos_produtos()    
        opcao = input('Digite o código do produto que deseja alterar')

        data_frame_opcao_esclhida = oracle.sqlToDataFrame('select pc.codigo as codigo_produto_carrinho, p.codigo as codigo_produto, pm.codigo as codigo_produto_mercado, pc.quantidade from produtos_carrinho pc inner join produtos_mercados pm on pc.codigo_produto_mercado = pm.codigo inner join produtos p on pm.codigo_produto = p.codigo')

        if not data_frame_opcao_esclhida.empty:
            
            codigo_produto_carrinho = data_frame_opcao_esclhida.iloc[0]['codigo_produto_carrinho']
            codigo_produto = data_frame_opcao_esclhida.iloc[0]['codigo_produto']
            codigo_produto_mercado = data_frame_opcao_esclhida.iloc[0]['codigo_produto_mercado']
            quantidade = data_frame_opcao_esclhida.iloc[0]['quantidade']

            
            print('1 - Alterar quantidade')
            print('2 - Alterar produto (mercado)')
            print('0 - Sair')
            
            opcao = input("Digite o número da opção desejada: ")
            
            if opcao == '1':
            
                nova_quantidade = int(input('Digite a quantidade desejada: '))
                oracle.write(f'UPDATE produtos_carrinho SET quantidade = {nova_quantidade} WHERE codigo = {codigo_produto_carrinho}')
                print('Produto atualizado! Voltando para a tela inicial...')
                
            elif opcao == '2':

                produto = ControllerProduto.busca_produto_codigo(codigo_produto)
                produto_perim, produto_extrabom =  ControllerProdutoMercado.busca_produtos_mercados_db(produto)

                print('Produtos disponíveis: ')
                
                if produto_extrabom and produto_perim:
                    print(f'1 - {str(produto_perim)}')
                    print(f'2 - {str(produto_extrabom)}')
                    print(f'3 - Cancela alteração')
                
                    opcao = input('Digite o código do produto que deseja selecionar: ')
                    
                    if opcao == '1':
                        ...
                    elif opcao == '2':
                        ...
                    elif opcao == '3':
                        ...
                    else:
                        ...

                    
                elif produto_perim:
                    print(f'1 - {str(produto_perim)}')
                    print(f'2 - Cancela alteração')
                    
                    if opcao == '1':
                        ...
                    elif opcao == '2':
                        ...
                    else:
                        ...

                elif produto_extrabom:
                    print(f'1 - {str(produto_extrabom)}')
                    print(f'2 - Cancela alteração')
                    
                    if opcao == '1':
                        ...
                    elif opcao == '2':
                        ...
                    else:
                        ...
                

        else:
            print('Código inválido. Voltando ao menu inicial...')




    def excluir_produto():

        ControllerProdutoCarrinho.lista_todos_produtos()

        opcao = input('Digite o código do produto que deseja alterar')

        data_frame_opcao_esclhida = oracle.sqlToDataFrame('select pc.codigo as codigo_produto_carrinho, p.codigo as codigo_produto, pm.codigo as codigo_produto_mercado, pc.quantidade from produtos_carrinho pc inner join produtos_mercados pm on pc.codigo_produto_mercado = pm.codigo inner join produtos p on pm.codigo_produto = p.codigo')

        if not data_frame_opcao_esclhida.empty:
            ...
            




    @staticmethod
    def lista_todos_produtos():
        # Inicialize a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        produtos_carrinho = oracle.sqlToDataFrame('select pc.codigo, p.descricao as produto, pm.descricao as produto_mercado, pm.valor_unitario, pc.quantidade from produtos_carrinho pc inner join produtos_mercados pm on pc.codigo_produto_mercado = pm.codigo inner join produtos p on pm.codigo_produto = p.codigo')

        # Iterar sobre cada linha
        for index, row in produtos_carrinho.iterrows():
            codigo = row['codigo']
            produto = row['produto']
            valor_unitario = row['valor_unitario']
            quantidade = row['quantidade']
            total = valor_unitario * quantidade

            print(f"Código - {codigo} \t Produto: {produto} \t Valor unitário: {valor_unitario} \t Quantidade: {quantidade} \t Total: {total}")




if __name__ == "__main__":
    ControllerProdutoCarrinho.adicionar_produto()
