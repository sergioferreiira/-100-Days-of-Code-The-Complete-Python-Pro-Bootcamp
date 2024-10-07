import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '?', '/']


alphabet_password = int(input("How many letters? "))
numbers_password = int(input("How many numbers? "))
symbols_password = int(input("How many symbols? "))

x = []
y= 0

for n in range(0, alphabet_password):
    x.append(str(random.choice(alphabet)))

for n in range(0, numbers_password):
    x.append(str(random.choice(numbers)))

for n in range(0, symbols_password):
    x.append(str(random.choice(symbols)))


random.shuffle(x)

password = ''.join(x)

print(password)
