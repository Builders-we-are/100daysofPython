#Write your code below this line 👇
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
        

    

                


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
prime_checker(number=n)

