

import math

n = 11

def prime_checker(number):
    really_prime = True
    for x in range(2,n):
        if number % x == 0:
            really_prime = False
    if really_prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
        

#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
prime_checker(number=n)


# George version ================================================

def prime_checker(number):
    for x in range(2,(number+1)):
        if x < number and number % x == 0: 
            print ("not prime")
            # print(x)
            break
        elif x == number:
            print ("prime")
            break

number = int(input("Check this number: "))
prime_checker(number)



# IK version ================================================

import math

def prime_checker(number):
    really_prime = True
    for x in range(2,n/2):
        if number % x == 0:
            really_prime = False
    if really_prime == False:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")
        
 
n = int(input("Check this number: "))
prime_checker(number=n)
