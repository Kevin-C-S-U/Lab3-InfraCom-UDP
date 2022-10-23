import socket
import select

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
c = msgFromServer[0]
cliente = "Numero de cliente: {}".format(c)
print(cliente)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
p = msgFromServer[0]
prueba = "Prueba con: {} clientes".format(p)
print(prueba)

f = open(f"ArchivosRecibidos/Cliente-{c}-Prueba{p}","wb")

while True:
    ready = select.select([UDPClientSocket], [], [], timeout)
    if ready[0]:
        data, addr =   UDPClientSocket.recvfrom(1024)
        f.write(data)
    else:
        print("Se ha recibido el archivo")
        f.close()
        break
UDPClientSocket.close()