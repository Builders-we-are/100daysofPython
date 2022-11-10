# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if add_pepperoni == "Y":

    if size == "S":
        bill = 15+2
    elif size == "M":
        bill = 20+3
    elif size == "L":
        bill = 25+3
    else:
        bill = 0

else:
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25
    else:
        bill = 0

if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}.")



