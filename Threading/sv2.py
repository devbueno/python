import socket
import RPi.GPIO as GPIO
#import time
#import threading
 
GPIO.setmode(GPIO.BCM)
LED = 16
GPIO.setup(LED,GPIO.OUT)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ip', port))


while True:
    msg_rcv = s.recv(1024).decode('ascii')
    if msg_rcv == True:
        GPIO.output(LED, 1)



