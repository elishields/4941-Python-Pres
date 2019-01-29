###################
# clientSocket.py #
###################

import socket
import sys

HOST = '127.0.0.1'
PORT = 8090

# create
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
cs.connect((HOST, PORT))

# send
clientSends = input("Request a filepath\n> ")
clientSendsBytes = clientSends.encode()
cs.sendall(clientSendsBytes)

# receive
print("Server says:")
clientReceivesBytes = cs.recv(1024)
while clientReceivesBytes:
    clientReceives = clientReceivesBytes.decode()
    print(clientReceives)
    clientReceivesBytes = cs.recv(1024)

cs.close()
