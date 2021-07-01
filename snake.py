
class Snake:
    def __init__(self):
        self.Direction = 1
        self.Length = 1
        self.HeadX = 50
        self.Heady = 50
        self.BodyParts = []

    def grow(self):
        self.Length += 1
        # Append a new snake body part onto list
    
    def move(self):
        if(self.Direction == 1):
            self.HeadX += 1
        
        for i in range(len(self.BodyParts)):
            print()
            # move them too
    
    def changeDirection(self):
        self.Direction = 2
