class Character():
    
    def __init__(self) :
        
        # Character positions

        self.x = 2
        self.y = 2

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

    def move_down(self, map):
       if map.map_array[self.y - 1][self.x] != '#':
           map.map_array[self.y][self.x] = ' '
           self.y -= 1
           map.map_array[self.y][self.x] = 'X'
       return map
        