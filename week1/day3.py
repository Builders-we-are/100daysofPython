#Exercise 1 - Odd or Even
print("#Exercise 1 - Odd or Even\n")

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.\n")
else:
    print("This is an odd number.\n")

#Exercise 2 - BMI 2.0
print("#Exercise 2 - BMI 2.0\n")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/ (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.\n")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.\n")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.\n")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.\n")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.\n")

#Exercise 3 - Leap Year
print("#Exercise 3 - Leap Year\n")

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 400 == 0:
        print("Leap year.\n")
    elif year % 100 == 0:
        print("Not leap year.\n")
    else:
        print("Leap year.\n")
else:
    print("Not leap year.\n")

#Exercise 4 - Pizza Order Practice
print("#Exercise 4 - Pizza Order Practice")

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
final_bill = 0

if size == 'S':
    final_bill += 15
    if add_pepperoni == 'Y':
        final_bill += 2
    if extra_cheese == 'Y':
        final_bill += 1
    print(f"Your final bill is: ${final_bill}.\n")

elif size == 'M':
    final_bill += 20
    if add_pepperoni == 'Y':
        final_bill += 3
    if extra_cheese == 'Y':
        final_bill += 1
    print(f"Your final bill is: ${final_bill}.\n")

elif size == 'L':
    final_bill += 25
    if add_pepperoni == 'Y':
        final_bill += 3
    if extra_cheese == 'Y':
        final_bill += 1
    print(f"Your final bill is: ${final_bill}.\n")

#Exercise 5 - Love Calculator
print("#Exercise 5 - Love Calculator")

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_total = 0
love_total = 0

#check true
combined_name = name1.lower() + name2.lower()

for char in "true":
    if char in combined_name:
        true_total += combined_name.count(char)

for char in "love":
    if char in combined_name:
        love_total += combined_name.count(char)

total_score = str(true_total) + str(love_total)

total_score_as_int = int(total_score)

if total_score_as_int < 10 or total_score_as_int > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.\n")

elif total_score_as_int >= 40 and total_score_as_int <= 50:
    print(f"Your score is {total_score}, you are alright together.\n")

else:
    print(f"Your score is {total_score}.\n")

#Day3 Final Project
print("#Day3 Final Project")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
decision = input ("Do you want to go left or right?\n")
decision = decision.lower()
if decision == 'left':
  decision = input ("Do you want to swim or wait?\n")
  decision = decision.lower()
  if decision == 'wait':
    decision = input ("Choose a color\n")
    decision = decision.lower()
    if decision == 'red':
      print("You were burned by fire. Game Over!!!\n")
    elif decision == 'blue':
      print("You have been eaten by beasts, Game Over !!!\n")
    elif decision == 'yellow':
      print("You Win!!!!\n")
    else:
      print("You lose, Game Over!!!!\n")
  else:
    print("You were attached by trout, Game Over!!!\n")
else:
  print("You fell into a hole, Game Over!!!")