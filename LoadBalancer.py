import socket
import threading

SERVERS = [("192.168.60.1", 8000), ("192.168.249.22", 8000)]

class LoadBalancer:
    def __init__(self, port):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port
        print(socket.gethostbyname(socket.gethostname()))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Load balancer listening on {self.host}:{self.port}")

    def handle_request(self, client_socket, client_address):
        print(f"Received request from {client_address}")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for server in SERVERS:
            try:
                print(f"Trying to connect to server {server[0]}:{server[1]}")
                server_socket.connect(server)
                server_socket.sendall(b"Hello from the load balancer!")
                response = server_socket.recv(1024)
                client_socket.sendall(response)
                print(f"Forwarded response from server {server[0]}:{server[1]} to {client_address}")
                server_socket.close()
                return
            except:
                print(f"Failed to connect to server {server[0]}:{server[1]}")
                continue
        client_socket.sendall(b"No servers available to handle the request.")
        client_socket.close()

    def start(self):
        while True:
            client_socket, client_address = self.socket.accept()
            threading.Thread(target=self.handle_request, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    load_balancer = LoadBalancer(8000)
    load_balancer.start()
