import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the IP address of the server
server_address = (
    "192.168.249.250",
    8000,
)  # replace with the actual IP address of the server

# connect to the server
client_socket.connect(server_address)
# receive data from the server
data = client_socket.recv(1024).decode("utf-8")
print("Received data from server: %s" % data)

# send a message to the server
message = "Hello, server!"
client_socket.send(message.encode("utf-8"))


# close the socket
client_socket.close()
