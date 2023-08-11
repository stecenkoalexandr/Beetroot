all_numbers = list(range(1, 101))
result_list = []

i = 0
while i < len(all_numbers):
    if all_numbers[i] % 7 == 0 and all_numbers[i] % 5 != 0:
        result_list.append(all_numbers[i])
    i += 1

print(result_list)
