
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

    def leer_archivo2(self, path):
        offset= 0
        cant_bytes= 1024
        leyendo = True
        while offset < cant_bytes:
            with open(path,'wb') as archivo:
                
                data = self.adapter.read_file(archivo)
                respuesta += data
                offset = len(data)
                archivo.write(data)
                leyendo = offset == cant_bytes
        return respuesta

	def read_file(self, path):
	    print('reading')
	    offset = 0
	    number_bytes = 512
	    eof = False
	    try:
	      print('abriendo salida.txt')
	      with open('salida', 'wb') as archivo:
		print('salida.txt opened')
		while not eof:
		  data = self.adapter.read_file(path, offset, number_bytes)
		  print(data)
		  offset = offset + len(data)
		  if not (offset%number_bytes == 0):
		    eof = True
		  archivo.write(data)
		  print('still reading')
	    except Exception as e:
	      print('ERROR -> -client- read file ', e)
		
	    return ('check the ouput file in this directory')


