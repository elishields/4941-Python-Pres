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
clientSends = input("What do you want to say to the server?\n> ")
clientSendsBytes = clientSends.encode()
cs.sendall(clientSendsBytes)

# receive
clientReceivesBytes = cs.recv(1024)
clientReceives = clientReceivesBytes.decode()

print("Server says:\n", clientReceives)

cs.close()
