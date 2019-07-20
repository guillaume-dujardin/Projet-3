from random import *

class Map :
    
    def __init__(self) :
        self.map_array = []
        self.pos_ob = []

    def create_map(self,filename):
        try:
            with open(filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))   #Création du labyrinthe via fichier map.txt                    
                        
        except FileNotFoundError:
            print("Couldn't open map file \"" + filename + "\"")
            exit()    

           
    
    def display_map(self):
        i = 0
        for line in self.map_array:            
            for character in line:        #Affichage du labyrinthe
                print(character, end="")                
            print()
    
    



