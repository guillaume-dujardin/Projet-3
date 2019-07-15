#!/usr/bin/python3

from Game import Game

# Ajouter 3 tresors aleatoirement dans le labyrinthe a chaque debut de jeu
# Permettre au joueur de recommencer la partie
# Donner un nom aux objets different ramasser dans le labyrinthe
# Recuperer la saisi utilisateur sur les touches directionnel pour directement faire une action

#alors tranchons pour map.py, on n'utilise pas de majuscule dans les noms de modules
# Pour le placement aleatoire, tu peux peux. utiliser random.sample() directement avec
# ta liste de positions des chemins. Cela tirera au sort des positions sans repetition 
# dans ta liste. Si tu n'as pas de liste de positions des chemins, tu peux en construire 
# une a la lecture du fichier decrivant la structure de labyrinthe.
           
def play():   
    parti_une = Game()
    parti_une.jouer()
                   
if __name__ == "__main__" :
    play()