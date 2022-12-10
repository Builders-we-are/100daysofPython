
from resources import resources, MENU


def clear():
    import os
    os.system("clear")


def is_resource_sufficient(order_ingredients):
    """RETURNS TRUE WHEN INGREDIENTS ARE ENOUGH TO MAKE THE DRINK"""
    resource_check = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            resource_check = False
    return resource_check


def process_coins():
    """RETURNS THE TOTAL $$$ VALUE OF COINS"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted , or False when is not enough"""
    change = money_received - drink_cost
    if money_received >= drink_cost:
        if money_received > drink_cost:
            print(f"Here is ${change:.2f} in change.")
        global profit
        profit += drink_cost
        return True
    elif money_received > 0:
        print(
            f"Sorry there's not enough money. ${money_received:.2f} has been refunded.")
        return False
    else:
        print("Sorry there's not enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    """"Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\nHere is your {drink_name} ☕️ ")


clear()

profit = 0
is_on = True

while is_on:
    # TODO 1:Print Report
    need = input(
        "\n \n \n \n \nWhat would you like? (espresso/latte/cappuccino): ").lower()
    clear()
    if need == "off":
        is_on = False
    elif need == "report":
        water_left = resources['water']
        milk_left = resources['milk']
        coffee_left = resources['coffee']

        print(f"Water:  {water_left}ml")
        print(f"Milk:   {milk_left}ml")
        print(f"Coffee: {coffee_left}g")
        print(f"Money:  ${profit:.2f}")
    elif need in MENU.keys():
        drink = MENU[need]
        print(
            f"\n \n \n \n \nThe customer has ordered {need}. ")
        if is_resource_sufficient(drink["ingredients"]):
            print(f"Your bill is ${drink['cost']:.2f}")
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(need, drink["ingredients"])
    else:
        print("Drink is not on the list, try again.")
