from file_system import FS
from server import Server
from server_stub import Stub 

def main():
    stub = Stub('localhost', '50051')
    servidor = Server(stub)
    servidor.inicializar()

if __name__ == '__main__':
    main()
