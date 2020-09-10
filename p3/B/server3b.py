import socket
from stub import Stub
from server import Server

def main():
    stub = Stub('localhost',8080)
    server = Server(stub)
    server.conectar()
    server.listen()
#    cliente, addr = server.accept()
    message = 'Tu conexion fue cerrada con Exito!!\n'

    while True:
        print('Server disponible!')
        connection, client_address = server.aceptar()
        from_client = ''
        while True:
            data = connection.recv(4096)
            #connection.send(data.encode('utf-8'))
            if data.decode() == 's':break
            from_client += data.decode() #acumula los mensajes que llegan.
            connection.send(from_client.encode('utf-8'))
        print('salio')	
        connection.send(data)
        connection.close()
        print('cliente desconectado \n')
main()