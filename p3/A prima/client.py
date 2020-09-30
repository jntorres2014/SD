
class Client:
    def __init__ (self, adapter=None):
        self.adapter = adapter

    def conectar(self):
        self.adapter.connect()

    def desconectar(self):
        #self.adapter.desconectar()
        self.adapter.disconnect()

    def enviar(self,mensaje):
        self.adapter.enviar(mensaje)

    def recibir(self):
        return self.adapter.recibir()
    
    #FALTA?
    def listar_archivos(self,path):
        return self.adapter.list_files(path)

    def abrir_archivo(self,path):
        return self.adapter.open_file(path)

    def cerrar_archivo(self,path):
        return self.adapter.close_file(path)

    def leer_archivo(self,path):
        return self.adapter.read_file(path)


