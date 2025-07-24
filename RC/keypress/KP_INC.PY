import keyboard
import time
speed_w = 0



while True:
    w_key = keyboard.is_pressed("w")
    if w_key == True:
        speed_w += 1
        time.sleep(0.1)
        print(str(speed_w) + " - " + str(w_key))
    if w_key == False:
        speed_w = 0
        time.sleep(0.1)
        print(str(speed_w) + " - " + str(w_key))
        

