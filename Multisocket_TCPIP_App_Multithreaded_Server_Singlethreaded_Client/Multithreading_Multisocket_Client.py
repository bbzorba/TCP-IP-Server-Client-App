import socket
from time import sleep
import warnings
from threading import Thread

warnings.filterwarnings("ignore")

################CONFIGURATION OF THE TCP/IP CONNECTION AND SENSORS################
#TCP/IP client connection
address = '192.168.178.25'
port1 = 8086
port2 = 8087
port3 = 8088

client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket1.connect((address, port1))
client_socket2.connect((address, port2))
client_socket3.connect((address, port3))

client_socket1.send(bytes("Client 1 is connected to the server", 'utf-8'))
client_socket2.send(bytes("Client 2 is connected to the server", 'utf-8'))
client_socket3.send(bytes("Client 3 is connected to the server", 'utf-8'))
##################################################################################




###############SENDING THE DATA IN DIFFERENT THREADS##############
def sendData1():
    Data1 = "Data 1 in strings"
    client_socket1.send(Data1.encode())
    sleep(2)
    
def sendData2():
    Data2 = "Data 2 in strings"
    client_socket2.send(Data2.encode())
    sleep(2)

def sendData3():
    Data3 = "Data 3 in strings"
    client_socket3.send(Data3.encode())
    sleep(2)

##################################################################################

#main loop
while True:

    try:

        Thread1 = Thread(target = sendData1)
        Thread2 = Thread(target = sendData2)
        Thread3 = Thread(target = sendData3)

        Thread1.start()
        Thread2.start()
        Thread3.start()

    except KeyboardInterrupt:
        client_socket1.close()
        client_socket2.close()
        client_socket3.close()
        break