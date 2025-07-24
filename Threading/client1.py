import socket
import threading
import keyboard
import time

nickname = input("Choose a nickname: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('34.176.175.169', 45001))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
            
        except:
            print("Ocorreu um erro. Fechando conexão...")
            client.close()
            break

def write():
    while True:
        while True:
            x = False
            kp = keyboard.is_pressed("q")
            time.sleep(0.1)
            if kp != x:
                msg = 'ledon'
                client.send(msg.encode('ascii'))
                break

        while True:
            x = True
            kp = keyboard.is_pressed("q")
            time.sleep(0.1)
            if kp != x:
                msg = 'ledoff'
                client.send(msg.encode('ascii'))
                break



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


        