from database.config import Database


db = Database()

cursor = db.pegar_cursor()

sql = """
    INSERT INTO alunos (nome) VALUES (%s)
"""

cursor.execute(sql, ["Wesley"])

db.commitar()

db.fechar_conexao()