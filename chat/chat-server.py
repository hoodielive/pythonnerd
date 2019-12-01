import sys
import socket
import select

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009

def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(HOST, PORT)
    server_socket.listen(10)

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    print("Chat server started on port " + str(PORT))

    while 1:
        # get the list sockets which are ready to be read through select
        # 4th arg, time_out = 0 : poll and never block
