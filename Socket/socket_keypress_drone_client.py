import socket as sc

s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
s.settimeout(5)

while True:
    try:
        addr = input("IP:")
        port = int(input("Porta:"))
        s.connect((addr, port))
        print("Connected to address: ", addr)
        while True:
            msg = input("Msg:")
            s.send(msg.encode())
            if msg == "exit":
                s.close()
                break
    except Exception as e:
        print("Error connecting to the server")
        print(e)
