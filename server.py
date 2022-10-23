import socket
import threading
import time

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

centinela = True
escAr = 1
while(centinela):
    try:
        escAr = int(input('Seleccione la opcion 1 para el archivo pequeno (100MB) y 2 para el archivo grande (250MB): '))
        conec = input('Cantidad de clientes concurrentes: ')
        if (escAr == 1 or escAr == 2) and int(conec)>0:
            centinela = False
        else:
            print('Ingrese una opción valida')
    except:
        print('Ingrese una opción valida')

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP listo...")

def handle_client():

    print("Enviando archivo...")
    if escAr == 1:
        f = open("Data/Pequeno.txt", 'r')
    else:
        f = open("Data/Grande.txt", 'r')

    data = f.read(bufferSize)

    while(data):

        if UDPServerSocket.sendto(str.encode(data), (localIP, localPort)):
            data = f.read(bufferSize)
            time.sleep(0.02)
    f.close()
    print("Archivo enviado con exito")

i = 1

# Listen for incoming datagrams
while(True):
    print("Esperando Conexiones")
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
    
    UDPServerSocket.sendto(str.encode(str(i)), (localIP, localPort))
    UDPServerSocket.sendto(str.encode(conec), (localIP, localPort))
    thread = threading.Thread(target=handle_client)
    thread.start()
    print(f"[THREADS ACTIVOS] {threading.activeCount() - 1}")
    i+=1
