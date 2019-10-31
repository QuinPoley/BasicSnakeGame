import random

class ThingyYouEat:

    def __init__(self):
        self.Xcoord = random.randint(1, 50) * 10
        self.Ycoord = random.randint(1, 50) * 10

    def getX(self):
        return self.Xcoords

    def getY(self):
        return self.Ycoord

    def __str__(self):
        return(self.Xcoord, self.Ycoord)
