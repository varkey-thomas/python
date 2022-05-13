import socket

host = socket.gethostname()
port = 9000

sock= socket.socket()

sock.bind((host,port))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    while data:
        print(data)
        data = conn.recv(1024)

    print("All data recieved")
conn.close()
