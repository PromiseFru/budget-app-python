class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description = ""):
        self.ledger.append({
            "amount": -amount,
            "description": description
        })

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance    
    


# food = Category("food")
# food.deposit(900,"food")
# food.withdraw(100,"food2")
# food.deposit(50,"food3")


# cloth = Category("cloth")
# cloth.deposite(500)

# print(food.get_balance())
# print(cloth.ledger[0])


def create_spend_chart(categories):
    return "hello world"