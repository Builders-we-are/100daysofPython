

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
os.system("clear")
print("\n \n \n \n \n \n \n \n ")

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(
        f"What would you like? {options}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in options:
        drink = menu.find_drink(choice)
        print(drink)
    else:
        print("Choice cannot be found. Try again")
        is_on = False
