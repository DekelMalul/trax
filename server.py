import socket 
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)   
DISCONNECT = "exit"
IP_LIST = ['192.168.1.1','192.168.1.2']
MORSE_CODE_DICT = { '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-'}

try:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created successfuly.")
except socket.error as e:
    print(f"Socket creation faild {e}")

try: 
    server.bind(ADDR)
except socket.error as e:
    print(f"Cant bind to port {PORT} {e}")

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    # creating morse code for the ip address
    for ip in IP_LIST:
        morse = ""
        for letter in ip:
            morse += MORSE_CODE_DICT.get(letter)
        conn.send(morse.encode())
    conn.send(DISCONNECT.encode())
    conn.close()

def start():
    server.listen()
    print(f"[LISTENNING] Server is listenning on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

print ("[STARTING] Server is starting...")
start() 