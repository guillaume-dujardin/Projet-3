import os
from Map import Map
from Constant import *

class Character():
    
    def __init__(self) :
        
        self.line = 1
        self.column = 1
        self.tresors = 0
        
    def victory(self,map,pos_column,pos_line):            
        if map.map_array[pos_column][pos_line] == "O" and self.tresors != 3 :
            return True

    def check_treasure(self, map,pos_column,pos_line):
        if map.map_array[pos_column][pos_line] == "$" :
            self.tresors += 1
            return True
        return False

    def move_r(self, map):
        map.map_array[self.column][self.line] = ' '
        self.line += 1
        map.map_array[self.column][self.line] = 'X'

    def move_l(self, map):
        map.map_array[self.column][self.line] = ' '
        self.line -= 1
        map.map_array[self.column][self.line] = 'X'

    def move_u(self, map):
        map.map_array[self.column][self.line] = ' '
        self.column -= 1
        map.map_array[self.column][self.line] = 'X'

    def move_d(self, map):
        map.map_array[self.column][self.line] = ' '
        self.column += 1
        map.map_array[self.column][self.line] = 'X'
     
    def move_right(self, map):  
        if self.check_treasure(map,self.column,self.line + 1) == True :
            self.move_r(map)
        elif self.victory(map,self.column,self.line +1) :
            pass
        elif map.map_array[self.column][self.line + 1] != '#':
            self.move_r(map)
        else :
            pass
        return map

    def move_left(self, map):
        if self.check_treasure(map,self.column,self.line - 1) == True :
            self.move_l(map)
        elif self.victory(map,self.column,self.line - 1) :
            pass
        elif map.map_array[self.column][self.line - 1] != '#':
            self.move_l(map)
        else :
            pass
        return map

    def move_down(self, map):
        if self.check_treasure(map,self.column + 1,self.line) == True :
            self.move_d(map)
        elif self.victory(map,self.column + 1,self.line) :
            pass
        elif map.map_array[self.column + 1][self.line] != '#':
            self.move_d(map)
        else :
            pass
        return map

    def move_up(self, map):
        if self.check_treasure(map,self.column - 1,self.line) == True :
            self.move_u(map)
        elif self.victory(map,self.column - 1,self.line) :
            pass
        elif map.map_array[self.column - 1][self.line] != '#':
            self.move_u(map)
        else :
            pass
        return map
