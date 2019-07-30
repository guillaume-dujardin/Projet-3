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
        self.window = pygame.display.set_mode((side_window,side_window))
        self.background = pygame.image.load(IMAGE_FOND).convert()
        self.window.blit(self.background,(0,0)) # poster the background
        self.map.show(self.window) # allows the display of all the elements
        pygame.display.flip() # show all
        
    def play(self):      
            self.init_game()

            continuer_game = 'M'
            while continuer_game != 'N' :
                self.map.place_Items() # place the objects in the labyrinth
                self.initialisation() # intializes the pygame values
                self.map.display_map() # show the map in console
                game = True
                while game == True :

                    for event in pygame.event.get() : # for each pygame event
                        if event.type == QUIT :
                            exit() # function that leaves the program
                        if event.type == KEYDOWN :

                             if event.key == K_ESCAPE :
                                 exit()
                            
                             if event.key == pygame.K_RIGHT : # if the event is the right directional key
                                 self.character.move(self.map, 'right') # use the move function for moving
                             elif event.key == pygame.K_LEFT :
                                 self.character.move(self.map, 'left')
                             elif event.key == pygame.K_DOWN :
                                 self.character.move(self.map, 'down')
                             elif event.key == pygame.K_UP :
                                 self.character.move(self.map, 'up')

                             self.map.display_map() # show the map for each move
                             self.map.show(self.window) # allows the display of each element
                             pygame.display.flip() # show all

                        if self.map.map_array[self.character.column][self.character.line] == 'O' and self.map.score == 3 :
                            exit() # if the location is equal to "O" and the objects equal to three
                            self.map.to_Win(self.window) # apply the function to_win
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

