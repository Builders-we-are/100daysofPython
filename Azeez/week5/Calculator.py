#Calculator

#Add
def add(n1, n2)
    return n1 + n2

#subtract
def subtract(n1, n2)
    return n1 - n2

#Multiply
def multiply(n1, n2)
    return n1 * n2

#Divide
def divide(n1, n2)
    return n1 / n2

#Create a dictionary with the symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#Ask for numbers to calculate
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

#Create a loop that prints symbols from deictionary 

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the  line above: ")
#pass chosen symbol from dictionary and store as variable
calculation_function = operations[operation_symbol]

#Create new function based on the choice of the user
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#USING RETURN IN CODE TO EXTEND CALCULATION
#Here we select "*" which overides the "+" we selected on line 26.
operation_symbol = input("Pick an operation: ") 
num3 = int(input("What's the next number?: "))

#Here the calculation_function selected will be the multiply() function
calculation_function = operations[operation_symbol] 

#Here the code will be:
#second_answer = multiply(multiply(num1, num2), num3) Two parameters in new function
#second_answer = 2 * 3 * 3 = 18
second_answer = calculation_function(first_answer, num3)
#In the next lesson, we will delete all the code from line 34-48 so don't worry
#It won't affect your final project.
#But it's a good oportunity to practice debugging. 🐞

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")






