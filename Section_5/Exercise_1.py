# # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# student_heights = [10, 20, 30]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(f"I want to eat {fruit.lower()} pie")

count = 0
summ = 0

# print(student_heights)

for n in student_heights:
    count += 1
    summ = summ + n
    
print (round(summ/count))
