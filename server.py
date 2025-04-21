import socket
import threading
from game_logic import verifier_victoire, afficher_plateau, update_board

HOST = '127.0.0.1'  # Localhost (for now, can use your server IP for a remote one)
PORT = 12345         # Port number to listen on

def handle_client(client_socket):
    # Function to handle each client connection
    client_socket.send("Welcome to Tic Tac Toe! You're connected.".encode('utf-8'))
    
    plateau = [" "] * 9  # Empty board
    joueur = "X"         # Start with player X
    
    while True:
        try:
            # Receive the move from the client (expecting a number between 1-9)
            move = client_socket.recv(1024).decode('utf-8')
            if not move:
                break

            move = int(move)  # Convert to integer

            # Update board
            updated_board = update_board(plateau, move, joueur)
            if updated_board is not None:
                plateau = updated_board

                # Check if the player has won
                if verifier_victoire(plateau, joueur):
                    client_socket.send(f"{joueur} wins!".encode('utf-8'))
                    break
                # Switch to the other player
                joueur = "O" if joueur == "X" else "X"
                afficher_plateau(plateau)  # Display the updated board
                client_socket.send("Your move was successful.".encode('utf-8'))
            else:
                client_socket.send("Invalid move, try again.".encode('utf-8'))

        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

def start_server():
    # Start the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Connection established with {addr}")
        
        # Handle each client in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
