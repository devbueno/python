import tkinter as tk

def toggle_keyboard_input():
    global keyboard_input_enabled
    keyboard_input_enabled = not keyboard_input_enabled
    if keyboard_input_enabled:
        keyboard_input_button.config(text="Keyboard Input ON")
        text_box.config(state=tk.NORMAL)
    else:
        keyboard_input_button.config(text="Keyboard Input OFF")
        text_box.config(state=tk.DISABLED)

def handle_key(event):
    if keyboard_input_enabled:
        char = event.char
        text_box.insert(tk.END, char)

keyboard_input_enabled = False

root = tk.Tk()
root.title("Keyboard Input App")

text_box = tk.Text(root, height=10, width=30)
text_box.pack(pady=10)

keyboard_input_button = tk.Button(root, text="Keyboard Input OFF", command=toggle_keyboard_input)
keyboard_input_button.pack(pady=5)

toggle_keyboard_input()  # Ensure keyboard input starts off

root.bind("<Key>", handle_key)

root.mainloop()
