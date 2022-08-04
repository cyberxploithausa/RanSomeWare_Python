import socket
from datetime import datetime
import os
import time

os.system("cls" if os.name == 'nt' else "clear")
time = datetime.now()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "192.168.43.112"
    #host = socket.gethostname()
    port = 5678
    s.bind((host, port))
    s.listen(3)
    

    while True:
        clisock, addr = s.accept()
        print(f"Receiving connection from %s on {time}" % str(addr))
        clisock.send(bytes(f"Welcome to the server. You connected on {time}", "utf-8"))
        message = clisock.recv(1024)
        print(message.decode("utf-8"))
        print()
        