import unittest
import time
from funcoes import somar, conectar_db, ler_api, processando_dados, add_ferramenta

endpoint = "https://68f979b1ef8b2e621e7c2c73.mockapi.io/"
url = f"{endpoint}/alunos"

# unitest
class TestFuncoes(unittest.TestCase):
    # TESTE DE INTEGRAÇÃO
    def test_soma(self):
        self.assertEqual(somar(2,3), 5)
        self.assertNotEqual(somar(2,2), 5)
        
    # TESTE DE INTEGRAÇÃO COM BANCO
    def test_conexao_db(self):
        result = conectar_db()
        self.assertEqual(result["status"], "ok")
        self.assertTrue(len(result["dados"]) > 0)
        
    def test_add_ferramenta(self):
        teste_1 = add_ferramenta("META DURO", 11)
        self.assertEqual(teste_1["status"], "Erro")
        
        teste_2 = add_ferramenta("META DURO", 4)
        self.assertEqual(teste_2["status"], "Erro")
        
        teste_3 = add_ferramenta("META DURO", 7)
        self.assertEqual(teste_3["status"], "ok")
        
    

# Testes
# resposta = ler_api(url)

# assert resposta.status_code == 401

# print(resposta.content)


def test_perfomace():
    inicio = time.time()
    processando_dados()
    duracao = time.time() - inicio
    assert duracao < 0.8

    



