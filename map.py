from random import *

class Map :

    def __init__(self) :
        self.map_array = []

    def create_map(self,filename):
        try:
            with open(filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))   #Création du labyrinthe via fichier map.txt
        except FileNotFoundError:
            print("Couldn't open map file \"" + filename + "\"")
            exit()


    def display_map(self):
        for line in self.map_array:            
            for character in line:        #Affichage du labyrinthe
                print(character, end="")
            print()

    def is_passage(self, x, y):
        if map.map_array[y][x] == " " :
            print("cet acces est libre")
            return bool

    def is_wall(self,x, y):
        if map.map_array[y][x] == "#" :
            print("C'est un mur")
            return bool

    def is_treasure(self,x, y):
        if map.map_array[y][x] == "$":
            print("C'est un tresors")
            return bool
    
    def is_gardian(self,x, y):
        if map.map_array[y][x] == "O" :
            print("C'est un gardien")
            return bool
    
    



