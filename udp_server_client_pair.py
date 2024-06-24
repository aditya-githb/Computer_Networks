#code for server

import socket

HOST = '127.0.0.1'
PORT = 8080        

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f'Server listening on {HOST}:{PORT}...')

        while True:
            data, addr = server_socket.recvfrom(1024)
            print(f"Received message from {addr}: {data.decode()}")

            message = "Hello from server"
            server_socket.sendto(message.encode(), addr)
            print("Sent response back to", addr)

if __name__ == '__main__':
    main()

#code for client

import socket

HOST = '127.0.0.1' 
PORT = 8080        

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = "Hello from client"

        client_socket.sendto(message.encode(), (HOST, PORT))
        print("Message sent to server.")

        data, addr = client_socket.recvfrom(1024)
        print(f"Received response from server: {data.decode()}")

if __name__ == '__main__':
    main()
