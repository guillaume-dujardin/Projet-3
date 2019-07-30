import random
from Constant import *
import pygame
from pygame.locals import *
from Character import * 

class Map :

    def __init__(self) :
        self.map_array = [] # the labyrinth
        self.score = 0
        self.score_text = ''

    def create_map(self,filename) : # function to create the map
        try :
            with open(filename, "r") as map_file :
                for line in map_file :
                    self.map_array.append(list(line.strip()))

        except FileNotFoundError : # if there is a file error
            print("Couldn't open map file \"" + filename + "\"")
            exit()

    def show(self,window) : # function that sets each photo to a variable
        background = pygame.image.load(IMAGE_BACKGROUND).convert()
        wall = pygame.image.load(IMAGE_WALL).convert()
        finish = pygame.image.load(IMAGE_GUARDIAN).convert_alpha()
        ether = pygame.image.load(IMAGE_ETHER).convert()
        needle = pygame.image.load(IMAGE_NEEDLE).convert()
        plastic = pygame.image.load(IMAGE_PLASTIC_TUBE).convert()
        icone = pygame.image.load(IMAGE_ICONE).convert()

        if (self.score <= 3) : # if the score is less than or equal to 3
            myfont = pygame.font.SysFont("monospace", 22) # myfont will be equal to a minivan writing font
            self.score_text = myfont.render("My score : " + str(self.score), 1 , (23, 216, 216)) # for the score

        num_line = 0
        for line in self.map_array : # for each line in map_array
            num_case = 0
            for sprite in line : # for each square in the lines
                x = num_case * square_size
                y = num_line * square_size
                if sprite == '#' : # We define each square of a photo
                    window.blit(wall, (x,y))
                elif sprite == 'X' :
                    window.blit(icone, (x,y))
                elif sprite == 'O' :
                    window.blit(finish, (x,y))
                elif sprite == 'e' :
                    window.blit(ether, (x,y))
                elif sprite == 's' :
                    window.blit(needle, (x,y))
                elif sprite == 'p' :
                    window.blit(plastic, (x,y))
                elif sprite == ' ' :
                    window.blit(background, (x,y))
                num_case += 1
            num_line += 1
        window.blit(self.score_text, (93, 5)) # we display the score

    def display_map(self) : # display function of the console board for testing
        i = 0
        for line in self.map_array :
            for column in line :
                print(column, end = "")
            print()

    def place_Items(self) : # function that defines the objects in our labyrinth
        structure_items = ['e', 's', 'p']
        
        for item in structure_items : # for each two variable object are assign random number
            x = self.get_Random_Coordinates()
            y = self.get_Random_Coordinates()

            while (self.check_If_Valid(x, y) == False) : # as long as the position is valid
                x = self.get_Random_Coordinates()
                y = self.get_Random_Coordinates()

            self.map_array[x][y] = item

    def check_If_Valid(self, x, y) : # function to test if the position is empty
        if (self.map_array[x][y]) == ' ' :
            return True
        else :
            return False

    def get_Random_Coordinates(self) : # function that recovers a random number
        return random.randint(1, number_of_square - 1)

    def remove_Item(self, x, y) : # function that puts back the background of the decor instead of the photos
        self.map_array[x][y] = ' '

    def to_Win(self, window) : # function that displays the score and "win"
        myfont = pygame.font.SysFont("comicsansms", 40)
        self.score_text = myfont.render("Victory!!", 1, (0, 0, 255))
        window.blit(self.score_text, (130, 180))
        

    def to_Lose(self, window) : # function that displays the score and "you are dead"
        myfont = pygame.font.SysFont("comicsansms", 40)
        self.score_text = myfont.render("You are dead !", 1, (0, 0, 255))
        window.blit(self.score_text, (110, 180))
        