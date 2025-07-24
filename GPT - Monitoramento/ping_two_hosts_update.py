import os
import platform
import tkinter as tk

# Define a function to ping a device and return True if successful
def ping(host):
    if platform.system().lower() == 'windows':
        response = os.system(f'ping -n 1 -w 1000 {host} > nul 2>&1')
        return response == 0
    else:
        response = os.system(f'ping -c 1 -w 1000 {host} > /dev/null 2>&1')
        return response == 0

# Define a function to update the ping status for each device
def update_ping_status():
    status1 = ping(entry1.get())
    status2 = ping(entry2.get())
    if status1:
        label1.config(text='Machine 1 is online', bg='green')
    else:
        label1.config(text='Machine 1 is offline', bg='red')
    if status2:
        label2.config(text='Machine 2 is online', bg='green')
    else:
        label2.config(text='Machine 2 is offline', bg='red')
    root.after(5000, update_ping_status)

# Create the GUI window and widgets
root = tk.Tk()
root.title('Ping Monitor')
root.geometry('300x200')
root.resizable(False, False)

label1 = tk.Label(root, text='Machine 1 is offline', bg='red', width=15)
label1.grid(row=0, column=0, padx=5, pady=5)
label2 = tk.Label(root, text='Machine 2 is offline', bg='red', width=15)
label2.grid(row=0, column=1, padx=5, pady=5)

entry1 = tk.Entry(root, width=15)
entry1.grid(row=1, column=0, padx=5, pady=5)
entry1.insert(0, '192.168.1.1')
entry2 = tk.Entry(root, width=15)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.insert(0, '192.168.1.2')

button = tk.Button(root, text='Update', command=update_ping_status)
button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI main loop
root.after(0, update_ping_status)
root.mainloop()
