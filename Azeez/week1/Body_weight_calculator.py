
#number = int(input("Which number do you want to check?"))

#if number % 2 == 0 :
#   print("Even number")

#else :
#    print("Odd number")


weight = int(input("What is your weight?"))
height = int(input("What is your height?"))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")