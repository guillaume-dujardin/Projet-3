import os
from Map import Map

class Character():
    
    def __init__(self) :
        
        # Character positions

        self.x = 2
        self.y = 2
        tresors = 0

    def victory(self, map):
        if map.map_array[self.y][self.x + 1] == "O":
            input("Gardien : Vous avez eu de la chance... Souhaitez vous sortir de cet enfer ou bien.. vous reperdre dans le labyrinthe...  (oui pour quitter,non pour rester) : ")
            if "OUI" :
                os.system('cls')
                print("Vous sortez en vie du labyrinthe")
                continuer_game = False
                exit()
            elif "NON" :
                continuer_game = True

    def move_right(self, map):
        if map.map_array[self.y][self.x + 1] == "$" :
            tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",tresors," bravo !")
            map.map_array[self.y][self.x] = ' '
            self.x += 1
            map.map_array[self.y][self.x] = 'X'
                 
        elif map.map_array[self.y][self.x + 1] != '#':
            map.map_array[self.y][self.x] = ' '
            self.x += 1
            map.map_array[self.y][self.x] = 'X'            
        return map

    def move_left(self, map):
        if map.map_array[self.y][self.x - 1] != '#':
            map.map_array[self.y][self.x] = ' '
            self.x -= 1
            map.map_array[self.y][self.x] = 'X'
        return map

    def move_down(self, map):        
        if map.map_array[self.y + 1][self.x] != '#':
            map.map_array[self.y][self.x] = ' '
            self.y += 1
            map.map_array[self.y][self.x] = 'X'
        return map

    def move_up(self, map):
       if map.map_array[self.y - 1][self.x] != '#':
           map.map_array[self.y][self.x] = ' '
           self.y -= 1
           map.map_array[self.y][self.x] = 'X'
       return map
        