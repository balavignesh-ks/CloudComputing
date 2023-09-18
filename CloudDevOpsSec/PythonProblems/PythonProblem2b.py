from PythonProblem2a import BankAccount

AccountHolderName = input("Enter your name: \n")
AccountNumber = input("Enter your account number: \n")
p = BankAccount(AccountHolderName,AccountNumber)

def menu():
    check = True

    while check:
        print("\nWhat would you like to do?\n")
        print("1. Deposit\n")
        print("2. Withdraw\n")
        print("3. View Balance\n")
        print("Please enter 1,2 or 3 to perform any of the above operations. If you want to quit enter quit \n")
        response=input()

        if response == "1":
            p.deposit()
        elif response == "2":
            p.withdraw()
        elif response == "3":
            p.display()
        elif response == "quit":
            print("\nQuitting Thank You!!!\n")
            exit()
        else:
            print("\nInvalid Option!!!\n")
        
        resp = input("\nWould like to continue (yes\\no)? ")
        if resp == "no":
            check = False
            print("\nQuitting Thank You!!!\n")
        else:
            check = True

dummy = menu()