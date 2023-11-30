menu = {
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. prompt the user the type of coffee he/she likes


# TODO: 4. check resources sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, and False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"There is not enough {item}.")
            return False
    return True


# TODO: 5. process coins
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# TODO: 6. check if transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough enough money. Money refunded!")
        return False


# TODO: 7. make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕.")


is_on = True
while is_on:
    choice = input("What would you like? 'espresso', 'latte', or 'cappuccino': ").lower()

    # TODO: 2. turn off the coffee machine
    if choice == "off":
        print("Thanks for shopping with us. Goodbye!")
        is_on = False

    # TODO: 3. print report
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")

    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
            make_coffee(choice, drink["ingredients"])
