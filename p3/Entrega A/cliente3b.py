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
    #archivo=cliente.leer_archivo('prueba.mp4')
    archivo=cliente.leer_archivo2('prueba.pdf')

    #pdb.set_trace()
    print('llegue a la salida')
    print(archivo)
    #cliente.leer_archivo(archivo)

if __name__ == '__main__':
    main()
