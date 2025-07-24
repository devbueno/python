import time
import keyboard
a = 0

while True:
    if keyboard.is_pressed("w"):
        time.sleep(0.15)
        while keyboard.is_pressed("w"):
            a = a + 1
            print(a, a, a,a ,a ,a ,a ,a ,a)
            