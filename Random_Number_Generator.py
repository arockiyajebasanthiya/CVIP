#import random module
import random

#Initialize the Variables 
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\t\t*****Welcome to the SecurePass Creator!*****\t\t\n")
print("\n\t\t\tDesign Your Dream Password\t\t\t\t\n")

#Get the basic requirements from users
nr_letters = int(input("\nHow many letters should we include?\n"))
nr_symbols = int(input(f"How many symbols for your password?\n"))
nr_numbers = int(input(f"How many digits for your password?\n"))

password_list = []

#generate random letters
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    
#generate random symbols
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(numbers))
    
#generate random digits
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(symbols))

#randomize the order of the generated password
random.shuffle(password_list)

#Convert generated password into list
password = ""
for char in password_list:
    password += char
print("char", char)

# convert list to string
pwd = ''.join(password_list)

#Display the generated random Password
print(f"Your random password to use is: {pwd}")
