def afficher_plateau(plateau):
    print(f"{plateau[0]} | {plateau[1]} | {plateau[2]}")
    print("--+---+--")
    print(f"{plateau[3]} | {plateau[4]} | {plateau[5]}")
    print("--+---+--")
    print(f"{plateau[6]} | {plateau[7]} | {plateau[8]}")

def verifier_victoire(plateau, joueur):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for combo in combinaisons_gagnantes:
        if all(plateau[i] == joueur for i in combo):
            return True
    return False

