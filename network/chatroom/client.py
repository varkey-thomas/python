import socket
import threading
nickname = input("Choose a nickname :")

host = socket.gethostname()
port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'PASS':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("error occured")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}:{input("")}'
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
