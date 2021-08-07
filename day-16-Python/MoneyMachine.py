class MoneyMachine:
    def __init__(self):
        self.total_money = 0

    def make_payment(self, cost):
        print("Please enter Money.")
        quarters = float(input("How many Quarters:"))
        nickle = float(input("How many nickles:"))
        dimes = float(input("How many dimes:"))
        pennies = float(input("How many pennies:"))
        self.total_money = 0.25*quarters + 0.1*dimes + 0.05*nickle + 0.01*pennies
        if self.total_money >= cost:
            print(f"Your change is :- ${'{0:.2f}'.format(self.total_money-cost)}")
            return True
        else:
            return False

