from pyclbr import Function


programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Retrieving items from dictionary.
print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

programming_dictionary["Module"] = "Library that contains multiple functions"

print(programming_dictionary)

#Create an empty dictionary.
empty_dictionary = {}

#Wiping a dictionary
programming_dictionary = {}

#Loop through a dictionary
for key in programming_dictionary:
    print(key)

#Nesting Dictionary in a Dictionary

travel_log = {"France: {"cities_visited": ["Paris","Lille"], "total_visits":12}, "Germany":{}  




 