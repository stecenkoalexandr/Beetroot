week = ['monday', 'tuesday', 'wensday', 'thursday', 'friday', 'saturday', 'sunday']
num = 0
for i in week:
    num += 1
    first = [i, num]
    first_reversed = first.copy()
    first_reversed.reverse()

    first_tuple = tuple(first)
    second_tuple = tuple(first_reversed)

    print(first_tuple)
    print(second_tuple)
