import random
from Constant import *
import pygame
from pygame.locals import *
from Character import * 

class Map :

    def __init__(self) :
        self.map_array = []
        self.score = 0
        self.score_text = ''

    def create_map(self,filename) :
        try :
            with open(filename, "r") as map_file :
                for line in map_file :
                    self.map_array.append(list(line.strip()))

        except FileNotFoundError :
            print("Couldn't open map file \"" + filename + "\"")
            exit()

    def show(self,window) :
        fond = pygame.image.load(IMAGE_FOND).convert()
        wall = pygame.image.load(IMAGE_WALL).convert()
        finish = pygame.image.load(IMAGE_GARDIEN).convert_alpha()
        ether = pygame.image.load(IMAGE_ETHER).convert()
        aiguille = pygame.image.load(IMAGE_AIGUILLE).convert()
        plastic = pygame.image.load(IMAGE_TUBE_PLASTIQUE).convert()
        icone = pygame.image.load(IMAGE_ICONE).convert()

        if (self.score <= 3) :
            myfont = pygame.font.SysFont("monospace", 22)
            self.score_text = myfont.render("My score : " + str(self.score), 1 , (23, 216, 216))

        num_line = 0
        for line in self.map_array :
            num_case = 0
            for sprite in line :
                x = num_case * taille_carre
                y = num_line * taille_carre
                if sprite == '#' :
                    window.blit(wall, (x,y))
                elif sprite == 'X' :
                    window.blit(icone, (x,y))
                elif sprite == 'O' :
                    window.blit(finish, (x,y))
                elif sprite == 'e' :
                    window.blit(ether, (x,y))
                elif sprite == 's' :
                    window.blit(aiguille, (x,y))
                elif sprite == 'p' :
                    window.blit(plastic, (x,y))
                elif sprite == ' ' :
                    window.blit(fond, (x,y))
                num_case += 1
            num_line += 1
        window.blit(self.score_text, (93, 5))

    def display_map(self) :
        i = 0
        for line in self.map_array :
            for column in line :
                print(column, end = "")
            print()

    def place_Items(self) :
        structure_items = ['e', 's', 'p']
        
        for item in structure_items :
            x = self.get_Random_Coordinates()
            y = self.get_Random_Coordinates()

            while (self.check_If_Valid(x, y) == False) :
                x = self.get_Random_Coordinates()
                y = self.get_Random_Coordinates()

            self.map_array[x][y] = item

    def check_If_Valid(self, x, y) :
        if (self.map_array[x][y]) == ' ' :
            return True
        else :
            return False

    def get_Random_Coordinates(self) :
        return random.randint(1, nombre_de_carre - 1)

    def remove_Item(self, x, y) :
        self.map_array[x][y] = ' '

    def to_Win(self, window) :
        myfont = pygame.font.SysFont("monospace", 22)
        self.score_text = myfont.render("Victory!!", 1, (0, 0, 255))
        window.blit(self.score_text, (93, 30))

    def to_Lose(self, window) :
        myfont = pygame.font.SysFont("monospace", 22)
        self.score_text = myfont.render("You are dead !", 1, (0, 0, 255))
        window.blit(self.score_text, (93, 30))