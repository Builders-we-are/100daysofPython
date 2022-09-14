#Constructors creating a new list
a = [m for m in range(8)]
print(a)
b = [c**2 for c in range(10) if c>4]
print(b)

#Deleting from a list
c = [3, 4, 5, 6, 7, 8]
del(c[3])
print(c)

#Append add to list
d = [8, 5, 4, 3]
d.append(9)
print(d)

#Extend
c = [3, 4, 5, 6, 7, 8]
d = [8, 5, 4, 3]
c.extend(d)
print(c)

#insert
c = [3, 4, 5, 6, 7, 8]
c.insert(1, 71)
print(c)

#remove 
c = [3, 4, 5, 6, 7, 8]
c.remove(4)
print(c)

#reverse
c = [3, 4, 5, 6, 7, 8]
c.reverse()
print(c)