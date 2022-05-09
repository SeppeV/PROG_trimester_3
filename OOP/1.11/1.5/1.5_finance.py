class Grouping:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0


    def deposit(self, amount, description=""):
        self.balance += amount
        dictionary = {description: amount}
        self.ledger.append(dictionary)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, group):
        self.withdraw(amount, f"Transfer to {group.name}")
        group.deposit(amount, "transfer")
         
def create_spend_chart(groups):
    pass