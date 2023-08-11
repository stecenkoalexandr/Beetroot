import random

number = 0
my_list = []
while number < 10:
    number += 1
    my_list.append(random.randint(0, 100))
print(my_list)