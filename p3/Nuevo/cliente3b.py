from client import Client
from cliente_stub import Stub
import pdb

def main():
    stub = Stub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    #Texto
    cliente.leer_archivo2('prueba.txt')
    #PDF
    #cliente.leer_archivo2('prueba')
    #Video
    #cliente.leer_archivo2('prueba2')
    #pdb.set_trace()
    print('Lectura completa.')

if __name__ == '__main__':
    main()
