def make_operation(operator, *args):
    result = None
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    else:
        print("Your input is not a valid operator")

    return result

a = make_operation('+', 7, 7, 2)
b = make_operation('-', 5, 5, -10, -20)
c = make_operation('*', 7, 6)
print(a, b, c)