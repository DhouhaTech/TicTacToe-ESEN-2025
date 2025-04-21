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

def jeu():
    plateau = [" " for _ in range(9)]
    joueur_courant = "X"
    tour = 0

    while tour < 9:
        afficher_plateau(plateau)
        try:
            choix = int(input(f"Joueur {joueur_courant}, choisis une case (0-8) : "))
            if plateau[choix] != " ":
                print("Case déjà prise. Réessaye.")
                continue
        except (ValueError, IndexError):
            print("Choix invalide. Réessaye.")
            continue

        plateau[choix] = joueur_courant
        if verifier_victoire(plateau, joueur_courant):
            afficher_plateau(plateau)
            print(f"🎉 Joueur {joueur_courant} a gagné !")
            return

        joueur_courant = "O" if joueur_courant == "X" else "X"
        tour += 1

    afficher_plateau(plateau)
    print("Match nul !")

if __name__ == "__main__":
    jeu()

