from src.utils import config

class SplashScreen:

    def __init__(self):

        # Nome(s) do(s) criador(es)
        self.created_by = """   Cristian Menezes, Enzo Galão, 
                          Gabriel Schunk, Higor Soares,
                          João Pedro Guidolini, João Vitor Marvila"""
                                
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]
    
    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA MERCADO                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:              {str(self.get_documents_count(collection_name="produtos")).rjust(5)}
        #      2 - MERCADOS:              {str(self.get_documents_count(collection_name="mercados")).rjust(5)}
        #      3 - PRODUTOS DO CARRINHO:     {str(self.get_documents_count(collection_name="produtos_carrinho")).rjust(5)}
        #      4 - PRODUTOS POR MERCADO:  {str(self.get_documents_count(collection_name="produtos_mercados")).rjust(5)}
        #
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        #
        ########################################################
        """