import socket

host = input("Enter host name")
t_ip = socket.gethostbyname(host)

t_port = 80

sock = socket.socket()

sock.connect((t_ip,t_port))
sock.send(bytes('GET HTTP/1.1 \r\n', 'ascii'))

ret = sock.recv(1024)
print('[+]'+str(ret))

