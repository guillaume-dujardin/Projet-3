from Map import *
from Perso import *

#Message d'introduction au jeu

message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le à sortir indemne"
message_debut_modifier = message_debut.center(120,"*")
print(message_debut_modifier)


affiche_labyrinthe(labyrinthe) #afficher le labyrinthe

print("Vous êtes X et devez rejoindre la sortie ! Bonne chance...\n")
