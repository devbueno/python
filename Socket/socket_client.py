import socket

HOST = "54.94.128.127"  # The server's hostname or IP address
PORT = 57434  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    dados = input("Input:")
    dados_enc = dados.encode('utf-8')
    s.send(dados_enc)
