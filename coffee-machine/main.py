def print_report(current_resources, earned_money):
    print(f"Water: {current_resources["water"]}ml")
    print(f"Milk: {current_resources["milk"]}ml")
    print(f"Coffee: {current_resources["coffee"]}g")
    print(f"Money: ${earned_money}")


def check_resources_sufficient(drink, current_resources):
    is_sufficient = True

    for resource, stock in current_resources.items():
        drink_ingredient = drink["ingredients"].get(resource, 0)

        if drink_ingredient > stock:
            print(f"Sorry there is not enough {resource}.")
            is_sufficient = False

    return is_sufficient


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_transaction_successful(money_received, drink_cost):
    global money

    if money_received >= drink_cost:
        money += drink_cost

        change = round(money_received - drink_cost, 2)
        print(f"Here is ${"%.2f" % change} in change.")

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

        return False


def make_coffee(drink_name, current_resources):
    drink = MENU[drink_name]

    if check_resources_sufficient(drink, current_resources):
        coins = process_coins()

        if check_transaction_successful(coins, drink["cost"]):
            for resource in current_resources:
                drink_ingredient = drink["ingredients"].get(resource, 0)
                current_resources[resource] -= drink_ingredient

            print(f"Here is your {drink_name} ☕️. Enjoy!")

            return current_resources


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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        break
    elif order == "report":
        print_report(resources, money)
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        drink = MENU[order]

        make_coffee(order, resources)
    else:
        print("You typed an invalid value.")
