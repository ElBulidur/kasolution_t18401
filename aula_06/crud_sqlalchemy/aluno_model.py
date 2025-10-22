from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
                
DATABASE_URL = f"mysql+pymysql://root:root@localhost:3306/kasolution"


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Aluno(Base):
    __tablename__ = "alunos"
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cadastro=Column(DateTime(timezone=True), server_default=func.now())
    
Base.metadata.create_all(engine)
    
    



