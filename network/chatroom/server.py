import socket
import threading

host = socket.gethostname()
port = 9999

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat'.encode('ascii'))
            nicknames.remove(nicknames)
            break

def recieve():
    while True:
        client, addr = s.accept()
        print(f'Connected with {str(addr)}')

        client.send("PASS".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"Nickname of client is {nickname}")
        broadcast(f'{nickname} has joined the chat'.encode('ascii'))
        client.send('Connected to server'.encode('ascii'))
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

recieve()
