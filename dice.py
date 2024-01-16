import random

def roll_dice(nsides):
    #sides = int(input("number of sides: "))
    result= random.randint(1, nsides)
    return result

def askinput():
    sides= int(input("number of sides: "))
    value= roll_dice(sides)
    return value
 
roll_1= askinput()
roll_2= askinput()
print("roll_1: ",roll_1)
print("roll_2: ",roll_2)
print("total", roll_1 + roll_2)
