import uasyncio as asyncio
from machine import UART
import shut

uart = UART(1, baudrate=115200)

async def send_task():
    while True:
        msg = input("msg: ")
        uart.write(msg + "\n")
        await asyncio.sleep(0.1)

async def receive_task():
    while True:
        if uart.any():
            data = uart.readline()
            if data:
                try:
                    print("receb:", data.decode().strip())
                except Exception as e:
                    print("err:", e)
        await asyncio.sleep(0.1)
        
async def main():
    await asyncio.gather(send_task(), receive_task())

asyncio.run(main())

