from client import Client
from cliente_stub import Stub
import pdb

def main():
    stub = Stub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    pdb.set_trace()
    respuesta = cliente.listar_archivos('/home/jony/Descargas/Universidad/Sistemas Distribuidos/SD/p3/A prima/')
    cliente.leer_archivo('/home/jony/Descargas/Universidad/Sistemas Distribuidos/SD/p3/A prima/')
    print(respuesta)
    pdb.set_trace()
if __name__ == '__main__':
    main()
