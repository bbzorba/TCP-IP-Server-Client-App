import socket
import csv

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.10', 8086))
print("Waiting for connection...")
server_socket.listen()
connection, address = server_socket.accept()
print("Connection detected at... " + str(address))

while True:
    message = connection.recv(1024)
    print(message.decode())

    with open("test_data.txt","a") as f:
            writer = csv.writer(f)
            writer.writerow([str(message.decode())])

#connection.close()