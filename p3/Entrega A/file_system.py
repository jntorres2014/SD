import os

file_manager = {}
class FS:

    def list_files(path):
        try:
            print('listando...')
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(path):
        try:
            if path not in file_manager:
                #import pdb; pdb.set_trace()
                _file = open(path, 'r')
                file_manager[path] = _file
                print('imprimo', file_manager)
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False
    
    def close_file(path):
        try:
            if path in file_manager:
                file_manager[path].close()
                del file_manager[path]
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file(path):
        print('Leyendo...',path)
        try:
            if FS.open_file(path):
                if path in file_manager:
                    print('el archivo tiene',file_manager[path])    
                    data = file_manager[path].read()
                    FS.close_file(path)
                    print('el archivo tiene',data)
                return data
        except Exception as e:
            print('ERROR!!! ', e)
            return None
   
    def read_file2(path):
        print('entro al read',path)
        archivo= os.open(path,'r')
        import pdb; pdb.set_trace()
        data= archivo.readline()
        print (data)
        #path.close()
        return data
