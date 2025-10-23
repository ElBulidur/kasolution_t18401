import mysql.connector

def pegar_conn():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="kasolution"
        )
        
        return conn
        # print("Conexão realizada com sucesso!!!")

    except Exception as e:
        print(e)
    
# CREATE
def criar_aluno(aluno:str):
    ## SQL
    sql = "INSERT INTO alunos(nome) VALUES (%s)"
    dados = [aluno.capitalize()]

    ## CONEXÃO
    conn = pegar_conn()

    ## CURSOR
    cursor = conn.cursor()

    ## EXECUTAR SQL
    cursor.execute(sql, dados)

    ## COMITAR
    conn.commit()

    ## FECHAR CONEXÃO
    conn.close()

    print(f"Aluno {aluno} criado com sucesso!!!")

# EXEMPLO DE USO
alunos = ["Rene", "Wesley", "Mauro", "julio pereira"]

# for aluno in alunos:
#     criar_aluno(aluno)

# READ
def pegar_alunos():
    ## SQL
    sql = "SELECT * FROM alunos"

    ## CONEXÃO
    conn = pegar_conn()

    ## CURSOR
    cursor = conn.cursor()

    ## EXECUTAR SQL
    cursor.execute(sql)
    
    # cursor.fetchone() # Pegar primeira linha
    # cursor.fetchmany(3) #Pegar quantas linhas querer (numero)
    # cursor.fetchall() # Pegar todas as linhas

    alunos = []

    for linha in cursor.fetchall():
        alunos.append(linha[1])

    ## FECHAR CONEXÃO
    conn.close()

    return alunos
 
# EXEMPLO DE USO   
alunos = pegar_alunos()

# print(alunos)

## pegar por ID
def pegar_aluno_por_id(id):
    ## SQL
    # sql = "SELECT * FROM alunos WHERE id=%s"
    
    sql = "SELECT * FROM alunos WHERE id=%s"

    ## CONEXÃO
    conn = pegar_conn()

    ## CURSOR
    cursor = conn.cursor()

    ## EXECUTAR SQL
    cursor.execute(sql, [id])

    registro = cursor.fetchone()
    
    ## FECHAR CONEXÃO
    conn.close()

    if registro:
        return registro[1]
    else:
        print(f"Não existe no banco de dados aluno com id {id}")
        return False

# EXEMPLO DE USO
aluno = pegar_aluno_por_id(14)

# if aluno: print(f"Aluno {aluno} foi encontrado com sucesso!!!")

# UPDATE
def atualizar_nome_do_aluno(id, nome):
    ## SQL
    sql = "UPDATE alunos SET nome=%s WHERE id=%s"
    
    dados = [nome]

    dados.append(id)

    ## CONEXÃO
    conn = pegar_conn()

    ## CURSOR
    cursor = conn.cursor()

    ## EXECUTAR SQL
    cursor.execute(sql, dados)

    if cursor.rowcount:

        ## COMITAR
        conn.commit()
        
        ## FECHAR CONEXÃO
        conn.close()
        print(f"Aluno com id {id} foi atualizado com sucesso!!!")
    else:
        print("Não foi possivél encontrar aluno com id {id} no banco de dados!")
        ## FECHAR CONEXÃO
        conn.close()

# EXEMPLO DE USO
# atualizar_nome_do_aluno(16, "Julio Cezar Pereira")

# DELETE
def deletar_aluno(id):
    ## SQL
    sql = "DELETE FROM alunos WHERE id=%s"

    ## CONEXÃO
    conn = pegar_conn()

    ## CURSOR
    cursor = conn.cursor()

    ## EXECUTAR SQL
    cursor.execute(sql, [id])

    if cursor.rowcount:

        ## COMITAR
        conn.commit()
        
        ## FECHAR CONEXÃO
        conn.close()
        print(f"Aluno com id {id} foi Deletado com sucesso!!!")
    else:
        print("Não foi possivél encontrar aluno com id {id} no banco de dados!")
        ## FECHAR CONEXÃO
        conn.close()
        
# EXEMPLO DE USO      
# deletar_aluno(15)
