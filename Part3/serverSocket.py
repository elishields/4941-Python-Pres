###################
# serverSocket.py #
###################

import socket
import sys
import os

HOST = '127.0.0.1'
PORT = 8090

# create
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
ss.bind((HOST, PORT))

# listen
ss.listen(5)

while True:
    try:
        # accept
        conn, addr = ss.accept()
        print("Connection from", addr)

        serverReceivesBytes = conn.recv(1024)
        serverReceives = serverReceivesBytes.decode()
        print("Received:\n", serverReceives)

        # send
        fileList = os.listdir(serverReceives)
        print(len(fileList))
        for curFile in fileList:
            curFile += "\n"
            fileBytes = curFile.encode()
            conn.sendall(fileBytes)
    except BrokenPipeError as e:
        print(e)
        sys.exit()

ss.close()
