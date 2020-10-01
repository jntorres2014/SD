from client import Client
from cliente_stub import Stub
import pdb

def main():
    stub = Stub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    #pdb.set_trace()
    respuesta = cliente.listar_archivos('.')
    print(respuesta)
    archivo=cliente.abrir_archivo('prueba.txt')
    cliente.leer_archivo(archivo)

    pdb.set_trace()
if __name__ == '__main__':
    main()
