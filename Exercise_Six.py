# Custom Exceptions
class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass


# Function to deposit money
def deposit(Amount):
    if Amount < 0:
        raise NegativeAmountError
    else:
        print(f"You have  Successfully Deposited {Amount}USD")


# Function to withdraw money
def withdraw(Amount,Balance=5000):
    if Amount < 0:
        raise NegativeAmountError
    if Amount > Balance:
        raise InsufficientFundsError
    else:
        print(f"You have Successfully Withdrawn {Amount}")


#To Deposit Money 
try:
    Deposit_Amount=int(input("Enter Amount you want to deposit: "))
    deposit(Deposit_Amount)
except NegativeAmountError:
    print("Amount cannot be Negative")

#To Withdraw Money
try: 
    Withdrawal_Amount=int(input("Enter Withdrawal Amount: "))
    withdraw(Withdrawal_Amount)
except NegativeAmountError:
    print("Amount Cannot be Negative")
except InsufficientFundsError:
    print("Insufficient Funds!")