import random

sides= int(input("number of sides:" ))
d_num= int(input("number of dice:" ))
print (d_num, "d", sides)

total=0
x=1
for i in range (d_num):
    rolling= random.randint(1, sides)
    total= (total+ rolling)
    print ("result",x, ":", rolling)
    x=(x+1)

print("total:", total)
