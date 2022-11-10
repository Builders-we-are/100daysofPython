

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# print(logo)

#Add
def add(n1,n2):
    return n1+n2 
#Subtract
def subtract(n1,n2):
    return n1-n2
#Multiply
def multiply(n1,n2):
    return n1*n2
#Divide
def divide(n1,n2):
    return n1/n2

operations = { "+" : add, 
'-' : subtract,
'*' : multiply,
'/' : divide,
}

def calculator():
    num1 = float(input("What's the first number? :"))

    # for symbol in operations:
        # print (symbol)

    should_continue= True

    while should_continue:
        operation_symbol = input("\nPick an operation: ")
        num2 = float(input("\nWhat's the next number? :"))
        answer = operations[operation_symbol](num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} \n")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y" :
            num1 = answer
        else:
            should_continue = False
            calculator()
        

calculator()








