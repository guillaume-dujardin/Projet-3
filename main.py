#!/usr/bin/python3
import os 
from Map import Map
from Character import Character

#Message d'introduction au jeu

message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le à sortir indemne"
message_debut_modifier = message_debut.center(120,"*")
print(message_debut_modifier)

if __name__ == "__main__" :
    
   
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
            map = character.move_right(map)    # Deplacement
            map.display_map()                  # Affichage après déplacement
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
        
        if character.victory(map):      # Non concluant
            continuer_game = False      # Non concluant
        
        
                        
    
    
    
    
    