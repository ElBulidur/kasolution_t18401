import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="kasolution"
    )
    
    print("Conexão realizada com sucesso!!!")

except Exception as e:
    print(e)
    
    
   
cursor = conn.cursor()
   

# sql = """
#     CREATE TABLE IF NOT EXISTS alunos (
#         id SERIAL PRIMARY KEY,
#         nome VARCHAR(100) NOT NULL
#     )

# """ 

sql = """
    INSERT INTO alunos (nome) VALUES (%s)
"""

cursor.execute(sql, ["Julio Pereira"])

conn.commit()

print("tabela criada")


cursor.close()
conn.close()



