import os

class FS:
    #file_manager = {}

    def list_files(path):
        try:
            print('listando...')
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file2(path):
        try:
            if path not in file_manager:
                _file = open(path, 'r')
                file_manager[path] = _file
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False
    
    def open_file(path):
        print('entro al open')
        archivo = open(path,'r')
        return True
        
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
                    data= os.read(path)
                    #data = file_manager[path].read()
                close_file(path)
            return data
        except Exception as e:
            print('ERROR!!! ', e)
            return None
   
    def read_file(path):
        print('entro al read',path)
        import pdb; pdb.set_trace()
        data= path.read()
        print (data)
        #path.close()
        return data
