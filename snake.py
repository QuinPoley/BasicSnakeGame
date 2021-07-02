
from pygame.constants import BLENDMODE_ADD


class Snake:
    def __init__(self):
        self.Direction = 2
        self.Length = 0
        self.HeadX = 0
        self.Heady = 0 # A grid, 25 by 25 where the blocks are 32 pix
        self.BodyParts = []
        self.ListofDirectionChanges = []

    def grow(self):
        if(self.Length == 0): # The first added
            if(self.Direction == 1): # Up
                self.BodyParts.append(SnakeBodyParts(self.HeadX, self.Heady+1, self.Direction))
            if(self.Direction == 2): # Right
                self.BodyParts.append(SnakeBodyParts(self.HeadX-1, self.Heady, self.Direction))
            if(self.Direction == 3): # Down
                self.BodyParts.append(SnakeBodyParts(self.HeadX, self.Heady-1, self.Direction))
            if(self.Direction == 4): # Left
                self.BodyParts.append(SnakeBodyParts(self.HeadX+1, self.Heady, self.Direction))
        else:
            if(self.BodyParts[self.Length-1].Direction == 1): # Up
                self.BodyParts.append(SnakeBodyParts(self.BodyParts[self.Length-1].x, self.BodyParts[self.Length-1].y+1, self.Direction))
            if(self.BodyParts[self.Length-1].Direction == 2): # Right
                self.BodyParts.append(SnakeBodyParts(self.BodyParts[self.Length-1].x-1, self.BodyParts[self.Length-1].y, self.Direction))
            if(self.BodyParts[self.Length-1].Direction == 3): # Down
                self.BodyParts.append(SnakeBodyParts(self.BodyParts[self.Length-1].x, self.BodyParts[self.Length-1].y-1, self.Direction))
            if(self.BodyParts[self.Length-1].Direction == 4): # Left
                self.BodyParts.append(SnakeBodyParts(self.BodyParts[self.Length-1].x+1, self.BodyParts[self.Length-1].y, self.Direction))
        self.Length += 1
        # Append a new snake body part onto list
    
    def move(self):
        if(self.Direction == 1): # Up
            self.Heady -= 1
        if(self.Direction == 2): # Right
            self.HeadX += 1
        if(self.Direction == 3): # Down
            self.Heady += 1
        if(self.Direction == 4): # Left
            self.HeadX -= 1

        listindiciespop = []
        for i in range(len(self.BodyParts)):
            for j in range(len(self.ListofDirectionChanges)):
                if(self.BodyParts[i].x == self.ListofDirectionChanges[j][0] and self.BodyParts[i].y == self.ListofDirectionChanges[j][1]):
                    self.BodyParts[i].Direction = self.ListofDirectionChanges[j][2]
                    if((i+1) == len(self.BodyParts)): # Last piece of snake to turn there
                        listindiciespop.append(j)
            if(self.BodyParts[i].Direction == 1):
                self.BodyParts[i].y -= 1
            if(self.BodyParts[i].Direction == 2):
                self.BodyParts[i].x += 1
            if(self.BodyParts[i].Direction == 3):
                self.BodyParts[i].y += 1
            if(self.BodyParts[i].Direction == 4):
                self.BodyParts[i].x -= 1
        
        for x in range(len(listindiciespop)):
            self.ListofDirectionChanges.pop(listindiciespop[x])
            # move them too
    
    def Death(self):
        if(self.HeadX > 24 or self.HeadX < 0 or self.Heady > 24 or self.Heady < 0): # Into wall
            return True
        for j in range(len(self.BodyParts)):
            if(self.HeadX == self.BodyParts[j].x and self.Heady == self.BodyParts[j].y): # Into body
                return True
        return False
        
class SnakeBodyParts:
    def __init__(self, x, y, dir):
        self.x = x 
        self.y = y
        self.Direction = dir
