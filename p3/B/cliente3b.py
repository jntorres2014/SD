from stub import Stub
from client import Cliente

def main():
   stub = Stub('localhost', 8080)
   cliente= Cliente(stub)
   cliente.conectar()
   
   while True:
    #respuesta = input('Ingrese una S para salir\n')
    
    cliente.enviar('s')       
    from_server = cliente.recibir()
    print(from_server)
    if from_server.decode() == 's': 
      break
   cliente.desconectar()

main()

