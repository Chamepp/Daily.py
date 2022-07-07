from simplecrypt import encrypt, decrypt

import socket
import threading
import time


# Setting Up Values
tLock = threading.Lock()
poweroff = False


# Gather
def receving(name, sock):
    while not poweroff:
        try:

            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(2048)
        except:
            pass
        finally:
            tLock.release()

# IP Details
host = '127.0.0.1'
port = 0
server = ('127.0.0.1', 5000)

# Socket Setup
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

# Gather Data
alias = input("Username: ")
time.sleep(0.2)

# Complete Process
message = input(alias + ">>> ")
while message != 'q':
    cryptmsg = encrypt("Fatec123", message)
    if message != "":
        #s.sendto(str(alias + ": " + cryptmsg).encode('utf-8'), server)
        s.sendto(cryptmsg, server)
        print(cryptmsg)
    tLock.acquire()
    message = input(alias + ">>> ")
    cryptmsg = encrypt("Fatec123", message)
    tLock.release()
    time.sleep(0.2)

# Finish Process
poweroff = True
rT.join()
s.close()
