print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? \n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? \n").strip('%'))
people = int(input("How many people to split the bill? \n"))

try:
    total_bill = (bill * tip_percentage/100 + bill) / people
    final_amount = "{:.2f}".format(total_bill)
    print(f"Each person should pay: ${final_amount}")
except ZeroDivisionError:
    total_bill = bill * tip_percentage/100 + bill
    final_amount = "{:.2f}".format(total_bill)
    print(f"Your total bill ${final_amount}")