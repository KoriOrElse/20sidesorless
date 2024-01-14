import random

def askinput():
    value= (roll_dice(int(input("number of sides: "))))
    return value

def roll_dice(sides):
    #sides = int(input("number of sides: "))
    result= random.randint(1, sides)
    return result 
roll_1= askinput()
roll_2= askinput()
print("roll_1: ",roll_1)
print("roll_2: ",roll_2)
print("total", roll_1 + roll_2)

