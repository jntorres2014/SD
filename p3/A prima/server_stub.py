import grpc
from concurrent import futures
import time
#import tqdm
#import os

import file_system_pb2
from file_system_pb2_grpc import (
    add_FSServicer_to_server,
    FSServicer,
)


# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

class StubFSServicer(FSServicer):

    opened_files = {}

    def __init__(self, adapter):
        self._adapter = adapter
        FSServicer.__init__(self)

    def ListFiles(self, request, context):
        response = file_system_pb2.PathFiles()
        try:
            for file in self._adapter.list_files(request.value):
                response.values.append(file)
        except Exception as e:
            print('ERRR En server list files ', e)
        return response

    def ReadFile(self,path):
        if self.is_connected():  
            #Aca estoy tratando de leer el archivo (Siguiendo un ejemplo)
            read_file= file_system_pb2.ReadFile(value=path)
            response = self._adapter.ReadFile(read_file)
            return response.valor
        try:
            pass
        except Exception as e:
            print('ERRR En server read file ', e)
        return None

class Stub:

    def __init__(self, adapter, port='50051'):
        self._port = port
        self._adapter = adapter
        self.server = None

    def _setup(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_FSServicer_to_server(StubFSServicer(self._adapter), self.server)
        self.server.add_insecure_port('[::]:{}'.format(self._port))

    
    def run(self):
        self._setup()
        #Falta la definicion del Start
        self.server.start()

        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)
