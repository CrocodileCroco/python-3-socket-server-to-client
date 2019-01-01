import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
s.sendall('connected'.encode('utf-8'))
while True:
    try:
        data = s.recv(1024).decode('utf-8')
    except:
        pass
    if data != '':
        print ('Received', data)
