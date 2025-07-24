from machine import UART, Pin
import time
import shut

print("rs")
uart = UART(1, baudrate=115200) # deve dar match no 0 ou 1 caso na porta seja UART1 ou UART0 conforme o pinout da placa
#uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

while True:
    uart.write("Hello from Pico\n")
    time.sleep(1)
    data = uart.readline()
    if data:
        print(data.decode().strip())