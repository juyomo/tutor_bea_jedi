def lb():
    print("")

def title(s):
    print("")
    div = "=========="
    print(div + s + div)

######################
title("Pre #1")
print("a" * 3)

######################
title("Pre #2")
for i in range(4): # 0, 1, 2, 3
    print(i)

######################
title("Exercise 1")
# *
# **
# ***
print("Goal:")
print("*")
print("**")
print("***")
lb()

print("Actual:")

n = 4

for i in range(n):
    print("*" * (i + 1))

######################
title("Exercise 2")

print("Goal:")
print("***")
print("**")
print("*")
lb()

print("Actual:")
n = 6
for i in range(n):
    print("*" * (n-i))

######################
title("Exercise 3")
#     *
#    **
#   ***
#  ****
# *****

print("Goal:")
print("    *")
print("   **")
print("  ***")
print(" ****")
print("*****")
lb()

n = 5
for i in range(n): # 0, 1, 2, 3, 4
    print(" " * (n-i-1) + "*" * (i + 1))

######################
## Question # 4
title("Exercise 4")

print("    *")
print("   ***")
print("  *****")
print(" *******")
print("*********")

lb()

n = 20

for i in range(n):
    spacePart = " " * (n-i-1)
    starPart = "*" * (2 * i + 1)
    print(spacePart + starPart)

######################
# Homework #1
# Print the tree trunk! Below is where we left off in class.
height = n // 2

for i in range(height): # 0, 1, 2, 3, 4
    print("*" * height)

lb()

######################
# Homework #2
# Print the following shape
# *********
#  *******
#   *****
#    ***
#     *

######################
# Homework #3
# Print the following shape
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

######################
# Homework #4
# Print the following shape
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

######################
# Homework #5
# Print the following shape
# *       *
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *       *
