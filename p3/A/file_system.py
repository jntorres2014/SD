import os

def list_files(path):
	try:
		return os.listdir(path)
	except Exception as e:
		print('ERROR!!! ', e)
		return None

	

def openFile (path):
	f= open (Path) 
	return (f) 


def readFile (path): 
 	f=read(Path)
	return (f) 

def closeFile (path):
	f=close(Path)
	return (f) 

