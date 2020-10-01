import grpc
import pdb
from file_system_pb2 import Path
from file_system_pb2_grpc import FSStub
file_manager= {}

class Stub:

    def __init__(self, host='0.0.0.0', port='50051'):
        self._appliance = ':'.join([host, port])
        self._channel = None
        self._stup = None

    def connect(self):
        """ Returns a gRPC open channel """
        try:
            self._channel = grpc.insecure_channel(self._appliance)
            self._stub = FSStub(self._channel)
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
        pdb.set_trace()
        if self.is_connected():
            path = Path(value = path)
            response = self._stub.ListFiles(path)
            pdb.set_trace()
            print (response)
            return response.values
        return None
    

    def open_file(self,path):
        if path not in file_manager:
           archivo= open(path,'r')
           self.file_manager[path]= archivo
           return True
        return False
    def close_file(self,path):
        try:
            if path in file_manager :
                file_manager[path].close()
                del file_manager[path]
                return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False
    def read_file(self, path):
        try:
            if path in file_manager:
              datos = file_manager[path].read()
              pdb.set_trace()
            return datos
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    	
