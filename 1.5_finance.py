class Grouping:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0


    def deposit(self, amount, description=""):
        self.balance += amount
        dictionary = {description: amount}
        self.ledger.append(dictionary)

def create_spend_chart(groups):
    pass