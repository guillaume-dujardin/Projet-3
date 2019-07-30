from typing import List, Any
import os
import Map
import pygame
from pygame.locals import *
from Game import *
from Constant import *

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

    def move(self, map, direction) : # Displacement function

        self.initial(map)

        if direction == 'right' : # if the direction argument is 'right'
            if self.line < (number_of_square - 1) : # if line is less than the number of squares -1
                if self.map.map_array[self.column][self.line + 1] != '#' : # if the character's position in the maze is different from '#'
                    map.map_array[self.column][self.line] = ' ' # the space becomes empty
                    self.line += 1
                    map.map_array[self.column][self.line] = 'X' # the new location becomes the character
                    self.x = self.line * square_size
            self.direction = self.position

        if direction == 'left' :
            if self.line > 0 :
                if self.map.map_array[self.column][self.line - 1] != '#' :
                    map.map_array[self.column][self.line] = ' '
                    self.line -= 1
                    map.map_array[self.column][self.line] = 'X'
                    self.x = self.line * square_size
            self.direction = self.position

        if direction == 'up' :
            if self.column > 0 :
                if self.map.map_array[self.column - 1][self.line] != '#' :
                    map.map_array[self.column][self.line] = ' '
                    self.column -= 1
                    map.map_array[self.column][self.line] = 'X'
                    self.x = self.line * square_size
            self.direction = self.position

        if direction == 'down' :
            if self.column < (number_of_square - 1) :
                if self.map.map_array[self.column + 1][self.line] != '#' :
                    map.map_array[self.column][self.line] = ' '
                    self.column += 1
                    map.map_array[self.column][self.line] = 'X'
                    self.x = self.line * square_size
            self.direction = self.position

        current_item_in_box = self.map.map_array[self.column][self.line]
        if current_item_in_box == 'e' or current_item_in_box == 's' or current_item_in_box == 'p' :
            self.map.score += 1
            self.map.remove_Item(self.column, self.line)
    
   
    