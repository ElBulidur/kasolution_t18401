import mysql.connector



class Database:
    def __init__(self):
        self.conn = None
    
    
    def pegar_conexao(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="kasolution"
            )
            
            self.conn = conn
            
            print("Conexão realizada com sucesso!!!")

        except mysql.connector.Error as e:
            print(f"Erro do banco: {e}")
        except Exception as e:
            print(f"Erro do python: {e}")
            
    def pegar_cursor(self):
        self.pegar_conexao()
        return self.conn.cursor()
    
    def commitar(self):
        self.conn.commit()
    
    def fechar_conexao(self):
        self.conn.close()
        print("Conexão FECHADA com sucesso!!!")