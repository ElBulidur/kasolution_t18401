#FUNÇÕES

#Sem retorno
def saudacao_01():
    print("Ei, seja bem vindo!!")
  
# saudacao_01()
 
# Com retorno 
def saudacao_02():
    return "Ei, seja bem vindo 01"

# result = saudacao_02()
# print(result)

# Sem retorno e com parâmetro
def saudacao_03(nome):
    print(f"Seja bem vindo(a) {nome}")
 
# saudacao_03("Julio")

# Com retorno e com parâmetro   
def saudacao_04(nome):
    return f"Seja bem vindo(a) {nome}"

# result = saudacao_04("Julio")
# print(result)

# Com retorno e com parâmetro e inferencia 
def saudacao_05(nome: str) -> None:
    print(f"Seja bem vindo(a) {nome.capitalize()}")
    
# saudacao_05("julio")

# Com retorno e com parâmetro iniciavel
def saudacao_06(nome="Julio") -> None:
    print(f"Seja bem vindo(a) {nome}")
    
# saudacao_06()


def carrinho_compra(*args):
    print(sum(args))
    
    
def imposto(**kargs):
    print(kargs)

# carrinho_compra(15.50, 40, 48, 46)

imposto(usuario_id=None, reserva_id=None, cliente_id=None,
             nome_ferramenta=None, codigo_ferramenta=None,
             data_retirada=None, data_entrega=None,
             acao="", detalhes="", error=None)


def log_acao(usuario_id=None, reserva_id=None, cliente_id=None,
             nome_ferramenta=None, codigo_ferramenta=None,
             data_retirada=None, data_entrega=None,
             acao="", detalhes="", error=None):
    """
    Registra uma ação ou erro na tabela 'logs'.
    Aceita opcionalmente usuario_id, reserva_id, cliente_id, e informações da ferramenta.
    """
    try:
        with get_connection() as conn:
            c = conn.cursor()
            c.execute("""
                INSERT INTO logs (
                    usuario_id,
                    reserva_id,
                    cliente_id,
                    nome_ferramenta,
                    codigo_ferramenta,
                    data_retirada,
                    data_entrega,
                    acao,
                    detalhes,
                    error,
                    data_hora
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                usuario_id,
                reserva_id,
                cliente_id,
                nome_ferramenta,
                codigo_ferramenta,
                data_retirada,
                data_entrega,
                acao,
                detalhes,
                error,
                agora()  # Função utilitária que retorna datetime.now() no fuso SP
            ))
            conn.commit()
    except Exception as e:
        print("⚠️ ERRO AO REGISTRAR LOG:", e)
        try:
            # Tenta gravar log mínimo de erro em arquivo local para não perder o rastreio
            with open("erro_log_acao.txt", "a", encoding="utf-8") as f:
                f.write(f"[{agora()}] Falha ao registrar log no banco: {e}\n")
        except:
            pass