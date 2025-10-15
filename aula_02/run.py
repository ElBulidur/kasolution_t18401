# CONDICIONAL

# ALUNO 

# Nota maior que 6.9 => Aprovado
# Abaixo de 7 esta reprovado

nota = 7

# if nota > 6.9:
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado!")


# if nota > 6.9: print("Aluno aprovado!")
# else: print("Aluno reprovado!")

# print("Aluno aprovado!") if nota > 6.9 else print("Aluno reprovado!")


# Menor que 6 => Reprovado
# Entre 6 a 7 => Recuperação
# Maior que 7 => Aprovado

Nota = 6

# if nota < 6: print("Aluno Reprovado!")
# elif nota >= 6 or nota <= 7: print("Aluno Recuperação!")
# else: print("Aluno Aprovado!")


# COLEÇÕES (MUTÁVEL / IMUTÁVEL)

# LISTA
alunos = ["Julio", "Mauro", "Wesley"]
nomeros = [4,5,7,5,8]
dados_aluno_01 = ["Julio", 19, 89, 1.72, True]

# print( type(alunos) )
# print(alunos)
# print(alunos[-1])

# MÉTODOS (RETORNAR OU NÃO)

curso = ["Programando com python", "8 aulas", "32 hrs", '8 aulas']


# APPEND
# curso.append("06 alunos") # Adicionar elemento na lista (Não retorna)
# CLEAR
# curso.clear() # Limpa a lista (Não retorna)
# COPY
# retorno = curso.copy() # Faz uma cópia da lista para outro endereço da memória (Retorna)
# retorno_02 = curso

# print(retorno)
# print(retorno_02)
# print(curso)
# print(id(retorno))
# print(id(retorno_02))
# print(id(curso))
# print( curso is retorno_02 )
# print( curso is retorno )

# COUNT
# retorno = curso.count('8 aulas') # Retorna a quantidade de vezes é repetida.

# SORT
# curso.sort(reverse=True) # Ordena a lista (Não Retorna)

curso_lista = ["Programando com python", "8 aulas", "32 hrs", '8 aulas']

# POP
# retorno = curso.pop(0) # Extrai o elemento da lista e retorna.

# REMOVE
# curso.remove("32 hrs") # Remove o elemento da lista

# print(retorno)
# print(curso)

# TUPLA
curso_tupla = ("Programando com python", "8 aulas", "32 hrs", '8 aulas')
# meses = ("Janeiro", "Fevereiro", "Março")
# relacionamentos = [(1, 4), (1, 8)]

curso_lista[0] =  "Analisa de dados" # OK
# curso_tupla[0] =  "Analisa de dados" # ERROR


# DICIONÁRIO
curso_dicionario = {
    "Nome": "Programando com python",
    "Qtd Aulas": 8,
    "Carga": 32,
    "Alunos": [
        {"Nome": "Julio", "Nota": 7},
        {"Nome": "Mauro", "Nota": 5},
        {"Nome": "Rene", "Nota": 9}
    ]
}

# print(curso_dicionario)
# print(curso_dicionario["Nome"])
# print(curso_dicionario.get("carga"))
    
# POP
# retorno = curso_dicionario.pop("Nome") # Retorna o valor e remove a chave
# del curso_dicionario["Nome"]

# retorno = curso_dicionario.clear() # Limpa o dicionario (Não retorna)

# print( curso_dicionario.items() ) # Lista de tuplas com chave e valor
# print( curso_dicionario.values() ) # Lista de valores
# print( curso_dicionario.keys() ) # Lista de chaves 

curso_dicionario = {
    "Nome": "Programando com python",
    "Qtd Aulas": 8,
    "Carga": 32,
    "Alunos": [
        {"Nome": "Julio", "Nota": 7},
        {"Nome": "Mauro", "Nota": 5},
        {"Nome": "Rene", "Nota": 9}
    ]
}

# print(curso_dicionario["Alunos"][1]["Nome"])


# LOOP DE REPETIÇÃO

curso_lista = ["Programando com python", "8 aulas", "32 hrs", '8 aulas']


# for x in range(1, 10, 3): print(x)

# for x in curso_lista: print(x)

# for indice, elemento in enumerate(curso_lista): print(f"{indice+1} - {elemento}")

nome = "julio"

# for letra in nome:
#     print(letra)
#     if letra == 'l':
#         break

nome = [x for x in curso_lista if x != "8 aulas"]

print(nome)





