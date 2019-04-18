#bahar boroomand
import socket
from _thread import *

# thread fuction
def threaded(client):
    while True:

        # receive data from client
        # 1024 is the buffer length
        data1 = client.recv(1024)
        if not data1:
            print('Bye')
            break


        # send back the same msg to client
        client.sendall(data1)

        print("client : %s" % data1.decode('utf-8'))

    # connection closed
    client.close()

def Main():

    # AF_INET refers to ipv4
    # SOCK_STREAM refers to TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SOL_SOCKET:Use this constant as the level argument to getsockopt or setsockopt
# to manipulate the socket-level options described in this section.
# SO_REUSEADDR: you can reuse the port number after running the program agian
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_add = ('localhost', 10100)

    print("server is running on %s:%d" % server_add)

    # A server has a bind() method
    # which binds it to a specific ip and port
    # so that it can listen to incoming requests on that ip and port
    sock.bind(server_add)

    # This allows the server to listen to incoming connections
    # 5 here means that 5 connections are kept waiting if the server is busy
    # and if a 6th socket tries to connect then the connection is refused.
    sock.listen(5)

    while True:

        # The accept method initiates a connection with the client
        # It returns a client socket and ip&port address
        client, addr = sock.accept()

        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (client,))

if __name__ == '__main__':
    Main()

