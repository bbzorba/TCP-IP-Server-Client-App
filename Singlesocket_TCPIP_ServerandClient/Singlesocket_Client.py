import socket
from time import sleep
import warnings

warnings.filterwarnings("ignore")

#TCP/IP client connection
address = '192.168.1.10'
port = 8086
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((address, port))
client_socket.send(bytes("Sensor Client is connected to the server", 'utf-8'))


while True:
    
    try:
        Data1 = "Data 1 in strings"
        client_socket.send(Data1.encode())

        sleep(2)

        Data2 = "Data 2 in strings"
        client_socket.send(Data2.encode())

        sleep(2)

    except KeyboardInterrupt:
        connection.close()