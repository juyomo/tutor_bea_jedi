# for loops
div = "----------"
print(div)

for x in range(3):
  print(x)

print(div)

for x in range(3):
  print(x - 1)

print(div)

for x in range(2, 6):
  print(x)

print(div)

for x in "bananas":
  print(x)

print(div)

for x in "bananas":
  if (x == "a"):
    print(x)

print(div)

# how to declare lists
fruits = ["apples", "bananas", "oranges"]
students = ["Abby", "Bob", "Chris", "Dave"]
list1 = ["element"] * 5
# you can check by doing print(fruits)

# find length of list
print(len(fruits))

print(div)

# access elements in the list
print(fruits[0])
print(fruits[2])
print(fruits[-2])

print(div)

# modifying lists
students.pop()
print(students)
students.append("Dave")
print(students)

print(div)

# Iterating through a list (for loops AND lists!)

for x in fruits:
  print(x)

print(div)

for idx in range(3):
  print(fruits[idx])

print(div)

for i in range(3):
  print("I like " + fruits[i])

print(div)


for x in students:
  for y in fruits:
    print(x + " likes " + y)

print(div)

### Exercises

# 1
for x in range(1, 7):
  for y in range(1, 7):
    if (x+y == 7):
      print(str(x) + ", " + str(y) + ": sum is seven")

print(div)

# 2
count = 0
for x in range(1, 7):
  for y in range(1, 7):
    if (x+y == 7):
      count = count + 1

print(count)

print(div)

# 3
randoms = [3, 6, 20394, 8, 49, 3]
count = 0
for x in randoms:
    if (x % 3 == 0):
        count = count + 1
print(count)

print(div)

# 4
for x in randoms:
  if (x > 10):
    count = count + 1

print(count)
print(div)

# 5
nums = [1, 2, 3, 4, 5]
nums.append(6)
for x in range(7, 21):
  nums.append(x)

print(nums)

print(div)

# 6
nums[0] = nums[0] + 3
print(nums)

print(div)

# 7
for idx in range(len(nums)):
  nums[idx] = nums[idx] * -1

print(nums)

print(div)

# 8
channels = ["abc", "bbc", "mbc", "cnn"]
for i in range(len(channels)):
  channels[i] = channels[i] + " channel"

print(channels)

print(div)

# 9
for x in range(0, 10):
  if (x % 2 == 0):
    print("even")
