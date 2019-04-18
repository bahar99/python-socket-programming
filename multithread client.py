#bahar boroomand
import socket
def Main():
    # AF_INET refers to ipv4
    # SOCK_STREAM refers to TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_add = ('localhost', 10100)

    print("connecting to the address : %s:%s" % server_add)

    try:
        # connect to the server on local computer
        sock.connect(server_add)

        # input function returns string
        msg = input("client : ")
        while msg != "exit":
            # encode convert string to bytes
            sock.sendall(msg.encode('utf-8'))

            # receive the data that the server have sent as bytes
            data = sock.recv(2048)

            print("received from server : %s" % data.decode('utf-8'))
            msg = input("client : ")
    # this exception is raised for address-related errors
    except socket.gaierror as e:
        print("socket error : %s" % str(e))
    except Exception as e:
        print(e)
    finally:
        # close method closes the connection with the client.
        sock.close()
if __name__ == '__main__':
    Main()