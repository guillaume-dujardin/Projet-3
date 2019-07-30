from typing import List, Any
from Map import *
from Game import *
from Constant import *
import pygame
from pygame.locals import *
import os
import time

class Character():
        
    def __init__(self) :
        
        self.line = 1
        self.column = 1
        self.x = 1
        self.y = 1

    def initial(self, map) :
        self.position = pygame.image.load(IMAGE_ICONE).convert_alpha()
        self.direction = self.position
        self.map = map        

    def objects(self,pos_y,pos_x, window) :
        self.current_item_in_box = self.map.map_array[pos_y][pos_x]
        if self.current_item_in_box == 'e' or self.current_item_in_box == 's' or self.current_item_in_box == 'p' :
            print(self.current_item_in_box)
            self.map.score += 1
            self.map.remove_Item(self.column, self.line)
            if self.current_item_in_box == 'e' :
                myfont = pygame.font.SysFont("comicsansms", 40)
                self.score_text = myfont.render("ether object", 1, (0, 0, 255))
                window.blit(self.score_text, (80, 180))
                pygame.display.flip()
                time.sleep(1)
            elif self.current_item_in_box == 's' :
                myfont = pygame.font.SysFont("comicsansms", 40)
                self.score_text = myfont.render("needle object", 1, (0, 0, 255))
                window.blit(self.score_text, (80, 180))
                pygame.display.flip()
                time.sleep(1)
            elif self.current_item_in_box == 'p' :
                myfont = pygame.font.SysFont("comicsansms", 40)
                self.score_text = myfont.render("plastic_tube object", 1, (0, 0, 255))
                window.blit(self.score_text, (80, 180))
                pygame.display.flip()
                time.sleep(1)
    def verif_win(self,pos_y,pos_x) :
        if self.map.map_array[pos_y][pos_x] == 'O' and self.map.score == 3 :
            return True 

    def verif_loose(self,pos_y,pos_x):    
        if self.map.map_array[pos_y][pos_x] == 'O' and self.map.score < 3 :
            return True

    def tap_wall(self, window):
        myfont = pygame.font.SysFont("comicsansms", 40)
        self.score_text = myfont.render("Ouch! It hurts!", 1, (0, 0, 255))
        window.blit(self.score_text, (80, 180))
        pygame.display.flip()
        time.sleep(1)

    def move(self, map, direction, window) : # Displacement function

        self.initial(map)

        if direction == 'right' : # if the direction argument is 'right'
            if self.line < (number_of_square - 1) : # if line is less than the number of squares - 1
                self.objects(self.column,self.line + 1, window)               
                if self.map.map_array[self.column][self.line + 1] != '#' : # if the character's position in the maze is different from '#'
                    map.map_array[self.column][self.line] = ' ' # the space becomes empty
                    self.line += 1
                    map.map_array[self.column][self.line] = 'X' # the new location becomes the character
                    self.x = self.line * square_size          
                else :
                    self.tap_wall(window)
                self.direction = self.position

        if direction == 'left' : 
            if self.line > 0 : 
                self.objects(self.column,self.line - 1, window) 
                if self.map.map_array[self.column][self.line - 1] != '#' : 
                    map.map_array[self.column][self.line] = ' ' 
                    self.line -= 1 
                    map.map_array[self.column][self.line] = 'X' 
                    self.x = self.line * square_size                   
                else :
                    self.tap_wall(window)
            self.direction = self.position 

        if direction == 'up' :
            if self.column > 0 :
                self.objects(self.column - 1,self.line, window)
                if self.map.map_array[self.column - 1][self.line] != '#' :
                    map.map_array[self.column][self.line] = ' '
                    self.column -= 1
                    map.map_array[self.column][self.line] = 'X'
                    self.x = self.line * square_size
                else :
                    self.tap_wall(window)
            self.direction = self.position

        if direction == 'down' :
            if self.column < (number_of_square - 1) :
                self.objects(self.column + 1,self.line, window)
                if self.map.map_array[self.column + 1][self.line] != '#' :
                    map.map_array[self.column][self.line] = ' '
                    self.column += 1
                    map.map_array[self.column][self.line] = 'X'
                    self.x = self.line * square_size
                else :
                    self.tap_wall(window)
            self.direction = self.position

      
   
    