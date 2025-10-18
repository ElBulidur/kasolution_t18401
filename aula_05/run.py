from abc import ABC, abstractclassmethod

#ABSTRAÇÃO
class Produto(ABC):
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        
    def valor_total(self):
        return self.preco * self.qtd
    
    @abstractclassmethod
    def exebir_info(self):
        pass
    
class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, qtd, validade):
        super().__init__(nome, preco, qtd)
        self.validade = validade
        
    def exebir_info(self):
        return f"{self.nome} (perecivel) - Validade: {self.validade} - R${self.preco:.2f}"
    
class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, qtd, garantia):
        super().__init__(nome, preco, qtd)
        
        self.garantia = garantia
        
    def exebir_info(self):
        return f"{self.nome} (Eletrônico) - garantia: {self.garantia} meses - R${self.preco:.2f}"
    
    
produto_perecivel = ProdutoPerecivel("Leite", 6.74, 20, "01/11/2025")
produto_eletronico = ProdutoEletronico("Mouse", 45.50, 15, 12)

# print(produto_perecivel.exebir_info())
# print(produto_eletronico.exebir_info())

# print(f"Total de valor do produto perecível é: {produto_perecivel.valor_total():.2f}")
# print(f"Total de valor do produto eletrônico é: {produto_eletronico.valor_total():.2f}")


# ARQUIVOS
# BANCO DE DADOS
# APIs
