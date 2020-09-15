import os
file_manager= {}
def list_files(path):
	try:
		return os.listdir(path)
	except Exception as e:
		print('ERROR!!! ', e)
		return None

def openFile(path):
	try:
		if path not in file_manager:
		   archivo= open(path,'r')
		   self.file_manager[path]= archivo

		return True
	except Exception as e:
		print('ERROR!!! ', e)
		return False
def readFile(path):
	try:
		if path in file_manager:
			datos = file_manager[path].read()
		return datos
	except Exception as e:
		print('ERROR!!! ', e)
		return None
def closeFile(path):
	try:
		if path in file_manager:
		   file_manager[path].close()
		   del file_manager[path]
		   return true
	except Exception as e:
		print('ERROR!!! ', e)
		return False	
