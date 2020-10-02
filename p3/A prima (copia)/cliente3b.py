from client import Client
from cliente_stub import Stub
import pdb

def main():
    stub = Stub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    #pdb.set_trace()
    #respuesta = cliente.listar_archivos('.')
    #print(respuesta)
    archivo=cliente.leer_archivo('prueba.txt')
    #pdb.set_trace()
    print(archivo)
    #cliente.leer_archivo(archivo)

if __name__ == '__main__':
    main()
