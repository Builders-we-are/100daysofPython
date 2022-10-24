# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

true_count_1 = lower_case_name1.count("t") + lower_case_name1.count("r")+lower_case_name1.count("u")+lower_case_name1.count("e")
true_count_2 = lower_case_name2.count("t") + lower_case_name2.count("r")+lower_case_name2.count("u")+lower_case_name2.count("e")

love_count_1 = lower_case_name1.count("l") + lower_case_name1.count("o")+lower_case_name1.count("v")+lower_case_name1.count("e")
love_count_2 = lower_case_name2.count("l") + lower_case_name2.count("o")+lower_case_name2.count("v")+lower_case_name2.count("e")

total_true = true_count_1 + true_count_2
total_love = love_count_1 + love_count_2

love_score = int(str(total_true) + str(total_love))
 
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")








