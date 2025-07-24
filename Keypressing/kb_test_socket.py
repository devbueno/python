import keyboard as kb
import time

while True:
    if kb.is_pressed("w"):
            time.sleep(0.5)
            print("tecla pressionada", time.time())