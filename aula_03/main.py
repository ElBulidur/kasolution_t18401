lista = ["Julio", 18, 85, 1.72, True]

tupla = ("Julio", 18, 85, 1.72, True)

dicionario = {
    "Nome": "Julio",
    "Idade": 18,
    "Peso": 85,
    "Altura": 1.72,
    "Aprovado": True
}

# LOOPS
nome_idade_aluno = {}

for i in range( len(lista) ):
    if i == 0:
        nome_idade_aluno["Nome"] = lista[i]
    elif i == 1:
        nome_idade_aluno["Idade"] = lista[i]
        
dicionario = {
    "Nome": "Julio",
    "Idade": 18,
    "Peso": 85
}

# INSERT INTO ALUNOS(Nome, Idade, Peso) VALUES ( Julio, 18, 85)

sql = "INSERT INTO ALUNOS("

for x in dicionario.keys():
    if x == "Peso":
        sql = f"{sql} {x}) values ("
    else:
       sql = f"{sql} {x}, "

for x in dicionario.values():
    if x == list(dicionario.values())[-1]:
        sql = f"{sql} {x})"
    else:
        sql = f"{sql} {x},"
        
# for x in dicionario.items(): print(f"{x[0]}: {x[1]}")

# [print(f"{x[0]}: {x[1]}") for x in dicionario.items()]
       
# print(sql)

# print( list(dicionario.values())[-1] )
        
# print( len(lista) )
# print(nome_idade_aluno)

# WHILE

x=0

# while x < 2:
#     print("Entrou aqui")
#     x += 1
    

saque = 0 #int(input("Digite o valor do saque (múltiplo de 5): "))

while saque%5 != 0:
    saque = int(input("Errou. Tente novamente ou digite 0 para sair: "))
    
    if saque == 0:
        break

if saque ==0:
    pass
    # print("Ate mais!!!")
else:
    c_50 = saque // 50
    saque = saque%50

    c_20 = saque // 20
    saque = saque%20

    c_10 = saque // 10
    saque = saque%10

    c_5 = saque // 5
    saque = saque%5


    print(f"Nota 50: {c_50}, Nota 20: {c_20}, Nota 10: {c_10}, Nota 5: {c_5}")



# MÓDULOS
# import random
from random import randint, random

# print( randint(1, 10)  )
# print( random()  )

opcao = input("1 para Somar ou 2 para subtrair: ")

# if opcao == "1":
#     from calc import soma
    
#     print( soma.somar(23, 10) )
# elif opcao == "2":
#     from calc import sub
    
#     print( sub.subtrair(50, 20))
    

    






# FUNÇÕES