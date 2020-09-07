from stub import Stub
from client import Cliente

def main():
   stub = Stub('localhost', 8080)
   cliente= Cliente(stub)
   cliente.conectar()
   while True:
    respuesta = input('Ingrese una S para salir\n')
    print (respuesta)
    cliente.enviar('hola')       
    from_server = cliente.recibir()
    if from_server.decode() == 's': 
      break
   cliente.desconectar()

main()