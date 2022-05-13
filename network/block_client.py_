import socket

host = socket.gethostname()
port = 9000
sock = socket.socket()

sock.connect((host,port))

sock.setblocking(0)

data = 10*1024*1024

assert sock.send(bytes(data))
