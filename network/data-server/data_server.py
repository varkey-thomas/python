import socket

host = socket.gethostname()
port = 6000

sock = socket.socket()
sock.bind((host,port))
sock.listen(5)

conn, addr = sock.accept()

print('connected to ', addr)

while True:
    data = conn.recv(1024)
    data1 = str(data.decode())
    data1.split(',')
    print(data1)
    print(len(data1))
    print(data1[0])
    result = int(data1[0]) + int(data1[2])
    conn.send(bytes(str(result),'utf-8'))
conn.close()


