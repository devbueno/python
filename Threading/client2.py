import socket
import threading
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = 16
GPIO.setup(LED,GPIO.OUT)

nickname = input("Seu nickname: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('34.176.175.169', 45001))

def receive():
    while True:
        try:
            message = client.recv(512).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            if message == 'ledon':
                GPIO.output(LED, 1)
            if message == 'ledoff':
                GPIO.output(LED, 0)
            
        except:
            print("Ocorreu um erro. Fechando conexão...")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

        