import random
import snake

class ThingyYouEat:

    def __init__(self, snake):
        self.x = random.randint(0, 24)
        self.y = random.randint(0, 24)

    def __str__(self):
        return(self.Xcoord, self.Ycoord)
