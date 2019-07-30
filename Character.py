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
       
    def display_and_sleep(self,window) :
        window.blit(self.score_text, (80, 180)) 
        pygame.display.flip() 
        time.sleep(.600)
       
    def objects(self,pos_y,pos_x, window) : 
        self.current_item_in_box = self.map.map_array[pos_y][pos_x] 
        if self.current_item_in_box == 'e' or self.current_item_in_box == 's' or self.current_item_in_box == 'p' : 
            print(self.current_item_in_box) 
            self.map.score += 1 
            self.map.remove_Item(self.column, self.line) 
            if self.current_item_in_box == 'e' : 
                myfont = pygame.font.SysFont("comicsansms", 40) 
                self.score_text = myfont.render("ether object", 1, (0, 0, 255)) 
                self.display_and_sleep(window)

            elif self.current_item_in_box == 's' : 
                myfont = pygame.font.SysFont("comicsansms", 40) 
                self.score_text = myfont.render("needle object", 1, (0, 0, 255)) 
                self.display_and_sleep(window)

            elif self.current_item_in_box == 'p' : 
                myfont = pygame.font.SysFont("comicsansms", 40) 
                self.score_text = myfont.render("plastic_tube object", 1, (0, 0, 255)) 
                self.display_and_sleep(window)
            else :
                return AttributeError
       
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
        time.sleep(.500) 
       
    def move_r(self,map) :
        map.map_array[self.column][self.line] = ' ' 
        self.line += 1 
        map.map_array[self.column][self.line] = 'X' 
        self.x = self.line * square_size
       
    def move_l(self,map) :
        map.map_array[self.column][self.line] = ' ' 
        self.line -= 1 
        map.map_array[self.column][self.line] = 'X' 
        self.x = self.line * square_size
       
    def move_u(self,map) : 
        map.map_array[self.column][self.line] = ' ' 
        self.column -= 1 
        map.map_array[self.column][self.line] = 'X' 
        self.x = self.line * square_size
       
    def move_d(self,map) :
        map.map_array[self.column][self.line] = ' ' 
        self.column += 1 
        map.map_array[self.column][self.line] = 'X' 
        self.x = self.line * square_size 
       
    def move_tap_r(self,window,map) :
        if self.map.map_array[self.column][self.line + 1] != '#' : # if the character's position in the maze is different from '#'
            self.move_r(map) 
        else :
            self.tap_wall(window)
        self.direction = self.position
       
    def move_tap_l(self,window,map) :
        if self.map.map_array[self.column][self.line - 1] != '#' : 
            self.move_l(map)
        else :
            self.tap_wall(window)
        self.direction = self.position
       
    def move_tap_u(self,window,map) :
        if self.map.map_array[self.column - 1][self.line] != '#' :
            self.move_u(map)
        else :
            self.tap_wall(window)
        self.direction = self.position
       
    def move_tap_d(self,window,map) :
        if self.map.map_array[self.column + 1][self.line] != '#' :
            self.move_d(map)
        else :
            self.tap_wall(window)
        self.direction = self.position
       
    def move(self, map, direction, window) : # Displacement function

        self.initial(map)

        if direction == 'right' : # if the direction argument is 'right'
            if self.line < (number_of_square - 1) : # if line is less than the number of squares - 1
                self.objects(self.column,self.line + 1, window) 
                self.move_tap_r(window,map)

        elif direction == 'left' : 
            if self.line > 0 : 
                self.objects(self.column,self.line - 1, window) 
                self.move_tap_l(window,map)

        elif direction == 'up' :
            if self.column > 0 :
                self.objects(self.column - 1,self.line, window)
                self.move_tap_u(window,map)

        elif direction == 'down' :
            if self.column < (number_of_square - 1) :
                self.objects(self.column + 1,self.line, window)
                self.move_tap_d(window,map)
        else :
            return AttributeError