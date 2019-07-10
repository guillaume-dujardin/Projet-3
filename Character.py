import os
from Map import Map

class Character():
    
    def __init__(self) :
        

        self.x = 2
        self.y = 2
        self.tresors = 0

    def victory(self, map):  # Non concluant \ à modifier
        if map.map_array[self.y][self.x + 1] == "O":
            input("Gardien : Vous avez eu de la chance... Souhaitez vous sortir de cet enfer ou bien.. vous reperdre dans le labyrinthe...  (oui pour quitter,non pour rester) : ")
            if "OUI" :
                os.system('cls')
                print("Vous sortez en vie du labyrinthe")
                continuer_game = False
                exit()
            elif "NON" :
                continuer_game = True
    
    def check_treasure(self, pos_x, pos_y):
        if map.map_array[pos_y][pos_x] == "$" :
            self.tresors += 1
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            return True
        return False

    def move_right(self, map):
        if map.map_array[self.y][self.x + 1] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            map.map_array[self.y][self.x] = ' '
            self.x += 1
            map.map_array[self.y][self.x] = 'X'
        elif map.map_array[self.y][self.x + 1] != '#':
            map.map_array[self.y][self.x] = ' '
            self.x += 1
            map.map_array[self.y][self.x] = 'X'            
        return map

    def move_left(self, map):
         if map.map_array[self.y][self.x - 1] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            map.map_array[self.y][self.x] = ' '
            self.x -= 1
            map.map_array[self.y][self.x] = 'X'

         elif map.map_array[self.y][self.x - 1] != '#':
             map.map_array[self.y][self.x] = ' '
             self.x -= 1
             map.map_array[self.y][self.x] = 'X'
         return map

    def move_down(self, map):
        if map.map_array[self.y + 1][self.x] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            map.map_array[self.y][self.x] = ' '
            self.y += 1
            map.map_array[self.y][self.x] = 'X'
        elif map.map_array[self.y + 1][self.x] != '#':
            map.map_array[self.y][self.x] = ' '
            self.y += 1
            map.map_array[self.y][self.x] = 'X'
        return map

    def move_up(self, map):
        if map.map_array[self.y - 1][self.x] == "$" :
            self.tresors += 1     
            print("Vous avez dégoter un tresor ! Cela vous en fait ",self.tresors," bravo !")
            if self.tresors == 3 :
                print("Vous avez tout les tresors allez vite trouver le gardien pour l'endormir !!")
            map.map_array[self.y][self.x] = ' '
            self.y -= 1
            map.map_array[self.y][self.x] = 'X'
        elif map.map_array[self.y - 1][self.x] != '#':
            map.map_array[self.y][self.x] = ' '
            self.y -= 1
            map.map_array[self.y][self.x] = 'X'
        return map



        