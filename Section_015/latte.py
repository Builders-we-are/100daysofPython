
from resources import resources, MENU


def clear():
    import os
    os.system("clear")


clear()

water_left = resources['water']
milk_left = resources['milk']
coffee_left = resources['coffee']
total_cash = 0
is_on = True
make_coffee = True


def coffee():
    def report():
        print(f"Water:  {water_left}ml")
        print(f"Milk:   {milk_left}ml")
        print(f"Coffee: {coffee_left}g")
        print(f"Money:  ${total_cash}")

    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    total_cash = 0
    is_on = True
    make_coffee = True

    while is_on:
        # TODO 1:Print Report
        need = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if need == "off":
            is_on = False
            make_coffee = False
        if need == "report":
            report()
            make_coffee = False
        else:
            print(f"The customer has ordered {need}")

        # TODO 2:Check resources are sufficient?

        if (MENU[need]["ingredients"]["water"]) > water_left:
            print("Sorry there's not enough water")
            coffee()
        if (MENU[need]["ingredients"]["coffee"]) > coffee_left:
            print("Sorry there's not enough coffee")
            coffee()

        if need != "espresso":
            if (MENU[need]["ingredients"]["milk"]) > milk_left:
                print("Sorry there's not enough milk")
                coffee()

        # TODO 3:Process coins

        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
        paid_cash = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

        print(f"You paid ${paid_cash}")

        # TODO 4:Check transaction successful?
        print(f"It will cost ${MENU[need]['cost']}")

        change = paid_cash - MENU[need]["cost"]

        if paid_cash >= MENU[need]["cost"]:
            make_coffee = True
            if paid_cash > MENU[need]["cost"]:
                print(f"Here is ${change} dollars in change. ")

            # print("There's enough money")
            total_cash += paid_cash
        else:
            make_coffee = False
            print("Sorry there's not enough money. Money refunded.")
            break

        # TODO 5:Make coffee
        if make_coffee:
            water_left -= MENU[need]["ingredients"]["water"]
            coffee_left -= MENU[need]["ingredients"]["coffee"]
            if need != "espresso":
                milk_left -= MENU[need]["ingredients"]["milk"]
            print(f"Here is your {need}. Enjoy!")

        # def report():
        #     for key, name in enumerate(resources):
        #         print(f"{name.title()}: {resources[name]}ml")
        # print(list(resources.items())[key][:])


coffee()
