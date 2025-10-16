from services import validar_valor

def somar_valores(x, y):
    if type(validar_valor(x)) == str or type(validar_valor(y)) == str:
        return "Erro ao tentar converter os valores!!!"   
    
    return validar_valor(x) + validar_valor(y)