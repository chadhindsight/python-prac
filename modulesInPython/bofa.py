# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance =0.0):
        self.owner = owner
        self.balance = balance
    
    def getBalance(self):
        return self.balance
        
    def deposit(self, num):
        self.balance += num
        return self.balance
    
    def withdraw(self, num):
        self.balance -= num
        return self.balance
        # bs push