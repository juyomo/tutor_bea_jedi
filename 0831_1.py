def lb():
    print("")

def title(s):
    print("")
    div = "=========="
    print(div + s + div)

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

n = 19
height = n // 2   # 5
print("n, height: ")
print(n)
print(height)

# Leaf part of the tree
for i in range(n):
    spacePart = " " * (n-i-1)
    starPart = "*" * (2 * i + 1)
    print(spacePart + starPart)

######################
# Homework #1
# Print the tree trunk! Below is where we left off in class.


# Print the trunk part of the tree!
for i in range(height): # 0, 1, 2, 3, 4
    spacePart = " " * (n - height // 2)
    starPart = "*" * height
    print(spacePart + starPart)

## executing
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

