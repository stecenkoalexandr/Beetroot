# Task 1
import random

secret_number = random.randint(1, 10)
user_guess = int(input("Guess the number (between 1 and 10): "))

if user_guess == secret_number:
    print("Congratulations! Your guess is correct.")
else:
    print(f"Sorry, the correct number was {secret_number}.")

#fine, but isdigit check is nice to have


# Task 2
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
next_birthday_age = age + 1
print(f"Hello {name}, on your next birthday you'll be {next_birthday_age} years.")

# +

# Task 3
import random

input_string = input("Please enter an input string: ")
random_strings = [''.join(random.sample(input_string, len(input_string))) for _ in range(5)]

print("Random Strings:")
for random_string in random_strings:
    print(random_string)

#very good sollution with using of list comprehension