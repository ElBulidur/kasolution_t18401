"""
    Laboratório 1
    Criar um programa que utilize uma estrutura de repetição for. Nesta estrutura, o usuário deverá fornecer 5 nomes
    a serem adicionados em uma lista. No final, apresentar os nomes em ordem crescente.
    
    => O que vai aplicar neste exercício:
        - list
        - Input()
        - for
        - print()

"""

# nomes = []
# for i in range(2):
#    nome = input(f"digite o {i+1}º nome: ")
#    nomes.append(nome)
   
# nomes.sort()
# print("")
# print("nomes em ordem crescente:")
# for item in enumerate(nomes):
#     print(f"{item[0]+1}º Nome: {item[1]}")

# frutas = [input(f"Digite a {x+1}º fruta: ") for x in range(3)]

# frutas.sort()

# [print(f"{item[0]+1}º Nome: {item[1]}") for item in  enumerate(frutas)]
    

"""

    Laboratório 2
    Neste laboratório, uma lista de 100 números será criada de forma aleatória, ou seja, os elementos serão números
    aleatórios.
    Escrever o programa de forma a exibir E adicionar em uma lista, apenas os valores gerados que sejam maiores que
    10.

        => O que vai aplicar neste exercício:
            - random (from random import randint)
            - list
            - for
            - print()

"""

from random import randint as rdi

# numeros_maiores_que_10 = []



# for _ in range(100):
#     numero = rdi(1, 100)
#     if numero > 10:
#         numeros_maiores_que_10.append(numero)
        
# print(f"numeros maiores que 10: {len(numeros_maiores_que_10)}")
# print(numeros_maiores_que_10)

# numeros_maiores_que_10 = [x for x in [rdi(1,100) for _ in range(100)] if x > 10]

# print(f"numeros maiores que 10: {len(numeros_maiores_que_10)} => {numeros_maiores_que_10}")

from random import randint as rdi
numeros_maiores_que_10 = []
for _ in range (100):
    numero = rdi(1,100)
    if numero > 10:
        numeros_maiores_que_10.append(numero)
        
print("numeros maiores que 10:")
print(numeros_maiores_que_10)