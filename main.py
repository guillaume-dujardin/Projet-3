#!/usr/bin/python3
import os 
from Map import Map
from Character import Character

#Message d'introduction au jeu

message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le à sortir indemne"
message_debut_modifier = message_debut.center(120,"*")
print(message_debut_modifier)

if __name__ == "__main__" :
    
    ## We create a map object
    ## This object store all character useful methods and variables

    map = Map()

    map.create_map("map.txt")
    map.display_map()
    
   

    # We create a character objet
    # This object store all character useful methods and variable
    
    character = Character()

    ## Example of interaction between character and map
    ## We move the character on map and we display the map
    
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
            print("Entree invalide")
        
        character.victory(map)
        
        
                        
    
    
    
    
    