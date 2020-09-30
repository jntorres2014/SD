class Server:

    def __init__(self, adapter=None):
        self.adapter= adapter

    def conectar (self):
        self.adapter.conectar()

    def desconectar(self):
        self.adapter.desconecta()

    def enviar (self, mensaje):
        self.adapter.enviar(mensaje)

    def recibir(self):
        return self.adapter.recibir()

    def aceptar (self):
        return self.adapter.aceptar()
        
    def listen (self):
        self.adapter.listen()

    def escuchar(self):
        self.adapter.escuchar()

    def __init__(self, adapter):
        self.adapter = adapter

    def inicializar(self):
        print('Inicializando el servidor')
        self.adapter.run()
