class Banking:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def showBalance(self):
        print(f"Account number = {self.account}\nTotal amount = {self.amount}")



    def deposit(self, amount):
        self.amount+=amount
        self.showBalance()
        print(f"deposited amount = {amount}")
        

    def withdraw(self, amount):
        if self.amount>amount:
            self.amount-=amount
            print(f"withdraw : {amount}")
            self.showBalance()
        else:
            print("low balance")


    def transfer(self, to_account : "Banking", amount):
        self.withdraw(amount)
        to_account.deposit(amount)
        \



account1= Banking(1,999999)
account1.deposit(1)
account1.withdraw(99999999999)
account1.withdraw(1000)

account2= Banking(2,0)
account1.transfer(account2,10)
account2.showBalance()
