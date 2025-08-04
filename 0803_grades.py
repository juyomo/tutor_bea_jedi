grade = 89.99999999
# edge cases
# it's important to test your edge cases!

# if grade >= 90, A
# [80, 90) B
# [70, 80) C+
# [60, 70) C
# [50, 60) C-
# [0 50) F

# ex) 89.4 -> B
# >=, <=, >, <, and, or

if (grade >= 90):
    print ('A')

# [80, 90) B
if (grade >= 80 and grade < 90):
    print ('B')
