class Payment:
    def __init__(self):
        self.payed = {
            "euros": 0,
            "cents": 0
        }

    def collect_payment(self):
        two_euros = int(input("How many 2 Euro coins do you want to pay?: "))
        one_euros = int(input("How many 1 Euro coins do you want to pay?: "))
        fifty_cents = int(input("How many 50 cents do you want to pay?: "))
        twenty_cents = int(input("How many 20 cents do you want to pay?: "))
        ten_cents = int(input("How many 10 cents do you want to pay?: "))
        five_cents = int(input("How many 5 cents do you want to pay?: "))
        two_cents = int(input("How many 2 cents do you want to pay?: "))
        one_cents = int(input("How many 1 cents do you want to pay?: "))

        total_euros = (2 * two_euros) + one_euros
        total_cents = ((50 * fifty_cents) + (20 * twenty_cents) +
                       (10 * ten_cents) + (5 * five_cents) + (2 * two_cents) +
                       one_cents)

        self.payed["euros"] += total_euros + (total_cents // 100)
        self.payed["cents"] += total_cents % 100

        if self.payed["cents"] >= 100:
            self.payed["euros"] += self.payed["cents"] // 100
            self.payed["cents"] = self.payed["cents"] % 100

    def payment_in_cents(self):
        return (self.payed["euros"] * 100) + self.payed["cents"]


if __name__ == "__main__":
    payment = Payment()