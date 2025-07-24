import subprocess
import re

pattern =  "[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]"

out = subprocess.run("ipconfig", universal_newlines=True, capture_output=True, check=True)
out_n = str(out.stdout)
out_s = re.findall(pattern, out_n)
print(out_s)


             
