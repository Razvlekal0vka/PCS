import socket

sock = socket.socket()
sock.connect(('26.219.78.207', 9090))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print( data)