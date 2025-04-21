import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP connection
server_socket.bind(('localhost', 12345))  # Binding server to localhost and port 12345
server_socket.listen(2)  # We are allowing 2 connections (for 2 players)

print("Le serveur attend les connexions...")

# Accept connections from two players (clients)
client1, addr1 = server_socket.accept()
print(f"Joueur 1 connecté depuis {addr1}")

client2, addr2 = server_socket.accept()
print(f"Joueur 2 connecté depuis {addr2}")

# Send the starting message to both clients
client1.send("Bienvenue dans le jeu Tic Tac Toe ! Tu es le joueur X.".encode())
client2.send("Bienvenue dans le jeu Tic Tac Toe ! Tu es le joueur O.".encode())

# For now, after both players are connected and receive their messages, we close the connection
client1.close()
client2.close()
server_socket.close()
