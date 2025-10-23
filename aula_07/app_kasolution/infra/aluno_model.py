from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from .config_infra import Base

class Aluno(Base):
    __tablename__ = "tb_alunos"
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cadastro=Column(DateTime(timezone=True), server_default=func.now())

    
    
    


