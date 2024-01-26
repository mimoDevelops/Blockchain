import socket

# Client function to send a message
def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    client_socket.sendall(message.encode())
    client_socket.close()

# Example usage
send_message("Hello from client!")
