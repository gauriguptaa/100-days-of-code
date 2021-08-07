class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']} ,Milk: {self.resources['milk']} ,Coffee: {self.resources['coffee']}")

    def is_resources_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                can_make = False
                print(f"Sorry there is not enough {item}")

        return can_make

    def make_coffee(self, drink):
        print("Your coffee is served ☕️Enjoy")
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]


