import socket
import sys

name = input('Enter host name')
host = socket.gethostbyname(name)
print(host)
beg = int(input("Enter start :"))
end = int(input("Enter stop :"))

def hello():
    print("hello")

def portscan(port):
    sock = socket.socket()
    try:
        sock.connect((host,port))
        return True
    except:
        return False
    print("Port scanning complete")


for i in range(beg,end):
    result = portscan(i)
    if result:
        print("Port {}: Open".format(i))
    else:
        print("Port {}: Closed".format(i))
