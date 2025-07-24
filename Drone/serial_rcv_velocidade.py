import uasyncio as asyncio
from machine import UART
import shut
import motor_control
import _thread, sys

uart = UART(1, baudrate=115200)

VEL_ATUAL = 3351
VEL_MAX = 4512
VEL_MIN = 3300


async def receive_task():
    global VEL_ATUAL
    global VEL_MAX
    global VEL_MIN
    while True:
        if uart.any():
            data2 = uart.readline()
            data = data2.decode().strip()
            if data:
                try:
                    if data == 'w':
                        if VEL_ATUAL < VEL_MAX:
                            VEL_ATUAL += 20
                            motor_control.set_motor_speeds (VEL_ATUAL, 3000)
                            print("Velocidade atual: ", VEL_ATUAL)
                    if data == 's':
                        if VEL_MIN < VEL_ATUAL:
                            VEL_ATUAL -= 20
                            motor_control.set_motor_speeds (VEL_ATUAL, 3000)
                            print("Velocidade atual: ", VEL_ATUAL)
                                  #   print("receb:", data.decode().strip())
                except Exception as e:
                    print("err:", e)
        await asyncio.sleep(0.1)
        
async def main():
    await asyncio.gather(receive_task())

asyncio.run(main())