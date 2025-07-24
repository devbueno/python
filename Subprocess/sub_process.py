import subprocess


texty = subprocess.call('ping 192.168.0.1', shell=True)

print(str(texty))