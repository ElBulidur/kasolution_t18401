
# Abstracao
class Estoque:
    def __init__(self, produto, qtd, valor_unitario, peso, codigo, descricao="", qtd_minima=0) -> None:
        self.produto = produto
        self.descricao = descricao
        self.qtd = qtd
        self.valor_unitario = valor_unitario
        self.valor_total = self.qtd * self.valor_unitario
        self.qtd_minima = qtd_minima
        self.peso = peso
        self.codigo = codigo
        
    def montar_dicionario(self):
        estoque = {
            "produto": self.produto,
            "descricao": self.descricao,
            "qtd": self.qtd,
            "valor_unitario": self.valor_unitario,
            "valor_total": self.valor_total,
            "qtd_minima": self.qtd_minima,
            "peso": self.peso,
            "codigo": self.codigo
        }
        
        return estoque
    
    def __repr__(self):
        return f"Produto: {self.produto} - QTD: {self.qtd}"

    
