###################
# serverSocket.py #
###################

import threading
import socket
import sys
import os

HOST = '127.0.0.1'
PORT = 8090

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create
ss.bind((HOST, PORT)) # bind

def threadServer():
    ss.listen(5) # listen
    while True:
        try:
            conn, addr = ss.accept() # accept
            print("Connection from", addr)
            threading.Thread(target = dirReadThread, args = (conn, addr)).start()
        except BrokenPipeError as e:
            print(e)
            sys.exit()

def dirReadThread(conn, addr):
    while True:
        serverReceivesBytes = conn.recv(1024) # receive
        serverReceives = serverReceivesBytes.decode()
        print("Received:\n", serverReceives)

        # send
        fileList = os.listdir(serverReceives)
        print(len(fileList))
        for curFile in fileList:
            curFile += "\n"
            fileBytes = curFile.encode()
            conn.sendall(fileBytes)

threadServer()

ss.close()
