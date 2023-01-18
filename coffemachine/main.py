
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user by asking “What would you like?
# user_request = input("“What would you like? (espresso/latte/cappuccino):")
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print Report.


# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
profit = 0


def is_resource_sufficient(order_ingredients):
    """Inform you if there is enough resources to make a coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted """

    quarters = int(input("how many quarters?: ")) * 0.25
    dime = int(input("how many dime?: ")) * 0.10
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dime + nickels + pennies

    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, of False if ,money is insufficient."""
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True

while is_on:
    user_request = input("“What would you like? (espresso/latte/cappuccino):")
    if user_request.lower() == 'off':
        is_on = False
    elif user_request == 'report':
        print(f"Water: {resources['water']}ml Milk: {resources['milk']}ml Coffee: {resources['coffee']}ml Money: ${profit}")

    else:
        drink = MENU[user_request]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_request, drink["ingredients"])




