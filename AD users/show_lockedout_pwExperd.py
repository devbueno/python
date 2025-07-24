import tkinter as tk
import subprocess

class ADUserStatusGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AD User Status Checker")
        
        # Create the username input field
        self.username_label = tk.Label(self.root, text="Enter the username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        # Create the check button
        self.check_button = tk.Button(self.root, text="Check", command=self.check_user_status)
        self.check_button.pack()
        
        # Create the password expired and locked out labels
        self.password_expired_label = tk.Label(self.root, text="")
        self.password_expired_label.pack()
        self.locked_out_label = tk.Label(self.root, text="")
        self.locked_out_label.pack()
        
    def check_user_status(self):
        # Get the username from the input field
        username = self.username_entry.get()
        
        # Run the PowerShell command to get the user's status
        command = f'powershell.exe -Command "Import-Module ActiveDirectory; Get-ADUser -Identity {username} -Properties PasswordExpired,LockedOut | Select-Object PasswordExpired,LockedOut"'
        output = subprocess.run(command, capture_output=True, text=True)
        
        # Parse the output and update the labels
        output_lines = output.stdout.split("\n")
        password_expired = output_lines[2].strip().lower() == "true"
        locked_out = output_lines[3].strip().lower() == "true"
        self.password_expired_label.config(text=f"Password expired: {password_expired}")
        self.locked_out_label.config(text=f"Locked out: {locked_out}")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ADUserStatusGUI()
    app.run()
