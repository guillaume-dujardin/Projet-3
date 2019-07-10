import os

class Character():
    
    def __init__(self) :
        
        # Character positions

        self.x = 2
        self.y = 2

    def victory(self, map):
        if map.map_array[self.y][self.x + 1] == "O":
            input("Voulez vous sortir du labyrinthe ? : ")
            if "OUI" :
                os.system('cls')
                print("Vous sortez en vie du labyrinthe")
                continuer_game = False
            else :
                continuer_game = True

    def move_right(self, map):
        if map.map_array[self.y][self.x + 1] != '#':
            map.map_array[self.y][self.x] = ' '
            self.x += 1
            map.map_array[self.y][self.x] = 'X'
            print(self.x)
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
        