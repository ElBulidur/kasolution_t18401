# PARADIGMA

# PROCEDURAL (CALCULA MÉDIA)

numeros = [23, 45, 65] #

def media_valores(*args):
    total = 0
    for x in args:
        total += x
        
    return total / len(args)

# print(  media_valores(3, 3, 3) )

# FUNCIONAL (CALCULA MÉDIA)
# from functools import reduce, map, filter

media_valores_funcional = lambda *args: sum(args)/len(args)

# print(  media_valores_funcional(3, 3, 3) )


# Orientada a Objeto (CALCULA MÉDIA)

# Abstração
class MediaValores:
    def __init__(self, *args):
        self.args = args
        self.media = 0
        
    def calcular_media(self):
        self.media = sum(self.args)/len(self.args)
        

print(MediaValores)

# Objeto
media_valores_oop = MediaValores(3, 3, 3)

print(media_valores_oop)

# Atributos
print( media_valores_oop.args )
print( media_valores_oop.media )

# Métodos
media_valores_oop.calcular_media()

print( media_valores_oop.media )





