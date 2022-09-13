#Exercise 1 - Data Types
print("#Exercise 1 - Data Types\n")

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]), "\n")

#Exercise 2 - BMI Calculator
print("#Exercise 2 - BMI Calculator\n")

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / (float(height) ** 2 )
print(int(bmi), "\n")

#Exercise 3 - Life in Weeks
print("#Exercise 3 - Life in Weeks\n")

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#365 days 52 weeks and 12 months in a year 
age = int(age)
days = (90 - age) * 365
weeks = (90 - age) * 52
months = (90 - age) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.\n")

#Day2 project
print("#Day2 Project\n")

print("Welcome to the tip calculator!\n")

total_bill = input("What was the total bill?\n")
total_bill = float(total_bill)
total_tip = input("How much tip would you like to give?\n")
total_tip = float(total_tip)
num_of_people = input("How many people to split the bill?\n")
num_of_people = int(num_of_people)

#calculate how much per person 

total_bill_plus_tip = total_bill + (total_bill * (total_tip/ 100))
per_person_cost = round(total_bill_plus_tip / num_of_people, 2) 
per_person_cost = "{:.2f}". format(per_person_cost)

print(f"Each person should pay: ${per_person_cost}")
