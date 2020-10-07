from client import Client
from cli_stub import Stub

def main():
    stub = Stub('localhost', 8090)
    cliente = Client(stub)
    cliente.conectar()
    #respuesta = cliente.listar_archivos('.')
    #print(respuesta)
    cliente.leer_archivo('prueba.txt')
    print('salio')
if __name__ == '__main__':
    main()