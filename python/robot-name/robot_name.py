import random

class Robot(object):
    def __init__(self, firstLength=2, lastLength=3):
        random.seed()
        self.firstName = "".join([chr(random.randint(ord('A'), ord('Z'))) for _ in range(firstLength)])
        self.lastName = "".join([str(random.randint(0, 9)) for _ in range(lastLength)])
        self.name = self.firstName + self.lastName
    
    def reset(self, firstLength=2, lastLength=3):
        self.__init__(firstLength, lastLength)
