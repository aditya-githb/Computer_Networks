import socket

def start_client():
    host = 'localhost'
    port = 3456

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        print(f"Connected to server on port {port}")
        
        while True:
            message = input("Enter message to send (type 'exit' to close): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
            
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
