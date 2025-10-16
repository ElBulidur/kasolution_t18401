
def validar_valor(x):
    try:
        valor = float(x)
        return valor
    except:
        return "Não é possível converter."