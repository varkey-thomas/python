import socket


host = socket.gethostname()
port = 6000

sock = socket.socket()
#sock.setblocking(0)

num1 = (input("Enter num 1 :"))
num2 = (input("Enter num 2 :"))
num3 = num1+','+num2

print("Sending data {0} to server".format(num3))

sock.connect((host,port))
#sock.send(bytes(num1))
#sock.send(bytes(num2))
sock.sendall(bytes(num3,'utf-8'))

data = sock.recv(1024)
print(int(data.decode()))
