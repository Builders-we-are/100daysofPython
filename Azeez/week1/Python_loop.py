"""
fruits = ["Apple", "Peach", "Pear","Almond"]
for fruit in fruits:
    print(fruit)


student_heights = input("Input a list of student heights?\n").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height+= height

number_of_students = 0
for student in student_heights:
    number_of_students +=1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)

###
student_scores = input("Input a list of student scores?\n").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_scores = 0
for score in student_scores:
    if score > highest_scores:
        highest_scores=score
        print(f"The highest score in the class is: {highest_scores}")
###
"""
total_number = 0
for number in range(1,101):
    total_number += number

print(total_number)

###
total_even_number = 0 #variable2
for number in range(2,5,2): #start,end,step2,4
    total_even_number += number #2,4
    print(total_even_number)#2


for number in range(1,17):#16
    
    if number %3 == 0: # if this is true
        print("Fizz")
        #it will leave loop
    elif number %5 == 0:
        print("Buzz")
   #number =16
   elif number % 3 == 0 and number % 5 == 0: #15 %3 = 0 True and  15 % 5 == 0 True
        print("Fizzbuzz") # print ==> Fizzbuzz
        #exit 
    else:
        print(number)

