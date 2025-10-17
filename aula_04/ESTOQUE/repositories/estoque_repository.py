from models.estoque_model import Estoque


class EstoqueRepository:
    def inserir_produto(self, produto, qtd, valor_unitario, peso, codigo, descricao="", qtd_minima=0):
        
        entity = Estoque(produto, qtd, valor_unitario, peso, codigo, descricao, qtd_minima)
        
        estoque = entity.montar_dicionario()
        
        sql = "INSERT INTO logs("

        for x in estoque.keys():
            if x == list(estoque.keys())[-1]:
                sql = f"{sql} {x}) values ("
            else:
                sql = f"{sql} {x}, "

        for x in estoque.values():
            if x == list(estoque.values())[-1]:
                sql = f"{sql} {x})"
            else:
                sql = f"{sql} {x},"
        
        print(sql)
    
    
    def buscar_produtos(self):
        pass
    
    