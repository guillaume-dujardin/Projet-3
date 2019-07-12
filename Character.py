import os
from Map import Map

class Character():
    
    def __init__(self) :
        

        self.x = 1
        self.y = 1
        self.tresors = 0
        self.joueur = ""

    def victory(self,map):
        if map.map_array[self.y][self.x] == "O" and self.tresors == 3 :
            print("Gardien : Zzzz.. Zzzz.. Zzzz..  Je peut sortir du labyrinthe..")
        elif map.map_array[self.y][self.x] == "O" and self.tresors != 3 :
            print("Tu ne peut pas passer sans avoir tout les objets")
                
    def treasure(self):
        if map.map_array[self.y][self.x + 1] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Tout les objets sont en votre possession vite go chez le gardien pour le faire dodo")
        
    def check_treasure(self, map, x, y):
        if map.map_array[y][x] == "$" :
            self.tresors += 1
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            return True
        return False

    def move_r(self, map):
        map.map_array[self.y][self.x] = ' '
        self.x += 1
        map.map_array[self.y][self.x] = 'X'

    def move_l(self, map):
        map.map_array[self.y][self.x] = ' '
        self.x -= 1
        map.map_array[self.y][self.x] = 'X'

    def move_u(self, map):
        map.map_array[self.y][self.x] = ' '
        self.y -= 1
        map.map_array[self.y][self.x] = 'X'

    def move_d(self, map):
        map.map_array[self.y][self.x] = ' '
        self.y += 1
        map.map_array[self.y][self.x] = 'X'
        
            

    def move_right(self, map):
        if map.map_array[self.y][self.x + 1] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            self.move_r(map)
        elif map.map_array[self.y][self.x + 1] != '#':
            self.move_r(map)
        else :
            print("Aie ma tête.. Qui à eu l'idée de placé un mur ici..'")
        return map

    def move_left(self, map):
         self.victory(map)
         if map.map_array[self.y][self.x - 1] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            self.move_l(map)
         elif map.map_array[self.y][self.x - 1] != '#':
             self.move_l(map)
         else :
             print("Aie ma tête.. Qui à eu l'idée de placé un mur ici..'")
         return map

    def move_down(self, map):
        self.victory(map)
        if map.map_array[self.y + 1][self.x] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            self.move_d(map)
        elif map.map_array[self.y + 1][self.x] != '#':
            self.move_d(map)
        else :
            print("Aie ma tête.. Qui à eu l'idée de placé un mur ici..'")
        return map

    def move_up(self, map):
        self.victory(map)
        if map.map_array[self.y - 1][self.x] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            self.move_u(map)
        elif map.map_array[self.y - 1][self.x] != '#':
            self.move_u(map)
        else :
            print("Aie ma tête.. Qui à eu l'idée de placé un mur ici..'")
        return map





        