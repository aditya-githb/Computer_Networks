import socket

def start_server():
    host = '0.0.0.0'  
    port = 3456

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on port {port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received from client: {data.decode()}")

                client_socket.sendall(data)
    server_socket.close()

if __name__ == "__main__":
    start_server()
