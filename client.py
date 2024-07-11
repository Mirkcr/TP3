import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 33333))

message = "Hola, servidor"
client_socket.sendall(message.encode())

client_socket.close()
