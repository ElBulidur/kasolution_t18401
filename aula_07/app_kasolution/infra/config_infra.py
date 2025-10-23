from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()


class Config:
    
    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user:str):
        self.__user = user
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password:str):
        self.__password = password
        
        
    @property
    def host(self):
        return self.__host
    
    @host.setter
    def host(self, host:str):
        self.__host = host
        
    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, port:str):
        self.__port = port 
           
    @property
    def db_name(self):
        return self.__db_name
    
    @db_name.setter
    def db_name(self, db_name:str):
        self.__db_name = db_name
           
    @property
    def token(self):
        return self.__token
    
    @token.setter
    def token(self, token:str):
        self.__token = token

    def __init__(self, host):
        self.host = host
            
class Database(Config):
        def __init__(self, host, port, user, password, db_name):
            super().__init__(host)
            
            self.host = host
            self.port = port
            self.user = user
            self.password = password
            self.db_name = db_name
            
            self.base_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
            self.engine = create_engine(self.base_url)#, echo=True)
            self.SessionLocal = sessionmaker(bind=self.engine)
            
        def create_tables(self):
            Base.metadata.create_all(self.engine)
        
        def get_session(self):
            return self.SessionLocal()
           
class Api(Config):
    def __init__(self, url):
        super().__init__(url)
        
    def get_url(self, recurso):
        return f"{self.url}/{recurso}"
        
class Arquivo(Config):
    def __init__(self, path):
        super().__init__(path)
        