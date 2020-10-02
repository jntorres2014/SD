import os

class FS:
    file_manager = {}

    def list_files(path):
        print ('listado 2...')
        try:
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(path):
        try:
            if path not in file_manager:
                _file = open(path, 'r')
                file_manager[path] = _file
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def close_file(path):
        try:
            if path in file_manager:
                os.close(file_manager[path])
                #file_manager[path].close()
                del file_manager[path]
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file2(path):
        try:
            if open_file(path):
                if path in file_manager:
                    data= os.read(file_manager[path])
                    #data = file_manager[path].read()
                close_file(path)
            return data
        except Exception as e:
            print('ERROR!!! ', e)
            return None
    
    def read_file(path):
        print ('entro')
        os.open(path)
        data= os.read(path)
        os.close(path)
        return data