
import os
os.system("clear")

print("\n \n \n \n \n \n \n \n \n ")

roman = { "I" : 1,
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000,
}

s = ["IV"]
split =[]
total = []
for each in s[0]:
    split.append(each)

print(split)
# print(len(split))

# s can only be between 1 and 15 letters long
if len(split)>15:
    exit()
#s must work for all digits from 1 to 3999 included
#s can only contain the roman dict. above
for letters in split:
    if letters not in roman:
        exit()
    total.append(roman[letters])

print(total)
print("I got to the end")

