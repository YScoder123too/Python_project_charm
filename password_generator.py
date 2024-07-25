import random  #puri library import kar do lol

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letter = int(input('How many letters do you want?'))
nr_numbers = int(input('How many numbers do you want?'))
nr_symbols = int(input('How many symbols do you want?'))

password_list = []  #We like is empty duh
for letter in range(1, nr_letter + 1):
    password_list.append(random.choice(letters))  #choice and shuffle are subparts of random library
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

#print(password_list)

#this is basically to print the password in normal form because if we directly print it it will comes in a form of list
random.shuffle(password_list)#shuffling because we want strong password
password = ""
for i in password_list:
    password += i

print(f'Your password is: {password}')
