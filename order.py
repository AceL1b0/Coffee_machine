from coffeemachine import CoffeeMachine
from payment import Payment


class Order:
    def __init__(self, machine: CoffeeMachine):
        self.machine = machine
        self.espresso = {
            "coffee": 9,
            "milk": 0,
            "watter": 50
        }
        self.cappuccino = {
            "coffee": 18,
            "milk": 50,
            "watter": 100
        }
        self.latte = {
            "coffee": 18,
            "milk": 100,
            "watter": 100}

    def drink(self, name: str):
        prices = {
            "espresso": 300,
            "cappuccino": 400,
            "latte": 500
        }

        name = name.lower()
        if name in prices:
            drink_price = prices[name]
            print(f"The price for {name} is {drink_price / 100:.2f} EUR.")
            payment = Payment()
            payment.collect_payment()
            total_payment = payment.payment_in_cents()

            if total_payment >= drink_price:
                change = total_payment - drink_price
                euros_change = change // 100
                cents_change = change % 100
                self.machine.use_items(getattr(self, name))
                print(f"Payment received: {total_payment / 100:.2f} EUR.")
                if change > 0:
                    print(f"Change to be returned: {euros_change} euros, "
                          f"{cents_change} cents.")
                    print("Here is your coffee. Enjoy!!")
            else:
                print(f"Insufficient payment. The price for {name} is "
                      f"{drink_price / 100:.2f} EUR. ")
        else:
            print("You can order these coffees: (espresso/cappuccino/latte")


if __name__=="__main__":
    order = Order()