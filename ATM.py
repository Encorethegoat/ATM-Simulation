class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance!")


def menu():
    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    atm = ATM(5000)

    while True:
        menu()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))
            atm.withdraw(amount)

        elif choice == 4:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")


main()