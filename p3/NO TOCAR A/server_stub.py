import grpc
from concurrent import futures
import time
import pdb
import file_system_pb2
from file_system_pb2_grpc import (
    add_FSServicer_to_server,
    FSServicer,
)

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

    def Read(self,request,context):
        #print ('En READ') 
        #armo mi respuesta File Data
        response = file_system_pb2.FileData()
        response.data= self._adapter.read_file(request)
        return response
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
        self.server.start() 
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)
