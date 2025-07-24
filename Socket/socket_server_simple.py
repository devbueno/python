import socket

HOST = "172.31.47.132"
PORT = 57434


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while(True):
            try:
                de = conn.recv(1024)
                dd = de.decode('utf-8')
                print(dd)
                if(dd == "stop"):
                    break
            except:
                s.close()




#        while True:
#           data = conn.recv(1024)
#            data_dec = data.decode('utf8')
#            print(data_dec)