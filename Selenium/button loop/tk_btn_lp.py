import tkinter as tk
import threading
import time

running = False
start_button = None
stop_button = None

def start_loop():
    global running, start_button, stop_button
    running = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    threading.Thread(target=loop).start()

def stop_loop():
    global running, start_button, stop_button
    running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def loop():
    global running
    while running:
        print("Loop is running...")
        # Your loop logic goes here
        time.sleep(1)  # Simulating some work

root = tk.Tk()

start_button = tk.Button(root, text="Start", command=start_loop)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_loop, state=tk.DISABLED)
stop_button.pack()

root.mainloop()
