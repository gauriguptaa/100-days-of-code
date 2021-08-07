class MenuItem:
    """Models each Menu Item"""
    def __init__(self, name, milk, water, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.Menu = [
          MenuItem(name="espresso", milk=0, water=50, coffee=18, cost=1.5),
          MenuItem(name="cappuccino", milk=50, water=250, coffee=24, cost=3),
          MenuItem(name="latte", milk=150, water=200, coffee=24, cost=2.5)
        ]

    def get_items(self):
        options = ""
        for item in self.Menu:
            options += item.name
            options += " / "
        return options

    def find_drink(self, order_name):
        for item in self.Menu:
            if item.name == order_name:
                return item
        return "Sorry the Drink is not available in the Menu"

