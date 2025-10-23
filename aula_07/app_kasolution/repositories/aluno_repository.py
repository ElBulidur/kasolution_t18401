from infra import Database, Aluno

class AlunoRepository:
    def __init__(self):
        
        db = Database("localhost", "3306", "root", "root", "kasolution_app")
        self.session = db.get_session()
        
    def add(self, aluno: Aluno):
        self.session.add(aluno)
        self.session.commit()
        
    def get_all(self):
        return self.session.query(Aluno).all()




