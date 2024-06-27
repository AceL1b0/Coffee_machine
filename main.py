from order import Order
from coffeemachine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()
    order = Order(coffee_machine)

    while True:
        coffee_type = input("Welcome to the best coffee machine. "
                            "You can order Espresso, Cappuccino or Latte. "
                            "What is your order?\n")

        try:
            order.drink(coffee_type)
            coffee_machine.report()
        except ValueError as e:
            print(f"Error: {e}")

        another_order = input("Would you like to place another order? "
                              "(yes/no): ").strip().lower()
        if another_order != "yes":
            print("Thank you, have a nice day!")
            break


if __name__ == "__main__":
    main()