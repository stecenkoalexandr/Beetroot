stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for item in stock:
    if item in prices:
        total_price += stock[item] * prices[item]

print("Sum of Stock:", total_price)