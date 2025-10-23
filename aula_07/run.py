import requests
import json

endpoint = "https://68f979b1ef8b2e621e7c2c73.mockapi.io/"
url = f"{endpoint}/alunos"


# CREATE
dados = {
    "nome": "Fernada Aluna",
    "email": "fernanda@email.com"
}

def criar_aluno_api(dados):
    resposta = requests.post(url=url, data=dados)

    if resposta.status_code == 201:
        print("Aluno criado com sucesso!!!")
        
        
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
    
# print( ler_api_por_email('EldrezxzJones60@gmail.com'))

# UPDATE
# DELETE



