import os 
from Map import Map
from Character import *
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
        self.background = pygame.image.load(IMAGE_BACKGROUND).convert()
        self.window.blit(self.background,(0,0)) # poster the background
        self.map.show(self.window) # allows the display of all the elements
        pygame.display.flip() # show all
    
    def key_right(self) :                           
        self.character.move(self.map, 'right', self.window) # use the move function for moving
        if self.character.verif_win(self.character.column,self.character.line + 1) == True :
            self.win()
            game = False
        elif self.character.verif_loose(self.character.column,self.character.line + 1) == True :
            self.loose()
            game = False
        
    def win(self) :
        self.map.to_Win(self.window)
        pygame.display.flip()
        time.sleep(2)

    def loose(self) :
        self.map.to_Lose(self.window)
        pygame.display.flip()
        time.sleep(2)

    def display_finish_home(self,window) :
        self.home = pygame.image.load(IMAGE_HOME).convert()
        self.window.blit(self.home,(0,0))
        myfont = pygame.font.SysFont("comicsansms", 40)
        self.score_text = myfont.render(" Start again ? ", 1, (0, 0, 255))
        self.window.blit(self.score_text, (100, 80))
        self.score_text = myfont.render("F1 for yes F2 for no", 1 ,(0, 0, 225))
        self.window.blit(self.score_text, (35, 130))
        pygame.display.flip()

    def display_home(self,window) :
        self.first_home = pygame.image.load(IMAGE_FIRST_HOME).convert()
        self.window.blit(self.first_home,(0,0))
        self.play_button = pygame.image.load(IMAGE_PLAY_BUTTON).convert()
        self.window.blit(self.play_button,(110,300))
        self.blue_button = pygame.image.load(IMAGE_BLUE_BUTTON).convert()
        self.window.blit(self.blue_button,(110,200))
        myfont = pygame.font.SysFont("comicsansms", 25)
        self.score_text = myfont.render("REGLES DU JEU", 1 ,(0, 0, 225))
        self.window.blit(self.score_text, (125, 216))
        pygame.display.flip()
    def display_rule(self,window):
        self.rule = pygame.image.load(IMAGE_RULE_OF_THE_GAME).convert()
        self.window.blit(self.rule,(0,0))
        self.blue_button = pygame.image.load(IMAGE_BLUE_BUTTON).convert()
        self.window.blit(self.blue_button,(220,380))
        myfont = pygame.font.SysFont("comicsansms", 40)
        self.score_text = myfont.render("RETOUR", 1 ,(0, 0, 225))
        self.window.blit(self.score_text, (300, 300))
        pygame.display.flip()

    def return_game(self,window) :
        for event in pygame.event.get() :
            if event.type == KEYDOWN :
                if event.key == K_F1 :
                    self.init_game()
                    continue_game = True                                
                    game = True
                elif event.key == K_F2 :
                    exit()
                else :
                    continue

    def play(self):      
        self.init_game()
        self.initialisation() # intializes the pygame values
        continue_game = False
        
        while continue_game == False :
            regle = False
            self.display_home(self.window)
            for event in pygame.event.get() :
                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] < 330 and event.pos[1] < 370 and event.pos[0] > 110 and event.pos[1] > 300 :
                    continue_game = True
                elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] < 330 and event.pos[1] < 100 and event.pos[0] > 110 and event.pos[1] > 200 :
                    regle = True
                else :
                    continue
        while regle == True :
            self.display_rule(self.window)
            for event in pygame.event.get() :
                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] < 330 and event.pos[1] < 370 and event.pos[0] > 110 and event.pos[1] > 300 :
                    continue_game = False
                          
        while continue_game :
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
                            elif event.key == pygame.K_RIGHT :
                                self.character.move(self.map, 'right', self.window) # use the move function for moving
                                if self.character.verif_win(self.character.column,self.character.line + 1) == True :
                                    self.win()
                                    game = False
                                elif self.character.verif_loose(self.character.column,self.character.line + 1) == True :
                                    self.loose()
                                    game = False   
                                     
                            elif event.key == pygame.K_LEFT :
                                self.character.move(self.map, 'left', self.window)
                                if self.character.verif_win(self.character.column,self.character.line - 1) == True :
                                    self.win()
                                    game = False
                                elif self.character.verif_loose(self.character.column,self.character.line - 1) == True :
                                    self.loose()
                                    game = False                                                         
                                 
                            elif event.key == pygame.K_DOWN :
                                self.character.move(self.map, 'down', self.window)
                                if self.character.verif_win(self.character.column - 1,self.character.line) == True :
                                    self.win()
                                    game = False
                                elif self.character.verif_loose(self.character.column - 1,self.character.line) == True :
                                    self.loose()
                                    game = False                                                              
                                 
                            elif event.key == pygame.K_UP :
                                self.character.move(self.map, 'up', self.window)
                                if self.character.verif_win(self.character.column + 1,self.character.line) == True :
                                    self.win()
                                    game = False
                                elif self.character.verif_loose(self.character.column + 1,self.character.line) == True :
                                    self.loose()
                                    game = False                                                                 
                            else :
                                return AttributeError

                            self.map.display_map() # show the map for each move
                            self.map.show(self.window) # allows the display of each element
                            pygame.display.flip() # show all
                                                    
            while game == False :
                self.display_finish_home(self.window)
                for event in pygame.event.get() :
                    if event.type == KEYDOWN :
                        if event.key == K_F1 :
                            self.init_game()
                            continue_game = True                                
                            game = True
                        elif event.key == K_F2 :
                            exit()
                        else :
                            continue               