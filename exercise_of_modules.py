import random 


class Dice:
    def roll(self):         
        return random.randint(0,40),random.randint(0,20)
        

newroll=Dice()
print(newroll.roll())


 
    