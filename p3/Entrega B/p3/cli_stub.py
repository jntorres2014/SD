import socket
import pickle
import pdb
from structures import (
    Path, 
    PathFiles,
    PathRead,
)

class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        print('entro')
        paquete = { 'value': path, 'operacion': 1}
        objeto_a_enviar = pickle.dumps(paquete)
        self._channel.send(objeto_a_enviar)
        list_files = []
        lista= self._channel.recv(4096)
        lista2=pickle.loads(lista)
        for i in lista2['value']:
            print(i)
            list_files.append(i)
        return list_files

    def Read(self,path):
        self._channel.send(path)
        print('paro 1')
        request = self._channel.recv(4096)
        print('paso 1')
        return request

    def list_files2(self, path):
        _path = Path(path=path, operacion=1)
        pickle_path = pickle.dumps(_path)
        self._channel.sendall(pickle_path)
        path_files = PathFiles()
        list_files = []
        while self._channel.recv_into(path_files):
            list_files.append(path_files.values)
        return list_files


class Stub:

    def __init__(self, host='0.0.0.0', port='8090'):
        self._appliance = (host, port)
        print(host,port)
        self._channel = None
        self._stub = None

    def connect(self):
        """ Returns a Socket channel """
        try:
            #import pdb; pdb.set_trace()
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            print('Cliente Conectado!!..')
            return True if self._channel else False
        except Exception as e:
            print('Error when openning channel {}'.format(e))
            return False

    def disconnect(self):
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files(self, path):
        #import pdb; pdb.set_trace()
        if self.is_connected():
            respuesta= self._stub.ListFiles(path)
            return respuesta
        return None

    def read_file(self,path, offset, number_bytes):
        if self.is_connected():
            paquete = { 'value': path, 'offset': offset, 'number_bytes': number_bytes, 'operacion':2}
            objeto_a_enviar = pickle.dumps(paquete)
            #import pdb; pdb.set_trace()
            respuesta= self._stub.Read(objeto_a_enviar)
            request= pickle.loads(respuesta)
            return request['value']
        return None

    
