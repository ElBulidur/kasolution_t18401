from calc import somar_valores

def start():
    print("=============== CALCULADORA SIMPLES =============")
    
    numero_01 = input("Coloque o PRIMEIRO número: ")
    numero_02 = input("Coloque o SEGUNDO número: ")
    
    print("Opções: 1 - Soma, 2 - Subtração, 3 - Divisão e 4 - Multiplicação")
    opt = input("Coloque a opção desejada: ")
    
    if opt == '1':
        
        result = somar_valores(numero_01, numero_02)
        
    
    print(f"O resultado da suma operação é: {result}")
    
    
    
if __name__ == "__main__":
    start()