import os 
from Map import Map
from Character import Character


class Game :

    def __init__(self):
        pass

    def init_game(self):
        self.character = Character()
        self.map = Map()        
        self.map.create_map("map.txt")   # Création de la carte
        

    def jouer(self):            
            self.init_game()
            continuer_game = 'O'
            while continuer_game != 'N' :
                player = ''
                partie = True                
                message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le a sortir indemne"
                message_debut_modifier = message_debut.center(120,"*")
                print(message_debut_modifier)
                
                self.map.display_map()   # Affichage de la carte
                
                while partie == True :
                    player = input("Voulez vous allez en bas en haut a droite a gauche ? : ")                    
                    if player == "R" :                        
                        self.map = self.character.move_right(self.map)                            
                        if self.map.map_array[self.character.y][self.character.x + 1] == "O" and self.character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif self.map.map_array[self.character.y][self.character.x + 1] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                            
                    elif player == "L" :
                        self.map = self.character.move_left(self.map)
                        if self.map.map_array[self.character.y][self.character.x - 1] == "O" and self.character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif self.map.map_array[self.character.y][self.character.x - 1] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    elif player == "D" :
                        self.map = self.character.move_down(self.map)
                        if self.map.map_array[self.character.y + 1][self.character.x] == "O" and self.character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif self.map.map_array[self.character.y + 1][self.character.x] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    elif player == "U" :
                        self.map = self.character.move_up(self.map)    
                        if self.map.map_array[self.character.y - 1][self.character.x] == "O" and self.character.tresors != 3 :
                            print("Tu ne peut pas passer sans avoir tout les objets")
                        elif self.map.map_array[self.character.y - 1][self.character.x] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False

                    os.system('cls')
                    self.map.display_map()

                while partie == False :
                    continuer_game = input("Voulez vous recommencer la partie (OUI/NON) ? : ") 
                    if continuer_game == "OUI" :                        
                        partie = True
                        self.init_game()
                        os.system('cls')
                    elif continuer_game == "NON" :
                        continuer_game = False
                        exit()
                    else :
                        print("C'est OUI ou NON")
              
                
                
            