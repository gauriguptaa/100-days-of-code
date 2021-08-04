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


def check_resources(coffee):
    if coffee not in "espresso":
        if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            return False
    if MENU[coffee]["ingredients"]["water"] > resources["water"] and MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        return False
    else:
        return True


def check_money(coffee):
    print("Please insert coins")
    quarters = float(input("How Many Quarters: "))
    dimes = float(input("How Many Dimes: "))
    nickles = float(input("How Many Nickles: "))
    penny = float(input("How Many Pennies: "))
    total_money = (0.25*quarters) + (0.1*dimes) + (0.05*nickles) + (0.01*penny)
    if total_money > MENU[coffee]["cost"]:
        print(f"Your change is ${'{0:.2f}'.format(total_money - MENU[coffee]['cost'])}")
        return True
    if total_money == MENU[coffee]["cost"]:
        return True
    return False


def recalculate_resource(coffee):
    if coffee not in "espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def generate_report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")


machine_running = True
while machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Coffee Machine is turned off")
        machine_running = False
    elif choice == "report":
        generate_report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        if not check_resources(choice):
            print("Not Sufficient resources are available")
            machine_running = False
        else:
            if not check_money(choice):
                print("Not Sufficient money")
                machine_running = False
            else:
                print(f"Your {choice} is served , please Enjoy")
                recalculate_resource(choice)
    else:
        print("Invalid entry")


