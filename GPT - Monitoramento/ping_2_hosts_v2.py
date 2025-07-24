import tkinter as tk
import threading
import time
from pythonping import ping


class Pinger:
    def __init__(self, target, interval=5):
        self.target = target
        self.interval = interval
        self.last_ping_status = None
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._ping_loop)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def _ping_loop(self):
        while self.running:
            response = ping(self.target, count=1, timeout=1000)
            ping_status = response.success
            if ping_status != self.last_ping_status:
                self.last_ping_status = ping_status
                self.on_ping_status_changed(ping_status)
            time.sleep(self.interval)

    def on_ping_status_changed(self, ping_status):
        pass


class PingCell(tk.Frame):
    def __init__(self, parent, name, target):
        super().__init__(parent)
        self.name = name
        self.target = target
        self.label = tk.Label(self, text=name, font=("Arial", 16))
        self.label.pack(side=tk.TOP, pady=10)
        self.status_label = tk.Label(self, text="", font=("Arial", 16))
        self.status_label.pack(side=tk.TOP, pady=10)
        self.pinger = Pinger(target)
        self.pinger.on_ping_status_changed = self.on_ping_status_changed

    def start(self):
        self.pinger.start()

    def stop(self):
        self.pinger.stop()

    def on_ping_status_changed(self, ping_status):
        color = "green" if ping_status else "red"
        text = "Pinging" if ping_status else "Offline"
        self.status_label.config(text=text, fg=color)


class App(tk.Frame):
    def __init__(self, parent, machine1, machine2):
        super().__init__(parent)
        self.machine1 = machine1
        self.machine2 = machine2
        self.cells = [
            PingCell(self, machine1["name"], machine1["target"]),
            PingCell(self, machine2["name"], machine2["target"]),
        ]
        for cell in self.cells:
            cell.pack(side=tk.LEFT, padx=50)
        self.pack(side=tk.TOP, padx=50, pady=50)

    def start(self):
        for cell in self.cells:
            cell.start()

    def stop(self):
        for cell in self.cells:
            cell.stop()


if __name__ == "__main__":
    machines = [
        {"name": "Google", "target": "google.com"},
        {"name": "Facebook", "target": "uhsdoaddo.com"},
    ]
    root = tk.Tk()
    app = App(root, *machines)
    app.start()
    root.mainloop()
    app.stop()