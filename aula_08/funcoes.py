import requests
import json
import time

# FUNÇÃO COMUM
def somar(a, b):
    return a+b

def conectar_db():
    return {"status": "ok", "dados": [1,2,3]}

def ler_api(url):
    return requests.get(url=url)


def processando_dados():
    time.sleep(0.6)
    return True

# METAL DURO > 5-10
def add_ferramenta(nome, espessura):
    if nome == "META DURO" and (espessura <= 5 or espessura > 10):
        return {"status": "Erro", "dados": None}
    
    return {"status": "ok", "dados": (nome, espessura)}