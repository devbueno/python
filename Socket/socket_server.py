import socket

HOST = "172.31.47.132"
PORT = 57434

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                de = conn.recv(1024)
                if not de:
                    break
                dd = de.decode('utf-8')
                print(dd)
            print("Cliente desconectado.")
