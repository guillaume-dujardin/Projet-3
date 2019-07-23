from random import sample

class Map :
    
    def __init__(self) :
        self.map_array = []
        self.lab = []        

    def create_map(self,filename):
        try:
            with open(filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))                
                        
        except FileNotFoundError:
            print("Couldn't open map file \"" + filename + "\"")
            exit()    
    

    def path_map_finder(self) :
        for y, line in enumerate(self.map_array) :
            for x, character in enumerate(line) :
                if character == " " :
                    self.lab.append((x,y))
    
    def pos_objet(self):
        i = 0
        self.path_map_finder()
        while i < 3 :
            pos = sample(self.lab,1)
            self.map_array[pos] = "$"
           
    
    def display_map(self):
        i = 0
        for line in self.map_array:            
            for character in line:
                print(character, end="")                
            print()

    



