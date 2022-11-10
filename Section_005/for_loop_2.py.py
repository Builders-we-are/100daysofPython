# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
n=0
big=0 

for n in student_scores:
    if n > big:
        big = n


# print(n)
print(f'The highest score in the class is: {big}')




