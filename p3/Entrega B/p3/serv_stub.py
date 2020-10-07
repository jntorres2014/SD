import socket
import pickle
from structures import Path

class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        print('entro a leer')
        data = self._channel.recv(4096)
        #import pdb; pdb.set_trace()
        operacion = pickle.loads(data)
        print('Entroooooooo!!!!')
        if operacion['operacion'] == 1:
                print('entro3')
                path_files = self._adapter.list_files(operacion['value'])
                entrega = { 'value': path_files}
                request= pickle.dumps(entrega)
                self._channel.send(request)
        if  operacion['operacion'] == 2:
            print('Entro!!!!!! READ')
            read_file = self._adapter.read_file(operacion)
            entrega = { 'value': read_file}
            request= pickle.dumps(entrega)
            self._channel.send(request)
            print ('salio')                
        return 0
        #else: 
        #    return 1


class Stub:

    def __init__(self, adapter, port='8090'):
        self._port = port
        self._adapter = adapter
        self.server = None
        self._stub = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 8090))        

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                connection, client_address = self.server.accept()
                from_client = ''
                self._stub = FSStub(connection, self._adapter)

        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)
