print("*********************")
intro = "Banking Program"
print(f"{intro:>18}")
print("*********************")
choice = 0
balance = 0


def bank_balance(balance_amount):
    print("*********************")
    print(f"Your bank balance is Rs.{balance_amount}")
    print("*********************")

def deposit(balance_amount):
    print("*********************")
    deposit_amount = int(input("Enter the amount to be deposited:\n"))
    balance_amount += deposit_amount
    print("*********************")
    return balance_amount

def withdraw(balance_amount):
    print("*********************")
    withdraw_amount = int(input("Enter the amount you want to withdraw:\n"))
    if withdraw_amount > balance_amount:
        print("sorry, but you have insufficient balance in your bank account to withdraw such amount")
        withdraw(balance_amount)
    balance_amount -= withdraw_amount
    print("*********************")
    return balance_amount


while(choice != 4):
    print("1. Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    print("*********************")
    choice = int(input("Enter your choice (1-4):\n"))
    if 1 == choice:
        bank_balance(balance)
    elif 2 == choice:
        balance = deposit(balance)
    elif 3 == choice:
        balance = withdraw(balance)
    elif 4 != choice:
        print("You have entered invalid character, please try again.")

