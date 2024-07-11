import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 33333))
server_socket.listen(1)
print("Servidor TCP escuchando en puerto 12345")

conn, addr = server_socket.accept()
print(f"Conexión desde {addr}")

data = conn.recv(1024)
print(f"Recibido: {data.decode()}")

conn.close()
