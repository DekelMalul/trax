import socket

PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.8.1"
ADDR = (SERVER, PORT)
HEADER = 100

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
msg = client.recv(HEADER).decode()

while msg != "exit" and len(msg) != 0:
    print(msg)
    msg = client.recv(HEADER).decode()
    
