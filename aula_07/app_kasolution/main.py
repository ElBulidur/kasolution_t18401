import requests
import json
from services import SRVService

srv = SRVService()

#USANDO API SIMPLES
# endpoint = "https://viacep.com.br/ws/35022500/json/"

# resposta = requests.get(url=endpoint)

# if resposta.status_code == 200:
    
#     conteudo = json.loads(resposta.content)
#     print(conteudo.get("logradouro"))

endpoint = "https://68f979b1ef8b2e621e7c2c73.mockapi.io/"

resposta = requests.get(url=f"{endpoint}/alunos")

if resposta.status_code == 200:
    conteudo = json.loads(resposta.content)
    
    for linha in conteudo:
        srv.cadastrar_aluno(linha.get("nome"), linha.get("email"))


