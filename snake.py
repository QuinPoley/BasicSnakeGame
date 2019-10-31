import pyglet
from pyglet import clock
import ThingyYouEat

CurrentX = 50
CurrentY = 50

class Snake:
    def __init__(self):
        self.Direction = 1

food = ThingyYouEat.ThingyYouEat()
food_image = pyglet.image.load('Red.png')
fx = food.Xcoord
fy = food.Ycoord
little_food = pyglet.sprite.Sprite(food_image, x=fx, y=fy)

snakedir = Snake()
ball_image = pyglet.image.load('Blue.png')
ball = pyglet.sprite.Sprite(ball_image, x=CurrentX, y=CurrentY)
window = pyglet.window.Window(width=750, height=500, caption="Learning")
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)


@window.event
def on_draw():
    window.clear()      # Removing this line causes snake game but like not the good kind
    ball.draw()
    little_food.draw()

@window.event
def on_key_press(symbol, modifiers):
    x, y = ball.position
    if(symbol == pyglet.window.key.UP):
        snakedir.Direction = 1
    elif(symbol == pyglet.window.key.DOWN):
        snakedir.Direction = 3
    elif(symbol == pyglet.window.key.RIGHT):
        snakedir.Direction = 2
    elif(symbol == pyglet.window.key.LEFT):
        snakedir.Direction = 4

# This moves the snake
def update(dt):
    x, y = ball.position
    if(snakedir.Direction == 1):    # 1 is UP
        ball.y = y + 20
    elif(snakedir.Direction == 2):  # 2 is RIGHT
        ball.x = x + 20
    elif(snakedir.Direction == 3):  # 3 is DOWN
        ball.y = y - 20
    elif(snakedir.Direction == 4):  # 4 is LEFT
        ball.x = x - 20

clock.schedule_interval(update, 0.5)
if __name__ == '__main__':
    pyglet.app.run()
