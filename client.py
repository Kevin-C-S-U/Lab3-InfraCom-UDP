from pickletools import TAKEN_FROM_ARGUMENT1
import socket
import select
import datetime
import time
import os

msgFromClient       = "Me mandas el archivo plis?"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.26.128", 20001)
bufferSize          = 1024
timeout = 3

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#UDPClientSocket.bind(("127.0.0.1",20001))
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

print("Esperando respuesta...")

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
inicio = time.process_time()
print(inicio)
c = int(msgFromServer[0])
cliente = "Numero de cliente: {}".format(c)
print(cliente)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
p = int(msgFromServer[0])
prueba = "Prueba con: {} clientes".format(p)
print(prueba)

nomAr = f"ArchivosRecibidos/Cliente-{c}-Prueba-{p}.txt"

f = open(nomAr,"wb")

while True:
    ready = select.select([UDPClientSocket], [], [], timeout)
    if ready[0]:
        data, addr =   UDPClientSocket.recvfrom(1024)
        f.write(data)
    else:
        fin = time.process_time()
        print("Se ha recibido el archivo")
        f.close()
        break


print(fin)
totalTime = fin-inicio
print(totalTime)

time.sleep(5)

UDPClientSocket.close()

dateNtime = datetime.datetime.now()
nombreFile = f"Logs/Cliente{c}-{dateNtime.year}-{dateNtime.month}-{dateNtime.day}-{dateNtime.hour}-{dateNtime.minute}-{dateNtime.second}-log.txt"

ar = os.stat(nomAr)
tamAr = ar.st_size/ (1024 * 1024)

log = open(nombreFile,"w")

log.write(f"Archivo recibido = {nomAr}\nTamano archivo recibido = {tamAr} MB\nTiempo de transferencia = {totalTime} s")
log.close()