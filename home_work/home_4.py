# Task 1
var = str(input("Input anything, please!\n"))
inp = "You input:( " + var + ") symbols"
print(inp)
if len(var) < 2:
    print("You input not enought symbols, try again please")
else:
    f_1 = var[0:2]
    f_2 = var[-2:]
    print(f_1 + f_2)

#Nice!

# Task 2

get_num = input("Please input phone number: \n")

if get_num.isdigit():  # Check if input consists of digits only
    print("You input: " + get_num + " number\n")

    if len(get_num) == 10:
        print("It's a valid phone number.\n")
    else:
        print("It's not a valid phone number.")
else:
    print("You did not input a number.")

# +

# Task 3
import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)
symbol = random.choice(['+', '-', '*', '/'])

print("Welcome Mathematick battle")
print(str(num1) + symbol + str(num2) + " = ?\n")

user_input = input("Please input your answer here: \n")
user_answer = int(user_input)  # Convert the user's input to an integer

if symbol == '+':
    correct_answer = num1 + num2
elif symbol == '-':
    correct_answer = num1 - num2
elif symbol == '*':
    correct_answer = num1 * num2
elif symbol == '/':
    correct_answer = num1 / num2  # Note: This is a floating-point division

if user_answer == correct_answer:
    print("Your input is the correct answer:", user_answer)
else:
    print("Sorry, you made a mistake. The correct answer is:", correct_answer)

# very good solution

# Task 4

my_name = "Oleksandr"

user_input = input("Please enter your name: ")

if user_input.lower() == my_name: 
    print(" It`s True")
else:
    print("It`s False")

#all is ok, but value in my_name variable is not in lower case. you can add my_name.lower() method call to the user_input.lower() == my_name check