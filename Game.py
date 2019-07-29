import os 
from Map import Map
from Character import Character
from Constant import *
import time
import pygame
from pygame.locals import *

class Game :

    def __init__(self):
        pass

    def init_game(self):
        self.character = Character()
        self.map = Map()        
        self.map.create_map("ressources/map.txt")

    def initialisation(self) :
        pygame.init()
        self.window = pygame.display.set_mode((cote_fenetre,cote_fenetre))
        self.fond = pygame.image.load(IMAGE_FOND).convert()
        self.window.blit(self.fond,(0,0)) # affiche le fond
        self.map.show(self.window) # affiche les elements sur le fond
        pygame.display.flip()
        
    def play(self):      
            self.init_game()

            continuer_game = 'M'
            while continuer_game != 'N' :
                self.map.place_Items()
                self.initialisation()
                self.map.display_map()
                game = True
                while game == True :

                    for event in pygame.event.get() :
                        if event.type == QUIT :
                            exit()
                        if event.type == KEYDOWN :

                             if event.key == K_ESCAPE :
                                 exit()
                            
                             if event.key == pygame.K_RIGHT :
                                 self.character.move(self.map, 'right')
                             elif event.key == pygame.K_LEFT :
                                 self.character.move(self.map, 'left')
                             elif event.key == pygame.K_DOWN :
                                 self.character.move(self.map, 'down')
                             elif event.key == pygame.K_UP :
                                 self.character.move(self.map, 'up')

                             self.map.display_map()
                             self.map.show(self.window)
                             pygame.display.flip()

                        if self.map.map_array[self.character.column][self.character.line] == 'O' and self.map.score == 3 :
                            exit()
                            self.map.to_Win(self.window)
                        if self.map.map_array[self.character.column][self.character.line] == 'O' and self.map.score < 3 :
                            exit()
                            self.map.to_Lose(self.window)
                        
            
                    
                    

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

