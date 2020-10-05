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
                _file = open(path, 'rb')
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
                    data = file_manager[path].read(300)
                    FS.close_file(path)
                    print('el archivo tiene',data)
                return data
        except Exception as e:
            print('ERROR!!! ', e)
            return None
   

     def read_file(path):
	    _path = path.value
	    _offset = path.offset
	    _number_bytes = path.number_bytes
	    try:
	      if FS.open_file(_path):
		_fd = FS.file_manager[_path]
		_fd.seek(_offset)
		data = _fd.read(_number_bytes)
		print("AASDASDASDASDASDSAD")        
		print(data)
	      FS.close_file(_path)
	      return data
	    except Exception as e:
	      print('error! FS read_file -> ', e)
	      return None

