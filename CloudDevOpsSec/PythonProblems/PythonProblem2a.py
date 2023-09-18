class BankAccount:
    def __init__(self, AccountHolderName, AccountNumber):
        self.AccountHolderName = AccountHolderName
        self.AccountNumber = AccountNumber
        self.balance = 0
        print("Hello {}!!! Welcome to the Deposit & Withdrawal Machine".format(self.AccountHolderName))
	
    def deposit(self):
        amount= float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited: ",amount)
	
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew: ",amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Available Balance = ",self.balance)
