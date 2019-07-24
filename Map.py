from random import sample

class Map :
    
    def __init__(self) :
        self.map_array = []
        self.wall = []
        self.lab = []
        self.position_Mc = (1,1)
        self.position_gardien = (1,1)
        self.objects_position = []

    def create_map(self,filename):
        try:
            with open(filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))                
                        
        except FileNotFoundError:
            print("Couldn't open map file \"" + filename + "\"")
            exit()    

    def espace_vide(self) :
        for y, line in enumerate(self.map_array) :
            for x, column in enumerate(line) :                    
                if column == " " :
                    self.lab.append((x,y))
                    print(self.lab(x,y))

    def objects_positions(self):
        object_position = sample(self.lab,3)

    def display_map(self):
        i = 0
        for line in range(15):
            for column in range(15):
                if (line, column) in self.position_Mc :
                    print("X")
                elif (line, column) in self.position_gardien :
                    print("O")
                elif (line, column) in self.objects_positions() :
                    print("$")
                elif (line, column) in self.espace_vide :
                    print(" ")
                else:
                    print("#")