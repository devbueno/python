import subprocess
import re



from macpath import split

pattern = "[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]"

out = subprocess.run("query user /server:192.168.0.5", universal_newlines=True, capture_output=True)
out_n = str(out)

