import socket
import threading

host = 'localhost'
port = 27000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen()

print('Aguardando conexão de um cliente.')

client, ip = socket.accept()

print('Conectado com: ', ip)

def recebe():
    while True:
        mensagem = client.recv(1024).decode('utf-8')
        print(mensagem)

def envia():
    while True:
        mensagem2 = input("")
        client.send(mensagem2.encode('utf-8'))

recebe_thread = threading.Thread(target=recebe)
recebe_thread.start()

envia_thread = threading.Thread(target=envia)
envia_thread.start()

    

