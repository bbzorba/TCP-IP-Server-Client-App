import socket

while True:

    choice = input("pick server or client \n")

    if choice == "server":
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 8086))
        print("Waiting for connection...")
        server_socket.listen()
        connection, address = server_socket.accept()
        print("Connection detected at... " + str(address))
        break
    
    elif choice == "client":
        address = input("IP address of the server: ")
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((address, 8086))
        name = input("Name of the client: ")
        connection.send(bytes(name + " connected to the server", 'utf-8'))
        break
    
    else:
        print("invalid input")

while True:
    message = connection.recv(1024)
    print(message.decode())
    new_message = input("Type a message: ")
    connection.send(new_message.encode())
    
    if new_message == "end":
        connection.close()
        break
