#Slicing with indexes
x = "computer"
print(x[5])
print(x[3:])
print(x[-1])
print(x[1:5])
print(x[1:6:2 ])

#Multiplying a sequence
#String
a = "bug" * 3
print(a)

#List
b = [8,5] * 3
print(b)

#Boolean Logic
#string
c = "bug"
print("g" in c)

#Tuple
d = ("Kevin", "Rick", "Paul")
print("Henry" in d)

#Iterating through items in a sequence
e = [7, 8, 3]
for item in e:
    print(item)

#Sum of Sequence
#List
f = [2, 5, 8, 12]
print(sum(f))
print(sum(f[-2:]))

#Sorting through sequence
#Tuple
g = ("Kevin", "Jenny", "Craig", "David")
print(sorted(g))

#Count function
#String
h = "Elephantiasis"
print (h.count("h"))

#Unpacking using variables
i = ["pig", "cow", "horse"]
a , b, c = i