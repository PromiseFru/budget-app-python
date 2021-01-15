class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })


# food = Category("food")
# food.deposite(900,"food")

# cloth = Category("cloth")
# cloth.deposite(500)

# print(food.ledger[0])
# print(cloth.ledger[0])


def create_spend_chart(categories):
    return "hello world"