import pyglet
import time

class Snake(pyglet.sprite.Sprite):
    def __init__(self, image, Xs, Ys, dir, len=0):
        super().__init__(image, x=Xs, y=Ys)
        self.image = image
        self.Direction = dir
        self.length = len
        self.snakeArray = []

    def grow(self):
        print(self.length)
        print(self.snakeArray)
        if(self.length == 0):
            if(self.Direction == 1):
                self.snakeArray.append(Snake(self.image, self.x, self.y-40, self.Direction))
            elif(self.Direction == 2):
                self.snakeArray.append(Snake(self.image, self.x-40, self.y, self.Direction))
            elif(self.Direction == 3):
                self.snakeArray.append(Snake(self.image, self.x, self.y+40, self.Direction))
            elif(self.Direction == 4):
                self.snakeArray.append(Snake(self.image, self.x+40, self.y, self.Direction))
        elif(self.length > 0):
            if(self.snakeArray[self.length-1].Direction == 1):
                self.snakeArray.append(Snake(self.image, self.snakeArray[self.length-1].x, self.snakeArray[self.length-1].y-40, self.snakeArray[self.length-1].Direction))
            elif(self.snakeArray[self.length-1].Direction == 2):
                self.snakeArray.append(Snake(self.image, self.snakeArray[self.length-1].x-40, self.snakeArray[self.length-1].y, self.snakeArray[self.length-1].Direction))
            elif(self.snakeArray[self.length-1].Direction == 3):
                self.snakeArray.append(Snake(self.image, self.snakeArray[self.length-1].x, self.snakeArray[self.length-1].y+40, self.snakeArray[self.length-1].Direction))
            elif(self.snakeArray[self.length-1].Direction == 4):
                self.snakeArray.append(Snake(self.image, self.snakeArray[self.length-1].x+40, self.snakeArray[self.length-1].y, self.snakeArray[self.length-1].Direction))
        self.length += 1






    def input(self, symbol):
        x, y = self.position
        if(symbol == pyglet.window.key.UP):
            self.Direction = 1
        elif(symbol == pyglet.window.key.DOWN):
            self.Direction = 3
        elif(symbol == pyglet.window.key.RIGHT):
            self.Direction = 2
        elif(symbol == pyglet.window.key.LEFT):
            self.Direction = 4

        for segment in self.snakeArray:
            segment.input(symbol)
