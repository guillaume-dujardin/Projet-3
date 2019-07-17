import os 
from Map import Map
from Character import Character


class Game :

    def __init__(self):
        pass

    def jouer(self):        
            map = Map()
            character = Character()
            continuer_game = 'O'
            while continuer_game != 'N' :
                print(map.case_libre)                
                player = ''
                partie = True                
                message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le a sortir indemne"
                message_debut_modifier = message_debut.center(120,"*")
                print(message_debut_modifier)
                map.create_map("map.txt")   # Création de la carte
                map.display_map()   # Affichage de la carte
                
                while partie == True :
                    player = input("Voulez vous allez en bas en haut a droite a gauche ? : ")                    
                    if player == "R" :
                        os.system('cls')
                        map = character.move_right(map)    
                        map.display_map()
                        if map.map_array[character.y][character.x + 1] == "O" and character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif map.map_array[character.y][character.x + 1] == "O" and character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                            
                    elif player == "L" :
                        os.system('cls')
                        map = character.move_left(map)    
                        map.display_map()
                        if map.map_array[character.y][character.x - 1] == "O" and character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif map.map_array[character.y][character.x - 1] == "O" and character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    elif player == "D" :
                        os.system('cls')
                        map = character.move_down(map) 
                        map.display_map()
                        if map.map_array[character.y + 1][character.x] == "O" and character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif map.map_array[character.y + 1][character.x] == "O" and character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    elif player == "U" :
                        os.system('cls')
                        map = character.move_up(map)    
                        map.display_map()
                        if map.map_array[character.y - 1][character.x] == "O" and character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif map.map_array[character.y - 1][character.x] == "O" and character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    else:
                        print("On avancera jamais avec",player)
                while partie == False :
                    continuer_game = input("Voulez vous recommencer la partie (OUI/NON) ? : ") 
                    if continuer_game == "OUI" :                        
                        partie = True
                        os.system('cls')
                    elif continuer_game == "NON" :
                        continuer_game = False
                        exit()
                    else :
                        print("C'est OUI ou NON")
              
                
                
            