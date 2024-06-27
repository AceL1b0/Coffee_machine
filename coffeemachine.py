class CoffeeMachine:
    def __init__(self):
        self.storage = {"coffee": 200,
                        "milk": 500,
                        "water": 500,
                        }

    def report(self):
        for item, quantity in self.storage.items():
            print(f"{item}: {quantity}")

    def use_items(self, items_to_use):
        for item, quantity in items_to_use.items():
            if item in self.storage:
                if self.storage[item] < quantity:
                    raise ValueError("Storage doesn't have enough ingredients,"
                                     " waiting for refill.")
                self.storage[item] -= quantity

        for item, quantity in self.storage.items():
            return item, quantity


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()