from client import Client
from cliente_stub import Stub

def main():
    stub = Stub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    respuesta = cliente.listar_archivos('.')
    cliente.leer_archivo('.')
    print(respuesta)

if __name__ == '__main__':
    main()
