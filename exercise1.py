import random
#Ask the user for two integers. 
x = input("x: ")
y = input("y: ")
#Write a Python program to generate a randomnumber between two of these integers (inclusive). 
number = random.randint(int(x), int(y))
print(number)
#Use random.randint()