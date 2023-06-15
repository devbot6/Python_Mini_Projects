from random import randrange


class msdie:

    def __init__(self, s):
        self.sides = 5
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

