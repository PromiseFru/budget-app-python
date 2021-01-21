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
        body = ""
        title = self.name.center(30, "*")
        total = "Total: {:.2f}".format(self.get_balance())
        for i in self.ledger:
            body += "{:.23} {:>{w}.2f}\n".format(i["description"], i["amount"], w = 29-len(i["description"]))
        txt = "{}\n{}{}"
        result = txt.format(title, body, total)
        return result
         
cloth = Category("cloth")
food = Category("food")
house = Category("house")
promise = Category("promise")
# food.transfer(900, cloth)
# food.deposit(500,"food3")
# food.withdraw(100,"food2")
# # cloth.deposite(500)

# # print(food.get_balance())
# print(cloth.ledger)
# print(str(food))
# print(food.ledger)


def create_spend_chart(categories):
    chart = ""
    # draw axis
    for i in range(100, -1, -10):
        chart += "{:>3}{}\n".format(i, "|")

    # line
    line = "    -"
    for i in categories:
        line += "---"

    # max length
    lengths = []
    for i in categories:
        lengths.append(len(i.name))
    maxLength = max(lengths)

    # name of categories
    catName = ""
    for x in range(maxLength):
        catLetters = ""
        for i in range(len(categories)):
            if x < lengths[i]:
                currentName = categories[i].name[x]
                catLetters += "{}  ".format(currentName)
            else:
                catLetters += "   "
        catName += "     {}\n".format(catLetters)

        # final
        result = "{}{}\n{}".format(chart, line, catName)
    
    print(result)

create_spend_chart([cloth, food, house, promise])