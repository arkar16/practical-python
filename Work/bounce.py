# bounce.py
#
# Exercise 1.5
bounce_start = 100
bounce_height = bounce_start * .6

while bounce_height > 0.1:
    print(round(bounce_height, 4))
    bounce_height = bounce_height * .6

print(round(bounce_height, 4))
