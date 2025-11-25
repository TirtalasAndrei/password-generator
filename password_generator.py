import random

list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


print(" --- Password Generator --- ")
choice = int(input("Choose (1 or 2) 1 if you want to type yourself how many characters you want in your password 2 if you want to generate automatic your password: "))
password_list = []
# Hard way
if choice == 1:
    nr_letters = int(input("Enter how many letters you want to have on your password: "))
    nr_numbers = int(input("Enter how many numbers you want to have on your password: "))
    nr_symbols = int(input("Enter how many symbols you want to have on your password: "))



    for char in range(0, nr_letters):
        password_list.append(random.choice(list_letters))

    for char in range(0, nr_numbers):
        password_list.append(random.choice(list_numbers))

    for char in range(0, nr_symbols):
        password_list.append(random.choice(list_symbols))


elif choice == 2:
    password_length = 16

    complet_list = list_letters + list_numbers + list_symbols

    for char in range(0, password_length):
        password_list.append(random.choice(complet_list))

else:
    print("Invalid choice!")

if len(password_list) > 0:
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your new password is: {password}")