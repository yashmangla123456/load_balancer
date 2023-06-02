import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the local machine name
host = socket.gethostbyname(socket.gethostname())

print(host)

# set a port number for the server to listen on
port = 8000

# bind the socket object to a specific address and port number
server_socket.bind(("", port))

# set the maximum number of queued connections


server_socket.listen(5)
x = 0
for x in range(0, 10):
    # wait for a client to establish a connection
    client_socket, address = server_socket.accept()
    print("Got a connection from %s" % str(address))

    # send a message to the client
    message = "Thank you for connecting %s" %str(socket.gethostbyname(socket.gethostname()))
    client_socket.send(message.encode("ascii"))

    # close the client connection
    client_socket.close()