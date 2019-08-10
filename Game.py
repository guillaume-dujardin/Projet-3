from Map import *
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
        self.map.create_map("ressources/map.txt") # Function that links a variable to a class

    def initialisation(self) :
        pygame.init()
        self.window = pygame.display.set_mode((side_window,side_window))
        self.background = pygame.image.load(IMAGE_BACKGROUND).convert()
        self.window.blit(self.background,(0,0)) # poster the background
        self.map.show(self.window) # allows the display of all the elements
        pygame.display.flip() # Initialize pygame and create the first window of the game
        
    def win(self) :
        self.map.to_Win(self.window)
        pygame.display.flip()
        time.sleep(2) # Shows the victory of the game

    def loose(self) :
        self.map.to_Lose(self.window)
        pygame.display.flip()
        time.sleep(2) # Shows the defeat of the game

    def display_finish_home(self,window) :
        self.home = pygame.image.load(IMAGE_HOME).convert()
        self.window.blit(self.home,(0,0))
        myfont = pygame.font.SysFont("comicsansms", 40)
        self.score_text = myfont.render(" Start again ? ", 1, (0, 0, 255))
        self.window.blit(self.score_text, (100, 80))
        self.score_text = myfont.render("F1 for yes F2 for no", 1 ,(0, 0, 225))
        self.window.blit(self.score_text, (35, 130))
        pygame.display.flip() # Display the end menu of the game

    def display_home(self,window) :
        self.first_home = pygame.image.load(IMAGE_FIRST_HOME).convert()
        self.window.blit(self.first_home,(0,0))
        self.play_button = pygame.image.load(IMAGE_RULES_BUTTON).convert()
        self.window.blit(self.play_button,(110,300))
        self.blue_button = pygame.image.load(IMAGE_RULES_BUTTON).convert()
        self.window.blit(self.blue_button,(110,200))
        self.exit_button = pygame.image.load(IMAGE_EXIT_BUTTON).convert()
        self.window.blit(self.exit_button,(0,410))
        myfont = pygame.font.SysFont("monospace",22)
        self.score_text = myfont.render("EXIT", 1 ,(255, 255, 255))
        self.window.blit(self.score_text, (20, 420))
        myfont = pygame.font.SysFont("monospace", 27)
        self.score_text = myfont.render("GAME RULES", 1 ,(255, 255, 255))
        self.window.blit(self.score_text, (140, 216))
        self.score_text = myfont.render("PLAY", 1 ,(255, 255, 255))
        self.window.blit(self.score_text, (187, 318))
        pygame.display.flip() # Show party start greeting

    def display_rule(self,window):
        self.rule = pygame.image.load(IMAGE_RULE_OF_THE_GAME).convert()
        self.window.blit(self.rule,(0,0))
        self.blue_button = pygame.image.load(IMAGE_RETURN_BUTTON).convert()
        self.window.blit(self.blue_button,(320,420))
        myfont = pygame.font.SysFont("monospace", 23)
        self.score_text = myfont.render("MAIN MENU", 1 ,(255, 255, 255))
        self.window.blit(self.score_text, (325, 422))
        pygame.display.flip() # Show the rules of the game
    
    def display_move(self) :
        self.map.display_map() # show the map for each move
        self.map.show(self.window) # allows the display of each element
        pygame.display.flip() # Show all

    def display_finish_move(self) :
        self.map.map_array[self.character.column][self.character.line + 1] = ' '
        self.map.map_array[self.character.column][self.character.line] = ' '
        self.map.map_array[self.character.column][self.character.line + 1] = 'X' # Makes the end of game display in case of victory

    def move_display_right(self) :
        self.character.move(self.map, 'right', self.window) # use the move function for moving
        self.display_move() #  Does the action of the right move

    def move_display_left(self) :
        self.character.move(self.map, 'left', self.window) # use the move function for moving
        self.display_move() # Does the action of the left move

    def move_display_down(self) :
        self.character.move(self.map, 'down', self.window) # use the move function for moving
        self.display_move() # Does the action of the down move

    def move_display_up(self) :
        self.character.move(self.map, 'up', self.window) # use the move function for moving
        self.display_move() # Does the action of the up move

    def display_right(self) :
        self.display_finish_move()
        self.display_move()
        self.win() # Displays the end move when the guard is asleep and the victory

    def place_init_display(self) :
        self.map.place_Items() # place the objects in the labyrinth
        self.initialisation() # intializes the pygame values
        self.map.display_map() # Show the map in console

    def game(self) :
        continue_game = False
        regle = False
        while continue_game == False :
            self.display_home(self.window)
            for event in pygame.event.get() :
                if event.type == QUIT :
                        exit()
                if event.type == KEYDOWN :

                    if event.key == K_ESCAPE :
                        exit()
                elif event.type == MOUSEBUTTONUP :
                    if event.button == 1 and event.pos[0] < 340 and event.pos[1] < 370 and event.pos[0] > 110 and event.pos[1] > 300 :
                        continue_game = True
                    elif event.button == 1 and event.pos[0] < 340 and event.pos[1] < 265 and event.pos[0] > 110 and event.pos[1] > 200 :
                        regle = True
                    elif event.button == 1 and event.pos[0] < 95 and event.pos[1] < 450 and event.pos[0] > 0 and event.pos[1] > 410 :
                        exit()
                    else :
                        continue

            while regle :
                self.display_rule(self.window)
                for event in pygame.event.get() :
                    if event.type == QUIT :
                        exit()
                    if event.type == KEYDOWN :

                        if event.key == K_ESCAPE :
                            exit()
                    if event.type == MOUSEBUTTONUP :
                        if event.button == 1 and event.pos[0] < 450 and event.pos[1] < 450 and event.pos[0] > 320 and event.pos[1] > 420 :
                            regle = False                            
                        else :
                            continue
                          
        while continue_game :
            self.place_init_display()
            game = True
            while game == True :

                for event in pygame.event.get() : # for each pygame event
                    if event.type == QUIT :
                        exit()
                    if event.type == KEYDOWN :
                        if event.key == K_ESCAPE :
                            exit()
                        elif event.key == pygame.K_RIGHT :
                            self.move_display_right()
                            if self.character.verif_win(self.character.column,self.character.line + 1) == True :
                                self.display_right()
                                game = False
                            elif self.character.verif_loose(self.character.column,self.character.line + 1) == True :
                                self.loose()
                                game = False
                            else :
                                continue
                                  
                        elif event.key == pygame.K_LEFT :
                            self.move_display_left()
                            if self.character.verif_win(self.character.column,self.character.line - 1) == True :
                                self.win()
                                game = False
                            elif self.character.verif_loose(self.character.column,self.character.line - 1) == True :
                                self.loose()
                                game = False
                            else :
                                continue
                                 
                        elif event.key == pygame.K_DOWN :
                            self.move_display_down()
                            if self.character.verif_win(self.character.column - 1,self.character.line) == True :
                                self.win()
                                game = False
                            elif self.character.verif_loose(self.character.column - 1,self.character.line) == True :
                                self.loose()
                                game = False
                            else :
                                continue
                                 
                        elif event.key == pygame.K_UP :
                            self.move_display_up()
                            if self.character.verif_win(self.character.column + 1,self.character.line) == True :
                                self.win()
                                game = False
                            elif self.character.verif_loose(self.character.column + 1,self.character.line) == True :
                                self.loose()
                                game = False                                                                 
                            else :
                                continue
                               
                                                    
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
                            continue # Displays the complete part compose function

    def play(self):      
        self.init_game()
        self.initialisation() # intializes the pygame values
        self.game() # Function that initializes the game and launches