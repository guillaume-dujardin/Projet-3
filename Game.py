import os 
from Map import Map
from Character import Character
import time
from Constant import *



class Game :

    def __init__(self):
        pass

    def init_game(self):
        self.character = Character()
        self.map = Map()        
        self.map.create_map("map.txt")

        
    def play(self):      
           
            self.init_game()
            continue_game = 'O'
            while continue_game != 'N' :                
                game = True                
                start_message = "Vous incarner Mcgiver dans un labyrinthe ! Aider le a sortir indemne"
                start_message_edit = start_message.center(120,"*")
                print(start_message_edit)
                
                self.map.display_map()
                
                while game == True :
                    player = ""
                    player = input("L,D,R,U : ")

                    if player == "R" :                       
                        self.map = self.character.move_right(self.map)                            
                        if self.map.map_array[self.character.column][self.character.line + 1] == "O" and self.character.tresors == 3 :                                
                            game = False                         
                    elif player == "L" :
                        self.map = self.character.move_left(self.map)
                        if self.map.map_array[self.character.column][self.character.line - 1] == "O" and self.character.tresors == 3 :
                            game = False
                    elif player == "D" :
                        self.map = self.character.move_down(self.map)
                        if self.map.map_array[self.character.column + 1][self.character.line] == "O" and self.character.tresors == 3 :                               
                            game = False
                    elif player == "U" :
                        self.map = self.character.move_up(self.map)    
                        if self.map.map_array[self.character.column - 1][self.character.line] == "O" and self.character.tresors == 3 :                                
                            game = False
                    
                    
                    os.system('cls')
                    self.map.display_map()
                    
                    

                while game == False :
                    continue_game = input("Voulez vous recommencer la partie (OUI/NON) ? : ") 
                    if continue_game == "OUI" or continue_game == "oui" :                       
                        game = True
                        self.init_game()
                        os.system('cls')
                    elif continue_game == "NON" or continue_game == "non" :
                        exit()
                    else :
                        continue

