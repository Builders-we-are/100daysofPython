# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# �� Don't change the code above 👆

#Write your code below this line 👇

leap4 = year % 4
leap100 = year % 100
leap400 = year % 400

# print(leap4, leap100, leap400)

if leap4 == 0 and leap400 == 0:
    print("Leap year.")

elif leap4 == 0 and leap100 != 0:
    print("Leap year.")

else:
     print("Not leap year.")


