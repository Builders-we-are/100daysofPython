#Dictionary
x = {"pork":25.5, "beef":18.5, "chicken":65.5}
print(x)
x = dict(pork=25.5, beef=18.5, chicken=65.5)
print(x)

#To add an item to dictionary
x["shrimp"] = 23.4
x["fish"] = 37.9
print(x)

#To delete an item
del(x["shrimp"])
print(x)