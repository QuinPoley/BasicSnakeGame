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
        if(symbol == pyglet.window.key.UP):
            self.Direction = 1
        elif(symbol == pyglet.window.key.DOWN):
            self.Direction = 3
        elif(symbol == pyglet.window.key.RIGHT):
            self.Direction = 2
        elif(symbol == pyglet.window.key.LEFT):
            self.Direction = 4

        for Snake in self.snakeArray:
            Snake.input(symbol)

    def update(self, dt):
        if(self.Direction == 1):    # 1 is UP
            self.y += 20
        elif(self.Direction == 2):  # 2 is RIGHT
            self.x += 20
        elif(self.Direction == 3):  # 3 is DOWN
            self.y -= 20
        elif(self.Direction == 4):  # 4 is LEFT
            self.x -= 20

        i = 0
        for Snake in self.snakeArray:
            self.recurse(self.snakeArray[i])
            i += 1


    def recurse(self, snake):
        x, y = snake.position
        if(snake.Direction == 1):    # 1 is UP
            snake.y = y + 20
        elif(snake.Direction == 2):  # 2 is RIGHT
            snake.x = x + 20
        elif(snake.Direction == 3):  # 3 is DOWN
            snake.y = y - 20
        elif(snake.Direction == 4):  # 4 is LEFT
            snake.x = x - 20
