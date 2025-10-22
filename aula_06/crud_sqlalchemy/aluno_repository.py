from aluno_model import Aluno, SessionLocal

class AlunosRepository:
    def __init__(self):
        self.session = SessionLocal()
        
    # CREATE
    def criar(self, nome:str, email:str):
        novo = Aluno(nome, email)
        
        self.session.add(novo)
        self.session.commit()
        
        return novo
    
    

aluno = AlunosRepository()

novo = aluno.criar("Wesley", "wesley@email.com")

print(f"Aluno criado: {novo.id} - {novo.nome}")