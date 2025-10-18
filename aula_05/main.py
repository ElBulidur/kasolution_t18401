
# HERANÇA
class Curso:
    # def __init__(self, nome="N/D", carga_horario=0):
    #     self.nome = nome
    #     self.carga_horaria = carga_horario
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.capitalize()
        
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, carga_horaria: str):
        self.__carga_horaria = carga_horaria
        
    def cadastrar_curso(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria
        
    def cadastrar_curso_sem_carga(self, nome):
        self.nome = nome
        
    def cadastrar_aluno(self):
        pass
    
    def cadastrar_serie(self):
        pass
        

#Ead => LINK
class CursoEAD(Curso):
        
        @property
        def link(self):
            return self.__link
        
        @link.setter
        def link(self, link: str):
            self.__link = link
            
        # POLIMOFISMO
        def cadastrar_curso(self, nome, carga_horaria, link):
            self.nome = nome
            self.carga_horaria = carga_horaria
            self.link = link
        
    
    
pythonEAD = CursoEAD()
pythonEAD.cadastrar_curso("Python", 32, "www.curso.com")

# pythonEAD.nome = None
# pythonEAD.carga_horaria = 32

# print(pythonEAD.nome)
# print(pythonEAD.link)
# print(pythonEAD.carga_horaria)

# pythonEAD.cadastrar_aluno()

#Presencial => Endereço

class CursoPresencial(Curso):
        
        @property
        def endereco(self):
            return self.__endereco
        
        @endereco.setter
        def endereco(self, endereco: str):
            self.__endereco = endereco
            
        # POLIMOFISMO
        def cadastrar_curso(self, nome, carga_horaria, endereco):
            self.nome = nome
            self.carga_horaria = carga_horaria
            self.endereco = endereco
            
            
pythonPresencial = CursoPresencial()

pythonPresencial.cadastrar_curso("Python", 32, "Rua dos limões, 44")

print(pythonPresencial.nome)
print(pythonPresencial.endereco)