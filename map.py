from random import *

class Map :
    #Labyrinthe niveau 1 (plan du labyrinthe)
    def __init__(self) :
        self.map_array = []

    # Create map with the fiven filename
    # The created map is stored in map_arrau object variable

    def create_map(self,filename):
        try:
            with open(filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))
        except FileNotFoundError:
            print("Couldn't open map file \"" + filename + "\"")
            exit()

# Display map stored in Map class

    def display_map(self):
        for line in self.map_array:
            for character in line:
                print(character, end="")
            print()

    



