import os

def list_files(path):
	try:
		return os.listdir(path)
	except Exception as e:
		print('ERROR!!! ', e)
		return None

def openFile(path):
	try:
		if path not in file_manager:
		   archivo= open(path)
		   file_manager.append(archivo)
		   return archivo
		return True
	except Exception as e:
		print('ERROR!!! ', e)
		return False
def readFile(path):
	try:
		archivo = read(path)
		return archivo
	except Exception as e:
		print('ERROR!!! ', e)
		return None
def closeFile(path):
	try:
		if path in file_manager:
		   close(path)
		   file_manager.remove(path)
		   return true
	except Exception as e:
		print('ERROR!!! ', e)
		return False	

