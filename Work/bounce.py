# bounce.py
#
# Exercise 1.5
num_of_bounce = 0
new_height = 100

while(num_of_bounce < 10):
    new_height = new_height * (3/5)
    num_of_bounce += 1
    print(num_of_bounce, round(new_height, 4))

