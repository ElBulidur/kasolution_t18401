'''
    Laboratório 1
    Escrever um programa em Python que solicite informações de três pessoas, como nome, idade, peso e altura.
    Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
    
    => Usar a formatação de interpolação.
'''

pessoas = [] # Coleção lista

# for i in range(1, 4):
#     print(f"\n-- Pessoa {i} ---")
#     nome = input("Nome: ")
#     idade = int(input("Idade: "))
#     peso = float(input("Peso (kg): "))
#     altura = float(input("Altura (m): "))
    
#     pessoas.append(
#         (nome, idade, peso, altura) # Tupla
#     )
    
# print("\n== Dados das Pessoas ===")
# print(f"{'Nome':<15}{'Idade':<10}{'Peso (kg)':<12}{'Altura (m)':<12}")
# print("-" * 50)

# for nome, idade, peso, altura in pessoas:
#     print(f"{nome:<15}{idade:<10}{peso:<12.2f}{altura:<12.2f}")


# nome, idade, peso, altura = input("Nome: "), int(input("Idade: ")), float(input("Peso: ")) , float(input("Altura: "))  
# nome2, idade2, peso2, altura2 = input("Nome: "), int(input("Idade: ")), float(input("Peso: ")) , float(input("Altura: ")) 
# nome3, idade3, peso3, altura3 = input("Nome: "), int(input("Idade: ")), float(input("Peso: ")) , float(input("Altura: ")) 

# print(f"Nome 01: {nome}\n", f"Idade 01: {idade}\n", f"Peso 01: {peso}\n", f"Altura 01: {altura}")
# print(nome2, idade2, peso2, altura2)
# print(nome3, idade3, peso3, altura3)

'''
    Laboratório 2
    
    Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. Usando operações de
    divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, a partir
    deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do
    saque.
    
    Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor
    quantidade possível de cédulas.

'''

# Operadores a trabalhar // %

# Entrada => Valor de saque
# Saida => Quantidade de cada cédula usada

# saque = int(input("Digite o valor do saque (múltiplo de 5): "))

# c_50 = saque // 50
# saque = saque%50

# c_20 = saque // 20
# saque = saque%20

# c_10 = saque // 10
# saque = saque%10

# c_5 = saque // 5
# saque = saque%5


# print(f"Nota 50: {c_50}, Nota 20: {c_20}, Nota 10: {c_10}, Nota 5: {c_5}")



valor = int(input("Digite o valor do saque (múltiplo de 5): "))

cedulas = [50, 20, 10, 5]
quantidade_cedulas = {}
resto = valor

for cedula in cedulas:
    quantidade = resto // cedula      
    resto = resto % cedula            
    quantidade_cedulas[cedula] = quantidade
    
print("\n=== Quantidade de Cédulas ===")

for cedula, quantidade in quantidade_cedulas.items(): print(f"Cédulas de R$ {cedula}: {quantidade}")