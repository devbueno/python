import socket as sc
import threading
import keyboard as kb
import time

s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

try:
    s.bind(('192.168.98.205', 12345))
    s.listen(1)
    print("Server is running on port 12345")
    conn, addr = s.accept()
    print("Connected to address: ", addr)

except Exception as e:
    print("Error binding to the port")
    print(e)

def receive_messages(conn):
    while True:
        msg = conn.recv(1024)
        print("Raspberry: ", msg.decode())



t1 = threading.Thread(target=receive_messages, args=(conn,))

t1.start()

while True:
    # msg = input()
    # conn.send(msg.encode())
    if kb.is_pressed("w"):
        time.sleep(0.5)
        msg = 'w'
        conn.send(msg.encode())
    if kb.is_pressed("s"):
        time.sleep(0.5)
        msg = 's'
        conn.send(msg.encode())








