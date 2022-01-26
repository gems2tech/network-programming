import threading
import socket

exitEvent = threading.Event()

host = '127.0.0.1' # localhost
port = 30333

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
pseudonyms = []
pseudonym_client = {}

quitMessage = "quit()"

#get the clients and send them a message
def broadcast(message):
    for client in clients:
        client.send(message)


# try to receive a message from client, and broadcast to other clients
def handle(client):
    while True:
        try: 
            message = client.recv(1024)

            messageString = message.decode('ascii') 
            receivedMessage = messageString.partition(':')[2]

            if quitMessage in receivedMessage:
                pseudonymSting = messageString.partition(':')[0]
                print(f"{pseudonymSting} wants to leave")
                #look for pseudonym in dict and remove client 
                if pseudonymSting in pseudonym_client:
                    # puts dict in a list to get the index 
                    # to find the client object trough the index 
                    pseudonymList = list(pseudonym_client)
                    pseudonymIndex = pseudonymList.index(pseudonymSting)
                    # gives client index as a parameter 
                    dismissClient(pseudonymIndex)
            else:           
                broadcast(message)

        except: 
        # disconnect to client, remove from list 
            index = client.index(client)
            clients.remove(client)
            client.close()
            pseudonym = pseudonyms[index]
            broadcast(f'{pseudonym} left the chat!'.encode('ascii'))
            pseudonyms.remove(pseudonym)
            break

def handshake():
    while True:
        #connect with client and print out it's address
        client, address = server.accept()
        print(f'Connected with Client: {address}')

        #send the word chat alias to client 
        client.send('Chat Alias'.encode('ascii'))
        #receive chat alias from client  
        pseudonym = client.recv(1024).decode('ascii')
        #put client and chat alias on list 
        pseudonyms.append(pseudonym)
        clients.append(client)
        pseudonym_client.update({pseudonym:client})

        # print chat alias of client on the server
        print(f'Chat alias of the client is {pseudonym}')
        # broadcast chat alias of client to clients list 
        broadcast(f'{pseudonym} joined the chat!\n'.encode('ascii'))

        client.send(f'{pseudonym}, you are connected to the server!'.encode('ascii'))

        #handle connection for a client 
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def dismissClient(index):
    #remove from list
    client= clients[index]
    pseudonym = pseudonyms[index]
    print(client)
    print(pseudonym)
    print(f'All clients are:\n{clients}')
    
    client.send('bye()'.encode('ascii'))
    clients.pop(index)
    pseudonyms.pop(index)

    broadcast(f'{pseudonym} left the chat!'.encode('ascii'))

    print("client Removed!")
    print(f'All clients are:\n{clients}')
    print(f'All pseudonyms are:\n{pseudonyms}')



print('Shh.. the server is listening!')
handshake()


