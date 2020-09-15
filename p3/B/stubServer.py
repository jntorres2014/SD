import socket
from server import Server
class StubServer:
    def escuchar(self):
        self.server.listen()
        
    def bind(self):
        self.server.bind()

    def conectar(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.host, self.port))

    def desconectar(self):
        self.server.close()
        
    def enviar(self, message):
        self.server.send(message.encode('utf-8'))

    def esperar (self):
        self.server.listen()

    def recibir(self):
        msg = self.server.recv(4096)
        return msg if not type(msg) == bytes else msg.decode()
        
    def aceptar(self):
        self.server.accept()