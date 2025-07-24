import keyboard
import time

# List initializing
ls = [False, False, False, False]
previous_list = [False, False, False, False]


speed_w = 0
speed_s = 0

while True:
    ls[0] = keyboard.is_pressed("w")
    ls[1] = keyboard.is_pressed("a")
    ls[2] = keyboard.is_pressed("s")
    ls[3] = keyboard.is_pressed("d")

    if ls[0] == True:
        speed_w += 1
        time.sleep (0.1)
        if speed_w >= 14:
            speed_w = 14

    if ls[0] == False:
        speed_w = 0
        time.sleep (0.1)

    if ls[2] == True:
        speed_s += 1
        time.sleep(0.1)
        if speed_s >=14:
            speed_s = 14

    if ls[2] == False:
        speed_s = 0
        time.sleep(0.1)

    if ls != previous_list:
        print(ls)
        # client.send
        previous_list = ls.copy()
        # previous_list = ls[:]
        # previous_list = list(ls

        
