import socket

HOST = '127.0.0.1'  # Server's IP address
PORT = 12345         # Same port as the server

def start_client():
    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    # Receive initial message from the server
    welcome_message = client.recv(1024).decode('utf-8')
    print(welcome_message)
    
    while True:
        # Ask the user to input their move (number 1-9)
        move = input("Enter your move (1-9): ")

        # Send the move to the server
        client.send(move.encode('utf-8'))

        # Receive and display the updated board from the server
        updated_board = client.recv(1024).decode('utf-8')
        print(updated_board)

        # Optionally, check for game over condition (win/loss)
        # If game is over, break the loop (You need to implement game over check on the client side)

    client.close()

if __name__ == "__main__":
    start_client()
