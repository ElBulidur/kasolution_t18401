from infra import Aluno
from repositories import AlunoRepository

class AlunoService:
    def __init__(self):
        self.repo = AlunoRepository()
        
        
    def cadastrar_aluno(self, nome, email):
        if self.repo.session.query(Aluno).filter_by(email=email).first():
            raise ValueError("Email já cadastrado!!!")
        
        novo_aluno = Aluno(nome, email)
        
        self.repo.add(novo_aluno)
        
        return novo_aluno
    
    def listar_alunos(self):
        alunos = [x.nome for x in self.repo.get_all()]
        
        return alunos
        
        