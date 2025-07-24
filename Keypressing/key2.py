import keyboard

# List initializing
ls = [False, False, False, False]
previous_list = [False, False, False, False]


while True:
     ls[0] = keyboard.is_pressed("w")
     ls[1] = keyboard.is_pressed("a")
     ls[2] = keyboard.is_pressed("s")
     ls[3] = keyboard.is_pressed("d")


     if ls != previous_list:
         print(f'{ls}')
         # client.send
         previous_list = ls.copy()
         # previous_list = ls[:]
         # previous_list = list(ls)

       



    




