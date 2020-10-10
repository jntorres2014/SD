
class Client:

    def __init__(self, adapter):
        self.adapter = adapter

    def conectar(self):
        try:
            self.adapter.connect()
        except Exception as e:
            print('Connection error {e}')

    def desconectar(self):
        self.adapter.disconnect()

    def esta_conectado(self):
        return self.adapter.is_connected()

    def listar_archivos(self, path):
        return self.adapter.list_files(path)


    def leer_archivo(self, path):
        offset = 0
        number_bytes = 1024
        Leyendo = True
        try:
            with open('salida', 'wb') as archivo:
                while Leyendo:
                    data = self.adapter.read_file(path, offset, number_bytes)
                    offset = offset + len(data)
                    if not (offset%number_bytes==0) :
                        Leyendo = False
                    archivo.write(data)
                    print('data')
                    print('offset', round(offset/(1024*1024),2),'MB')
        except Exception as e:
            print('ERROR -> -client- read file ', e)
                
            return ('')
