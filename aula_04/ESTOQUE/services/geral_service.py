from repositories.estoque_repository import EstoqueRepository



class GeralService:
    def cadastrar_produto(self, produto, qtd, valor_unitario, peso, codigo, descricao="", qtd_minima=0):
        repo = EstoqueRepository()
        
        try:
            int(qtd)
        except:
            print("Precisa mandar o numero certo!")
            
        
        repo.inserir_produto(produto, qtd, valor_unitario, peso, codigo, descricao="", qtd_minima=0)
        
    
    def inser_excel_para_banco(self):
        pass
        
        
        
