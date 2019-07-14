#!/usr/bin/python3
import os 
from Map import Map
from Character import Character

#Message d'introduction au jeu




    
class Game :

    def __init__(self):
        pass

    def jouer(self):
        if __name__ == "__main__" :

            self.y = 1
            self.x = 1
            message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le à sortir indemne"
            message_debut_modifier = message_debut.center(120,"*")
            print(message_debut_modifier)
            map = Map()

            map.create_map("map.txt") # Création de la carte
            map.display_map()   # Affichage de la carte
       
            character = Character()
    
            continuer_game = True
            player = ''
                
            while continuer_game :
                
                player = input("Voulez vous allez en bas en haut a droite a gauche ? : ")
                
                if player == "R" :
                    os.system('cls')
                    map = character.move_right(map)    
                    map.display_map()
                elif player == "L" :
                    os.system('cls')
                    map = character.move_left(map)    
                    map.display_map()
                elif player == "D" :
                    os.system('cls')
                    map = character.move_down(map) 
                    map.display_map()
                elif player == "U" :
                    os.system('cls')
                    map = character.move_up(map)    
                    map.display_map()
                else:
                    print("On avancera jamais avec",player)
                
            quitter = input("Voulez vous quitter ? : (OUI,NON)")
            if quitter == "OUI" :
                print("Vous arreter de jouer")
                continuer_game = False
                if continuer_game == False :
                    exit()
            elif quitter == "NON" :
                continuer_game = True


# Ajouter 3 tresors aleatoirement dans le labyrinthe a chaque début de jeu
# Permettre au joueur de recommencer la partie
# Donner un nom aux objets different ramasser dans le labyrinthe
# Recuperer la saisi utilisateur sur les touches directionnel pour directement faire une action

#alors tranchons pour map.py, on n'utilise pas de majuscule dans les noms de modules
#Pour le placement aléatoire, tu peux p.ex. utiliser random.sample() directement avec
# ta liste de positions des chemins. Cela tirera au sort des positions sans répétition 
# dans ta liste. Si tu n'as pas de liste de positions des chemins, tu peux en construire 
# une à la lecture du fichier décrivant la structure de labyrinthe.
                    
                
        
                   

parti_une = Game()
parti_une.jouer()
                       
    
    
    
    
    