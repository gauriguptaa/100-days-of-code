from MenuItem import Menu, MenuItem
from MoneyMachine import MoneyMachine
from CoffeeMaker import CoffeeMaker

coffee_machine_running = True

Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
while coffee_machine_running:
    coffee = input("What do you want to order: " + Menu.get_items())
    if coffee == "report":
        CoffeeMaker.report()
    elif coffee == "off":
        print("Coffee Machine is turned off....")
    elif coffee in ["espresso", "cappuccino", "latte"]:
        item = Menu.find_drink(coffee)
        if CoffeeMaker.is_resources_sufficient(item):
            if MoneyMachine.make_payment(item.cost):
                CoffeeMaker.make_coffee(item)
            else:
                print("Not Enough Money..")
    else:
        print("Please Enter a Valid Option")

