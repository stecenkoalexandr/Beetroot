# Task1
name = str(input("Please enter your name \n"))
day = str(input("Which day is today \n"))
message = f"Good day {name}! {day} is a perfect day to learn some Python."
print(message)

# Task2
first_name = "Oleksandr"
last_name = "Stetsenko"

full_name = first_name + " " + last_name
greeting = f"Hello, {full_name}! Nice to meet you."
print(greeting)

# Task3

a = int(input("Input 1st number\n"))
b = int(input("Input second number\n"))

# Addition
result_addition = a + b
print(f"Addition: {a} + {b} = {result_addition}")

# Subtraction
result_subtraction = a - b
print(f"Subtraction: {a} - {b} = {result_subtraction}")

# Division
result_division = a / b
print(f"Division: {a} / {b} = {result_division}")

# Multiplication
result_multiplication = a * b
print(f"Multiplication: {a} * {b} = {result_multiplication}")

# Exponent (Power)
result_exponent = a ** b
print(f"Exponent: {a} ** {b} = {result_exponent}")

# Modulus (Remainder)
result_modulus = a % b
print(f"Modulus: {a} % {b} = {result_modulus}")

# Floor Division
result_floor_division = a // b
print(f"Floor Division: {a} // {b} = {result_floor_division}")


# ok, fine. Good usage of f-string