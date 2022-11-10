
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_letters = 4
nr_symbols = 2
nr_numbers = 2

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# print(part1)
part2 = ""
for each1 in range(0,nr_letters):
    part1 = random.randint(0,len(letters)-1)
    part2 = part2 + letters[part1]
# print(part2)

part3 = ""
for each1 in range(0,nr_numbers):
    part1 = random.randint(0,len(numbers)-1)
    part3 = part3 + numbers[part1]
# print(part3)

part4 = ""
for each1 in range(0,nr_symbols):
    part1 = random.randint(0,len(symbols)-1)
    part4 = part4 + symbols[part1]
# print(part4)

print(part2 + part3 + part4)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
