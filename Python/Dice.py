import random as r

class Dice:
    def roll(self):
        return r.randint(1,6),r.randint(1,6)


d1=Dice()
print(d1.roll())
print(d1.roll())