import random

choix = ["pierre", "feuille", "ciseaux"]

while True:

    joueur = input("Choisis pierre, feuille ou ciseaux : ")

    ordinateur = random.choice(choix)

    print("L'ordinateur a choisi :", ordinateur)

    if joueur == ordinateur:
        print("Égalité !")

    elif joueur == "pierre" and ordinateur == "ciseaux":
        print("Tu gagnes !")

    elif joueur == "feuille" and ordinateur == "pierre":
        print("Tu gagnes !")

    elif joueur == "ciseaux" and ordinateur == "feuille":
        print("Tu gagnes !")

    else:
        print("Tu perds !")

    rejouer = input("Tu veux rejouer ? oui/non : ")

    if rejouer == "non":
        print("Fin du jeu")
        break