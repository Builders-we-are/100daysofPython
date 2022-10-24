

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? \n$"))
people = int(input("How many people to split the bill? \n"))
tip_percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? \n"))

# would be nice to add if statements for input <= 0

total_bill = bill * (1 + tip_percentage/100)  / people
final_amount = round(total_bill,2)+0.00
print(f"Each person should pay: ${final_amount}")


# Compare to more advanced ans. below

# See how two decimal places are forced to 
# make it $27.90 where as above code would show $27.9 instead


# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill? \n$"))
# tip_percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? \n").strip('%'))
# people = int(input("How many people to split the bill? \n"))

# try:
#     total_bill = (bill * tip_percentage/100 + bill) / people
#     final_amount = "{:.2f}".format(total_bill)
#     print(f"Each person should pay: ${final_amount}")
# except ZeroDivisionError:
#     total_bill = bill * tip_percentage/100 + bill
#     final_amount = "{:.2f}".format(total_bill)
#     print(f"Your total bill ${final_amount}")
