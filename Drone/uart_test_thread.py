import _thread
from machine import UART
import time
import motor_control

motor_control.set_motor_speeds(3000, 3000)

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

def uart_receive_thread():
    while True:
        if uart.any():
            data = uart.readline()
            if data:
                print("From Pi:", data.decode().strip())
        time.sleep(0.01)

# Start receive thread
_thread.start_new_thread(uart_receive_thread, ())

# Main thread: only user input + send
while True:
    try:
        user_input = input("You → ")
        uart.write((user_input + "\n").encode())
    except Exception as e:
        print("Error:", e)
