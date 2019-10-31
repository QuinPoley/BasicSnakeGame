import pyglet
from pyglet import clock
import ThingyYouEat

CurrentX = 50
CurrentY = 50

class Snake:
    def __init__(self):
        self.Direction = 1
# Makes a new food pellet when one is eaten
def newFoodPellet():
    global food
    global little_food
    food = ThingyYouEat.ThingyYouEat()
    food_image = pyglet.image.load('Red.png')
    fx = food.Xcoord
    fy = food.Ycoord
    little_food =  pyglet.sprite.Sprite(food_image, x=fx, y=fy)

food = None
little_food = None
newFoodPellet()
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
    try:
        little_food.draw()
    except:
        None

# Change direction that the snake is going
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

# This checks if the snake ate a pellet
def eating(dt):
    try:
        if((little_food.x >= ball.x and little_food.x <= ball.x + 20) or (little_food.x+6 >= ball.x and little_food.x+6 <= ball.x + 20)):
            if((little_food.y >= ball.y and little_food.y <= ball.y + 20) or (little_food.y+6 >= ball.y and little_food.y+6 <= ball.y + 20)):
                little_food.delete()
                newFoodPellet()
    except:
        None


clock.schedule_interval(update, 0.5)
clock.schedule_interval(eating, 0.5)
if __name__ == '__main__':
    pyglet.app.run()
