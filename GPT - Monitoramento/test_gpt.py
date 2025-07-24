import tkinter as tk

# Define a função para atualizar a cor da caixa
def update_box_color(box, status):
    if status == "available":
        box.config(bg="green")
        box_label.config(text="Available")
    elif status == "unavailable":
        box.config(bg="red")
        box_label.config(text="Unavailable")

# Cria a janela principal
root = tk.Tk()
root.title("Monitoramento")

# Cria as caixas e labels
statuses = ["available", "unavailable", "available", "unavailable", "available",
            "unavailable", "available", "unavailable", "available", "unavailable",
            "available", "unavailable", "available", "unavailable", "available",
            "unavailable", "available", "unavailable", "available", "unavailable",
            "available", "unavailable", "available", "unavailable", "available"]

boxes = []
for row in range(5):
    for column in range(4):
        box_frame = tk.Frame(root, width=50, height=50, padx=5, pady=5, bg="white")
        box_label = tk.Label(box_frame, text="", font=("Arial", 10))
        box_label.pack(expand=True)
        box_frame.grid(row=row, column=column, padx=5, pady=5)
        boxes.append(box_frame)
        update_box_color(box_frame, statuses[row * 4 + column])

    box_frame = tk.Frame(root, width=50, height=50, padx=5, pady=5, bg="white")
    box_label = tk.Label(box_frame, text="", font=("Arial", 10))
    box_label.pack(expand=True)
    box_frame.grid(row=row, column=4, padx=5, pady=5)
    boxes.append(box_frame)
    update_box_color(box_frame, statuses[row * 4 + 4])

root.mainloop()
