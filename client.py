import socket
import select

msgFromClient       = "Me mandas el archivo plis?"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
timeout = 3

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

print("Esperando respuesta...")

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
cliente = "Numero de cliente: {}".format(msgFromServer[0])
print(cliente)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
prueba = "Prueba con: {} clientes".format(msgFromServer[0])
print(prueba)

f = open(f"Cliente-{cliente}-Prueba{prueba}","wb")

while True:
    ready = select.select([UDPClientSocket], [], [], timeout)
    if ready[0]:
        data, addr =   UDPClientSocket.recvfrom(1024)
        f.write(data)
    else:
        print("Se ha recibido el archivo")
        f.close()
        break
