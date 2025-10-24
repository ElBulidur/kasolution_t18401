# ============================ REVISÃO ============================
# BÁSICO
## print, input, variáveis, operadores(matemáticos, relacional e lógicos)

# ESTRUTURA CONDICIONAL
## if/else

# COLEÇÕES
## Lista, Tupla e dicionários

# ESTRUTURA DE REPETIÇÃO
## for e while

# FUNÇÕES E MÓDULOS
## def, args, kargs, lambda, from e import

# ORIENTADA A OBJETO
## Classes, objetos, atributos, propriedades, métodos, construtores
## Herança, polimorfismo

# ARQUIVOS
## os, csv, pyopenxl, pandas

# BANCO DE DADOS
## mysql-conector-python, sqlalchyme, CRUD

## API
# requests, mockapi, métodos(get, post, put e delete)

# =========================== EXEMPLOS CRUD API ==================================
import requests
import json

endpoint = "https://68f979b1ef8b2e621e7c2c73.mockapi.io/"
url = f"{endpoint}/alunos"

# CREATE
def criar_aluno_api(dados):
    resposta = requests.post(url=url, data=dados)

    if resposta.status_code == 201:
        print("Aluno criado com sucesso!!!")
        
# EXEMPLO
# criar_aluno_api({ "nome": "Fernada Aluna", "email": "fernanda@email.com" })
         
# READ
def ler_api():
    respostas = requests.get(url=url)

    conteudo = json.loads(respostas.content)

    return conteudo

def ler_api_por_id(id):
    respostas = requests.get(url=f"{url}/{id}")

    conteudo = json.loads(respostas.content)

    return conteudo

def ler_api_por_email(email):
    alunos = ler_api()
    
    for aluno in alunos:
        if aluno.get("email") == email:
            return aluno
    
    return "Aluno não encontrado"
    
# EXEMPLOS
# print( ler_api())
# print( ler_api_por_id(10))
# print( ler_api_por_email('EldrezxzJones60@gmail.com'))

# UPDATE
def update_aluno_api(id, dados):
    resposta = requests.put(url=f"{url}/{id}", data=dados)

    if resposta.status_code == 200:
        print("Aluno com id {id} foi atualizado com sucesso!!!")

# EXEMPLO
# update_aluno_api(3, {"nome": "Fernanda MODIFICADO", "email": "fernanda.modificado@gmail.com"})

# DELETE
def deletar_aluno(id):
    resposta = requests.delete(url=f"{url}/{id}")

    if resposta.status_code == 200:
        conteudo = json.loads(resposta.content)
        print(f"Aluno {conteudo.get("nome")} foi deletado com sucesso!")
    elif resposta.status_code == 404:
        print(f"Aluno com id {id} não foi encontrado!")
    else:
        print("Ops, aconteceu algum erro!")

# EXEMPLO
# deletar_aluno(10) 