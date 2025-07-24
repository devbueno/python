from pythonping import ping
import threading
import pandas as pd

data = {
  "ip": [0, 0, 0],
  "st": [50, 40, 45]
}

df = pd.DataFrame(data)
df.shape(50, 50)

df.at[10, 10] = 50
