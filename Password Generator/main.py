# Password Generator Project
import random

def char_range(start, end):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for char in range(ord(start), ord(end) + 1):
        yield chr(char)



letters = list(char_range('a', 'z')) + list(char_range('A', 'Z'))

numbers = list(char_range('0', '9'))
symbols = list(char_range('!', '/'))

print("Welcome to the PyPassword Generator!")

print("How many letters would you like in your password?")
nr_letters = int(input())

print("How many symbols would you like?")
nr_symbols = int(input())

print("How many numbers would you like?")
nr_numbers = int(input())

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
