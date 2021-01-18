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
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True
    
    def __str__(self):
        result = "{}"
        return result.format(self.name.center(30, "*"))   
         
# cloth = Category("cloth")
food = Category("food")
# food.transfer(900, cloth)
food.withdraw(100,"food2")
food.deposit(50,"food3")


# # cloth.deposite(500)

# # print(food.get_balance())
# print(cloth.ledger)
print(str(food))


def create_spend_chart(categories):
    return "hello world"