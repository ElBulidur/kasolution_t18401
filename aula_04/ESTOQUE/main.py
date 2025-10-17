from services.geral_service import GeralService



def start():
    srv = GeralService()
    
    # srv.cadastrar_produto("Laranja", 10, 15.50, 1, "2541fjkd")
    srv.inser_excel_para_banco()
    
    
if __name__ == "__main__":
    start()



