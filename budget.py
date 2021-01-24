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
food.deposit(500,"food3")
house.deposit(500,"food3")
food.withdraw(100,"food2")
house.withdraw(100,"food2")
# # cloth.deposite(500)

# # print(food.get_balance())
# print(cloth.ledger)
# print(str(food))
# print(food.ledger)


def create_spend_chart(categories):
    # withdrawal count
    withdrawArr = []
    for i in range(len(categories)):
        total = 0
        for x in range(len(categories[i].ledger)):
            if categories[i].ledger[x]["amount"] < 0:
                total += categories[i].ledger[x]["amount"]
        withdrawArr.append(abs(total))

    # withdraw percentage: (category_spent/total_spent)*100
    total_spent = 0
    for i in withdrawArr:
        total_spent += i
    
    category_spent = []
    for i in withdrawArr:
        perc = round((i/total_spent)*100)
        modu = perc%10
        round_value = perc-modu
        category_spent.append(round_value)
    
    # draw axis
    chart = ""
    for i in range(100, -1, -10):
        # place points
        dot = ""
        for x in category_spent:
            if i<=x:
                dot += "{}".format(" o ")
            else:
                dot += "   "
        chart += "{:>3}{}{}\n".format(i, "|", dot)
        
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