# Sep 7
# Functions! :)

def doubleTheNumber(n):
    return n * 2

def findLength(s):
    return len(s)

x = doubleTheNumber(5)
y = findLength("Hello")

print(x)
print(y)

def add(a, b):
    return a + b

z = add(10.5, 5/2)
print(z)

######
def lb():
    print("--------")
def title(str):
    print("======== " + str + " ========")
 
######
title("Divisible by 3 Exercise")

def isDivisibleBy3(n):
    print(n)
    return n % 3 == 0

for i in range(5):
    print(isDivisibleBy3(i))
    lb()

######
title("isEven")

def isEven(n):
    # returns true if n is even, false otherwise
    print(n)
    return n % 2 == 0

print(isEven(2))
print(isEven(3))

######
######################
title("Stars!!!")

def printStars(n):
    for i in range(n):
        spacePart = " " * (n - i - 1)
        starPart = "*" * (i + 1)
        print(spacePart + starPart)

printStars(5)
lb()
printStars(10)
lb()
printStars(100)

#####
title("End of Program")

print(type(123) == int)