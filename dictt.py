class Bank_Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,deposit):
        self.balance = self.balance+deposit
        print(f"Mr.{self.name} your total balance after {deposit} deposit is {self.balance}")

    def withdraw(self,withdraw):
        if (withdraw > self.balance):
            raise ValueError("Insufficent balance")
        else:     
            self.balance = self.balance-withdraw
            print(f"Mr.{self.name} your total balance after {withdraw} withraw is {self.balance}")
class Savings_account(Bank_Account):
    def intrest(self):
        self.balance = self.balance+(self.balance*0.05)
        print(self.balance)
        
account = Savings_account("fahad",200000)
account.intrest()