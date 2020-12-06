class Category:
    def __init__(self, name):
        self.name = name
        self.initial_balance = 0
        self.ledger = list()

    def __str__(self):
        line = int((30 - len(self.name)) / 2) * '*' + self.name + int((30 - len(self.name)) / 2) * '*'
        for el in self.ledger:
            line += '\n' + (el['description'][:23] + (30 - len("{0:.2f}".format(el['amount'])[:7]) - len(el['description'][:23]))  * ' ' + ("{0:.2f}".format(el['amount'])[:7]))
        line += '\n' + f'Total: {self.get_balance()}'
        return line

    def deposit(self, amount, description = ''):
        self.initial_balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': - amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for op in self.ledger:
            balance += op['amount']
        return balance

    def transfer(self, amount, buget_category):
        if self.check_funds(amount):
            self.withdraw(amount, description = 'Transfer to ' + buget_category.name)
            buget_category.deposit(amount, description = 'Transfer from ' + self.name)
            return True
        return False
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def get_spent(self):
        try:
            spent_percent = 100 - int(100 * self.get_balance()/self.initial_balance)
        except:
            return 0
        if spent_percent % 10 < 5:
            spent_percent = (spent_percent // 10) * 10
        else:
            spent_percent = (spent_percent // 10) * 10 + 10
        return spent_percent


def create_spend_chart(categories):
    longest_name = ''
    chart = 'Percentage spent by category'
    for pourcentage in range(100, -10, -10):
        chart += '\n' + (3 - len(str(pourcentage))) * ' ' + str(pourcentage) + '|' 
        for category in categories:
            if category.get_spent() >= pourcentage:
                chart += ' o '
            else:
                chart += '   '
    chart += '\n' + 4 * ' '
    for category in categories:
        chart += '---'
        if len(category.name) > len(longest_name):
            longest_name = category.name
    chart += '-'
    for i in range(len(longest_name) + 1):
        for category in categories:
            if category.name[i-1:i]:
                chart += category.name[i-1:i] + 2 * ' '
            else:
                chart += 3 * ' '
        # quick fix
        if not (i == len(longest_name)):
            chart += '\n' + 5 * ' '
    return chart


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(food)
print(entertainment)
print(business)

expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(create_spend_chart([business, food, entertainment]))
print(expected)