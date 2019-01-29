###################
# clientSocket.py #
###################

import socket
import sys

HOST = '127.0.0.1'
PORT = 8090

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create
cs.connect((HOST, PORT)) # connect

clientSends = input("Request a filepath\n> ")
clientSendsBytes = clientSends.encode()
cs.sendall(clientSendsBytes) # send

print("Server says:")
clientReceivesBytes = cs.recv(1024) # receive
while clientReceivesBytes:
    clientReceives = clientReceivesBytes.decode()
    print(clientReceives)
    clientReceivesBytes = cs.recv(1024)

cs.close()
