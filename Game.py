import os 
from Map import Map
from Character import Character


class Game :

    def __init__(self):
        pass

    def jouer(self):        
            
            self.y = 1
            self.x = 1
            message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le a sortir indemne"
            message_debut_modifier = message_debut.center(120,"*")
            print(message_debut_modifier)
            map = Map()
            print(map.case_libre)
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