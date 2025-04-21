import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to the server at localhost:12345

# Receive welcome message from the server
welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

# Close the connection after receiving the message
client_socket.close()
