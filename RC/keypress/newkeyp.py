import keyboard
import time

# List initializing
ls = [False, False, False, False]
previous_list = [False, False, False, False]

speeds = {"w": 0, "s": 0, "a": 0, "d": 0}
prev_speeds = {"w": 0, "s": 0, "a": 0, "d": 0}

# Constants for key names
W_KEY = "w"
S_KEY = "s"
A_KEY = "a"
D_KEY = "d"

# Constants for speed limits
W_SPEED_LIMIT = 14
S_SPEED_LIMIT = 10
A_SPEED_LIMIT = 6
D_SPEED_LIMIT = 6

def update_speed(key, speed_limit):
    if ls[key]:
        speeds[key] += 1
        time.sleep(0.05)
        if speeds[key] >= speed_limit:
            speeds[key] = speed_limit
    else:
        speeds[key] = 0

    if speeds[key] != prev_speeds[key]:
        print(f"{key}: {speeds[key]}")
        prev_speeds[key] = speeds[key]

while True:
    ls = {
        W_KEY: keyboard.is_pressed(W_KEY),
        S_KEY: keyboard.is_pressed(S_KEY),
        A_KEY: keyboard.is_pressed(A_KEY),
        D_KEY: keyboard.is_pressed(D_KEY),
    }

    update_speed(W_KEY, W_SPEED_LIMIT)
    update_speed(S_KEY, S_SPEED_LIMIT)
    update_speed(A_KEY, A_SPEED_LIMIT)
    update_speed(D_KEY, D_SPEED_LIMIT)

    if ls != previous_list:
        print(ls)
        # client.send
        previous_list = ls.copy()
        # previous_list = ls[:]
        # previous_list = list(ls)
