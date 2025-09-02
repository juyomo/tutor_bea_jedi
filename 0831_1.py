def lb():
    print("")

def title(s):
    print("")
    div = " ========== "
    print(div + s + div)

######################
title("Review from last week")
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

print("Actual:")
n = 5
for i in range(n): # 0, 1, 2, 3, 4
    spacePart = " " * (n - i - 1)
    starPart = "*" * (i + 1)
    print(spacePart + starPart)

######################
title("Continued from last week - print a tree!")

n = 19
height = n // 2

# Leaf part of the tree
for i in range(n):
    spacePart = " " * (n-i-1)
    starPart = "*" * (2 * i + 1)
    print(spacePart + starPart)

# Print the trunk part of the tree!
for i in range(height): # 0, 1, 2, 3, 4
    spacePart = " " * (n - height // 2)
    starPart = "*" * height
    print(spacePart + starPart)

lb()


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

