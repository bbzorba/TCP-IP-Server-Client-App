import socket
import csv
from threading import Thread

#######################CONFIGURING TCP/IP CONNECTION#############################
ip_address = '192.168.178.25'
port1 = 8086
port2 = 8087
port3 = 8088

server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket1.bind((ip_address, port1))
server_socket2.bind((ip_address, port2))
server_socket3.bind((ip_address, port3))

print("Waiting for connection...")

server_socket1.listen()
connection1, address1 = server_socket1.accept()

server_socket2.listen()
connection2, address2 = server_socket2.accept()

server_socket3.listen()
connection3, address3 = server_socket3.accept()

print("Connections detected at... " + str(address1) + str(address2) + str(address3))
#################################################################################




############RECEIVING OF THE DATA FROM THE CLIENT AND WRITING INTO TEXT FILES###########
def receiveData1():
    message = connection1.recv(1024)
    print(message.decode())

    with open("sensorData/Data1.txt","a") as f:
        writer = csv.writer(f)
        writer.writerow([str(message.decode())])

    
def receiveData2():
    message = connection2.recv(1024)
    print(message.decode())

    with open("sensorData/Data2.txt","a") as f:
        writer = csv.writer(f)
        writer.writerow([str(message.decode())])
    
    
def receiveData3():
    message = connection3.recv(1024)
    print(message.decode())

    with open("sensorData/Data3.txt","a") as f:
            writer = csv.writer(f)
            writer.writerow([str(message.decode())])

########################################################################################



while(1):

    try:
    
        Thread1 = Thread(target = receiveData1)
        Thread2 = Thread(target = receiveData2)
        Thread3 = Thread(target = receiveData3)
        
        Thread1.start()
        Thread2.start()
        Thread3.start()
    
    except KeyboardInterrupt:
        server_socket1.close()
        server_socket2.close()
        server_socket3.close()
        break