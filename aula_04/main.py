

# FUNÇÕES

# ARGUMENTOS INFINITO
def carrinho_compra(*args):
    print(  args )
    return sum(args)

def tentativas_de_acertos(*args):
    for i in args:
        if i == 20:
            print("Parabens, você acertou!!!")

# print(total)  
    
    
# total = carrinho_compra(150.00, 45.50, 58.90, 56.94)
# tentativas_de_acertos(15, 2, 47, 48, 10, 20)


[452, 485] # Lista
(452, 452) # Tupla
{"chave": "valor"} # dicionario
    
def imposto(**kargs):
    print(kargs.get("dpvat"))
    
# imposto(fgts=152, ipva=452, iptu=456, dpvat=45)



def log_acao(**kargs):
    
    kargs["data_hora"] = 'agora()'
        
    sql = "INSERT INTO logs("

    for x in kargs.keys():
        if x == list(kargs.keys())[-1]:
            sql = f"{sql} {x}) values ("
        else:
            sql = f"{sql} {x}, "

    for x in kargs.values():
        if x == list(kargs.values())[-1]:
            sql = f"{sql} {x})"
        else:
            sql = f"{sql} {x},"
            
    print(sql)
    
log_acao(usuario_id=10, reserva_id=150, cliente_id=2, detalhes="Sei não", error="deu bizu")