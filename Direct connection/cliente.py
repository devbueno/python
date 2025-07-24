import socket
import threading

host = 'localhost'
port = 27002

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host, port))

def recebe():
    while True:
        data = socket.recv(1024).decode('utf-8')
        print(data)

def envia():
    while True:
        msg = print(input("Digite uma mensagem:"))
        socket.send(msg.encode('ascii'))

recebe_thread = threading.Thread(target=recebe)
recebe_thread.start()