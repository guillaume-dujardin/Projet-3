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
                
                if character.victory(map) :
                    player = input("Voulez vous rejouer ? : ")
                    if player == "OUI" :
                        continuer_game = True
                    elif player == "NON" :
                        continuer_game = False
                        if continuer_game == False :
                            print("Vous arrêter de jouer")
                            exit()
                    else : print("C'est OUI ou NON")

# Ajouter 3 tresors aleatoirement dans le labyrinthe a chaque début de jeu
# resoudre le problème du "O" quand on finit la partie
# Permettre au joueur de recommencer la partie
# faire en sorte que le personnage ne puisse pas passez si il n'a pas tout les objets
# Donner un nom aux objets different ramasser dans le labyrinthe
# Recuperer la saisi utilisateur sur les touches directionnel pour directement faire une action
                    
                
        
                   

parti_une = Game()
parti_une.jouer()
                       
    
    
    
    
    