from client import Client
from cli_stub import Stub

def main():
    stub = Stub('localhost', '8090')
    cliente = Client(stub)
    cliente.conectar()
    respuesta = cliente.listar_archivos('.')
    print(respuesta)
    cliente.leer_archivo2('prueba')
    datos= cliente.mostrar

if __name__ == '__main__':
    main()