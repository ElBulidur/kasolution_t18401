# ABSTRAÇÃO
class Copo:
    def __init__(self):
        self.estado = "Novo"
        self.capacidade_volumetrica = 500
        self.ml = 0
        
    def resistencia_ao_impacto(self, impacto):
        if impacto > 10:
            self.estado = "Quebrado"
            
    def encher_copo(self, ml):
        
        if self.ml+ml > 500:
            print("O copo ja esta cheio!")
        else:
            self.ml += ml
     

#OBJETOS
copo_do_wesley = Copo()
copo_da_fernanda = Copo()
copo_do_rene = Copo()
copo_do_julio = Copo()


# MÉTODOS
copo_do_wesley.encher_copo(10)
copo_da_fernanda.encher_copo(500)
copo_do_rene.encher_copo(520)


print(f"Copo do Welsley esta com {copo_do_wesley.ml} ML")
print(f"Copo da Fernanda esta com {copo_da_fernanda.ml} ML")
print(f"Copo do Rene esta com {copo_do_rene.ml} ML")
print(f"Copo do Julio esta com {copo_do_rene.ml} ML")

print(f"O copo do Rene que estava {copo_do_rene.estado}")
copo_do_rene.resistencia_ao_impacto(50)
print(f"O copo ficou {copo_do_rene.estado}")
