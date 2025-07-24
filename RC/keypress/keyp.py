import keyboard
import time

# List initializing
ls = [False, False, False, False]
previous_list = [False, False, False, False]

speed_list = [1, 1, 1, 1]
prev_speed_list = [1, 1, 1, 1]

speed_list[0] = 0          # w
speed_list[1] = 0          # s

speed_list[2] = 0          # a
speed_list[3] = 0          # d


while True:
    ls[0] = keyboard.is_pressed("w")
    ls[1] = keyboard.is_pressed("s")
    ls[2] = keyboard.is_pressed("a")
    ls[3] = keyboard.is_pressed("d")



    if ls[0] == True:            # W start
        speed_list[0] += 1
        time.sleep (0.05)
        if speed_list[0] >= 14:
            speed_list[0] = 14
    else:                           # W stop
        speed_list[0] = 0
    if speed_list != prev_speed_list:
        print(str(speed_list[0]))
        prev_speed_list = speed_list.copy()


    if ls[1] == True:           # S start
        speed_list[1] += 1
        time.sleep (0.05)
        if speed_list[1] >= 10:
            speed_list[1] = 10
    else:                          # S stop
        speed_list[1] = 0
    if speed_list != prev_speed_list:
        print(str(speed_list[1]))
        prev_speed_list = speed_list.copy()



    if ls[2] == True:          # A start
        speed_list[2] += 1
        time.sleep(0.05)
        if speed_list[2] >=6:
            speed_list[2] = 6
    else:
        speed_list[2] = 0       # A stop
    if speed_list != prev_speed_list:
        print(str(speed_list[2]))
        prev_speed_list = speed_list.copy()


    if ls[3] == True:
        speed_list[3] += 1
        time.sleep(0.05)
        if speed_list[3] >= 6:
            speed_list[3] = 6
    else:
        speed_list[3] = 0
    if speed_list != prev_speed_list:
        print(str(speed_list[3]))
        prev_speed_list = speed_list.copy()

    if ls != previous_list:
        print(ls)
        # client.send
        previous_list = ls.copy()
        # previous_list = ls[:]
        # previous_list = list(ls

        
