import keyboard
import threading

def press2():
    while True:
        if keyboard.read_key() == "":
             print(".")
        elif keyboard.read_key() == "q":
            break

press2_thread = threading.Thread(target=press2)
press2_thread.start()
