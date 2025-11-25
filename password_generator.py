import random

list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print(" --- Password Generator --- ")
nr_letters = int(input("Enter how many letters you want to have on your password: "))
nr_numbers = int(input("Enter how many numbers you want to have on your password: "))
nr_symbols = int(input("Enter how many symbols you want to have on your password: "))

# Easy way

password = ""

for char in range(0, nr_letters):
    password += random.choice(list_letters)

for char in range(0, nr_numbers):
    password += random.choice(list_numbers)

for char in range(0, nr_symbols):
    password += random.choice(list_symbols)

print(f"Your new password is: {password}")