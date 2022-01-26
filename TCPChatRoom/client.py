import os
import signal

import socket
import threading

exitEvent = threading.Event()

chatAlias = input("Choose a chat alias: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',30333))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'Chat Alias':
                client.send(chatAlias.encode('ascii'))
            elif message == 'bye()':
                print('Connection Closed, program closed')
                client.close()
                exitEvent.set()
                if exitEvent.is_set():
                    os.kill(os.getpid(), signal.SIGINT)
                    break
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break
    


def write():
    while True:
        message = f'{chatAlias}: {input("")}'
        client.send(message.encode('ascii'))
  
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()        

write_thread = threading.Thread(target=write)
write_thread.start()


