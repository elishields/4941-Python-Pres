###################
# serverSocket.py #
###################

import socket
import sys

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
        serverSends = "Num chars: " + str(len(serverReceives))
        serverSendsBytes = serverSends.encode()
        conn.sendall(serverSendsBytes)
    except BrokenPipeError as e:
        print(e)
        sys.exit()

ss.close()
