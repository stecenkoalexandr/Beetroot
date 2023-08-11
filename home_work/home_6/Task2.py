import random

# short_version
my_list_a = [random.randint(0, 100) for _ in range(10)]
print(my_list_a)

my_list_b = [random.randint(0, 100) for _ in range(10)]
print(my_list_b)

my_list_c = set(my_list_a + my_list_b)
my_list_c = list(my_list_c)
print("List C is combined (a) and (b) list", my_list_c)


# Long version

number1 = 0
list_a = []
list_b = []

while number1 < 10:
    random_number = random.randint(0, 100)
    list_a.append(random_number)

    random_number = random.randint(0, 100)
    list_b.append(random_number)

    number1 += 1

print("List A:", list_a)
print("List B:", list_b)

list_c = set(list_a + list_b)
list_c = list(list_c)
print("List_C is combined (a) and (b) list", list_c)

