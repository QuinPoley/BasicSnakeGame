import pyglet
from pyglet import clock
import ThingyYouEat
import Snake

CurrentX = 50
CurrentY = 50

# Makes a new food pellet when one is eaten
def newFoodPellet():
    global food
    global little_food
    food = ThingyYouEat.ThingyYouEat()
    fx = food.Xcoord
    fy = food.Ycoord
    little_food =  pyglet.sprite.Sprite(food_image, x=fx, y=fy)

food = None
little_food = None
food_image = pyglet.image.load('Red.png')
snake_image = pyglet.image.load('Blue.png')
newFoodPellet()
player = Snake.Snake(snake_image, Xs=CurrentX, Ys=CurrentY, dir=1)
window = pyglet.window.Window(width=750, height=500, caption="Learning")
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

@window.event
def on_draw():
    window.clear()      # Removing this line causes snake game but like not the good kind
    player.draw()
    little_food.draw()
    for Sprite in player.snakeArray:
        Sprite.draw()

# Change direction that the snake is going
@window.event
def on_key_press(symbol, modifiers):
    player.input(symbol)

def recurse(snake):
    x, y = snake.position
    if(snake.Direction == 1):    # 1 is UP
        snake.y = y + 20
    elif(snake.Direction == 2):  # 2 is RIGHT
        snake.x = x + 20
    elif(snake.Direction == 3):  # 3 is DOWN
        snake.y = y - 20
    elif(snake.Direction == 4):  # 4 is LEFT
        snake.x = x - 20

# This moves the snake
def update(dt):
    x, y = player.position
    if(player.Direction == 1):    # 1 is UP
        player.y = y + 20
    elif(player.Direction == 2):  # 2 is RIGHT
        player.x = x + 20
    elif(player.Direction == 3):  # 3 is DOWN
        player.y = y - 20
    elif(player.Direction == 4):  # 4 is LEFT
        player.x = x - 20

        #recursive call to move rest of snake
    i = 0
    for Snake in player.snakeArray:
        recurse(player.snakeArray[i])
        i += 1


# This checks if the snake ate a pellet
def eating(dt):
    if((little_food.x >= player.x and little_food.x <= player.x + 20) or (little_food.x+6 >= player.x and little_food.x+6 <= player.x + 20)):
        if((little_food.y >= player.y and little_food.y <= player.y + 20) or (little_food.y+6 >= player.y and little_food.y+6 <= player.y + 20)):
            little_food.delete()
            player.grow()
            newFoodPellet()


clock.schedule_interval(update, 0.4)
clock.schedule_interval(eating, 0.4)
if __name__ == '__main__':
    pyglet.app.run()
