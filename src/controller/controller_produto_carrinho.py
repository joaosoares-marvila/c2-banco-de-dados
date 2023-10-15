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



if __name__ == "__main__":
    ControllerProdutoCarrinho.adicionar_produto()
