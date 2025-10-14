
# print("imprimir")

"""
    comentário em bloco
    para várias linhas
    
"""

'''
    OUTRO COMENTÁRIO EM BLOCO
    
'''


# BOAS PRÁTICA

# FORMA DE ESCRITA (camelCase ou snack_case)

 # julioPereira (CAMELCASE)
 # julio_pereira (SNACK_CASE)



# VARIÁVEIS

numero = 45 # Variável inteira (int)
valor = 2.50 # Variável Real (float)
nome = "Julio" # Variável Texto (str)
sobrenome = 'Pereira' # Variável Texto (str)
acabou = True # Variável Boleana (bool)
numero_e_maior_que_50 = numero > 50 # Variável Boleana (bool)


# print( type(numero) ) # <class 'int'>
# print( type(valor) ) # <class 'float'>
# print( type(nome) ) # <class 'str'>
# print( nome.upper() )
# print( dir(nome) )
# print(nome[0])
# print(nome[-1])

# print( type(acabou) ) # <class 'bool'>
# print( type(numero_e_maior_que_50) ) # <class 'bool'>

# from datetime import datetime

# data = datetime.now()

# print(data)

# ATRIBUIÇÕES

# simples
x = 30

#multipla
y1 = y2 = y3 = 20

#sequencial
usuario, senha = "elbulidur", "bolaquadrada"


# OPERADORES
## MATEMÁTICOS (+, -, /, *, %, //)
x = 12
y = 10

soma = x + y 
sub = x - y
div = x / y
mult = x * y

z = x % y # Resto da divisão
w = x // y # divisão inteira


valor = 12

novo_valo_1 = 10

# FORMA DIRETA
# valor = valor + novo_valo_1
# valor += novo_valo_1
# valor -= novo_valo_1
# valor /= novo_valo_1
# valor *= novo_valo_1
# valor %= novo_valo_1
# valor //= novo_valo_1


# OPERADORES RELACIONAIS (>, <, >=, <=, ==, !=)

x = 15
y = 15

# print(  x > y) # Maior
# print(  x < y) # Menor
# print(  x >= y) # Maior ou igual
# print(  x <= y) # Menor ou igual
# print(  x == y) # Igual
# print(  x != y) # Diferente


#OPERADORES LÓGICOS
x = 120
y = 42

# AND
# print( x == y and x == 120 )
# print( x > y and x == 120 )

# OR
# print( x == y or y == 42 )
# print( x == y or y == 120 )

# NOT
# print( not x == y )
# print( not x > y )


# ENTRADAS DE DADOS(INFORMAÇÕES)
# nome = input("Escreva seu nome: ")

# print("Seja bem vindo,", nome)

try:
    numero_01, numero_02 = int(input("Coloque o PRIMEIRO número: ")), int(input("Coloque o SEGUNDO número: "))
    
    print( "A soma dos números é: ", numero_01 + numero_02 )
except NameError:
    print("Erro de nome")
except ValueError:
    print("Erro de valor. Vou te dar mais uma oportunidade. Poe só numero mano")
    
    numero_01, numero_02 = int(input("Coloque o PRIMEIRO número: ")), int(input("Coloque o SEGUNDO número: "))
    
    print( "A soma dos números é: ", numero_01 + numero_02 )


# try:
#     x = 12/0
# except ZeroDivisionError as e:
#     print(e, "Traduzindo , não faz divisão por 0.")
















 