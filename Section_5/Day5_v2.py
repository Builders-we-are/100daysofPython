
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = 4
nr_symbols = 2
nr_numbers = 2

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
 
# password = ""
# for each1 in range(0,nr_letters):
#     part1 = random.randint(0,len(letters)-1)
#     password = password + letters[part1]
 
# for each1 in range(0,nr_numbers):
#     part1 = random.randint(0,len(numbers)-1)
#     password = password + numbers[part1]
 
# for each1 in range(0,nr_symbols):
#     part1 = random.randint(0,len(symbols)-1)
#     password = password + symbols[part1]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for each1 in range(0,nr_letters):
    part1 = random.randint(0,len(letters)-1)
    password_list = password_list + [letters[part1]]
 
for each1 in range(0,nr_numbers):
    part1 = random.randint(0,len(numbers)-1)
    password_list = password_list + [numbers[part1]]
 
for each1 in range(0,nr_symbols):
    part1 = random.randint(0,len(symbols)-1)
    password_list = password_list + [symbols[part1]]

print(password_list)

random.shuffle(password_list)

print(password_list)

password=""
for each in password_list:
    password += each 
    
print(password)



















