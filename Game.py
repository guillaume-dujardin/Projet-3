import os 
from Map import Map
from Character import Character
import time

class Game :

    def __init__(self):
        pass

    def init_game(self):
        self.character = Character()
        self.map = Map()        
        self.map.create_map("map.txt")
        
    def play(self):            
            self.init_game()
            continuer_game = 'O'
            while continuer_game != 'N' :
                player = ''
                partie = True                
                message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le a sortir indemne"
                message_debut_modifier = message_debut.center(120,"*")
                print(message_debut_modifier)
                
                self.map.display_map()
                
                while partie == True :
                    
                    player = input("Voulez vous allez en bas en haut a droite a gauche ? : ")                    
                    if player == "R" or player == "r" :                       
                        self.map = self.character.move_right(self.map)                            
                        if self.map.map_array[self.character.column][self.character.line + 1] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False                         
                    elif player == "L" or player == "l" :
                        self.map = self.character.move_left(self.map)
                        if self.map.map_array[self.character.column][self.character.line - 1] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    elif player == "D" or player == "d" :
                        self.map = self.character.move_down(self.map)
                        if self.map.map_array[self.character.column + 1][self.character.line] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    elif player == "U" or player == "u" :
                        self.map = self.character.move_up(self.map)    
                        if self.map.map_array[self.character.column - 1][self.character.line] == "O" and self.character.tresors == 3 :
                            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
                            partie = False
                    
                    
                    os.system('cls')
                    self.map.display_map()
                    
                    

                while partie == False :
                    continuer_game = input("Voulez vous recommencer la partie (OUI/NON) ? : ") 
                    if continuer_game == "OUI" or continuer_game == "oui" :                       
                        partie = True
                        self.init_game()
                        os.system('cls')
                    elif continuer_game == "NON" or continuer_game == "non" :
                        exit()
                    else :
                        print("C'est OUI ou NON")

