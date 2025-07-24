import tkinter as tk
import random

# Define a função para atualizar a cor da caixa
def update_box_color(box, status):
    if status == "available":
        box.config(bg="green")
        box_label.config(text="Available")
    elif status == "unavailable":
        box.config(bg="red")
        box_label.config(text="Unavailable")

# Define a função para atualizar as caixas
def update_boxes():
    for i in range(len(boxes)):
        status = random.choice(states)
        update_box_color(boxes[i], status)
    root.after(5000, update_boxes)

# Cria a janela principal
root = tk.Tk()
root.title("Monitoramento")

# Cria as caixas e labels
states = ["available", "unavailable"]
boxes = []
for row in range(5):
    for column in range(4):
        box_frame = tk.Frame(root, width=50, height=50, padx=5, pady=5, bg="white")
        box_label = tk.Label(box_frame, text="", font=("Arial", 10))
        box_label.pack(expand=True)
        box_frame.grid(row=row, column=column, padx=5, pady=5)
        boxes.append(box_frame)
        update_box_color(box_frame, random.choice(states))

    box_frame = tk.Frame(root, width=50, height=50, padx=5, pady=5, bg="white")
    box_label = tk.Label(box_frame, text="", font=("Arial", 10))
    box_label.pack(expand=True)
    box_frame.grid(row=row, column=4, padx=5, pady=5)
    boxes.append(box_frame)
    update_box_color(box_frame, random.choice(states))

# Chama a função de atualização das caixas a cada 5 segundos
root.after(5000, update_boxes)

root.mainloop()
