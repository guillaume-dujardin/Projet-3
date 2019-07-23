import os 
from Map import Map
from Character import Character
import time
import pygame
from pygame.locals import *
from Constante import *



class Game :

    def __init__(self):
        pass

    def init_game(self):
        self.character = Character()
        self.map = Map()        
        self.map.create_map("map.txt")
        pygame.init()

        
    def play(self):      
        
            self.init_game()
            window = pygame.display.set_mode((400,400)) # Affichage de la fenetre

            icon = pygame.image.load(picture_Mc) # Chargement de l'icone du joueur
            pygame.display.set_icon(icon)

            pygame.display.set_caption(picture_home)

            continue_game = 'O'
            while continue_game != 'N' :
                fond = pygame.image.load(picture_home).convert()
                game = True                
                start_message = "Vous incarner Mcgiver dans un labyrinthe ! Aider le a sortir indemne"
                start_message_edit = start_message.center(120,"*")
                print(start_message_edit)
                
                self.map.display_map()
                
                while game == True :
                    
                    for event in pygame.event.get() :
                        
                        if event.type == QUIT :
                            exit()

                        elif event.type == KEYDOWN :

                            if event.key == K_ESCAPE :
                                exit()

                            elif event.type == K_RIGHT :                       
                                self.map = self.character.move_right(self.map)                            
                                if self.map.map_array[self.character.column][self.character.line + 1] == "O" and self.character.tresors == 3 :                                
                                    game = False                         
                            elif event.type == K_LEFT :
                                self.map = self.character.move_left(self.map)
                                if self.map.map_array[self.character.column][self.character.line - 1] == "O" and self.character.tresors == 3 :
                                    game = False
                            elif event.type == K_DOWN :
                                self.map = self.character.move_down(self.map)
                                if self.map.map_array[self.character.column + 1][self.character.line] == "O" and self.character.tresors == 3 :                               
                                    game = False
                            elif event.type == K_UP :
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

