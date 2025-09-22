#Concept of Encapsulation and Abstraction
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, account_number, account_holder_name, balance = 0):
        self.account_number = account_number
        self.account_holder_number = account_holder_name
        self.__balance = balance #Encapsulating the balance : private attribute

    #using property to access the private attribute
    @property
    def balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance : {self.__balance}")
        else:
            print("Deposit amount should be positive.")
    
    @abstractmethod
    def withdraw(self, amount):
        pass


#Concept of Polymorphism and Inheritance
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self._BankAccount__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance + 1000:  # overdraft limit
            print("Exceeded overdraft limit!")
        else:
            self._BankAccount__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")



class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        account_type = input("Enter account type (savings/current): ").lower()
        account_number = int(input("Enter account number: "))
        holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))

        if account_type == "savings":
            account = SavingsAccount(account_number, holder_name, initial_balance)
        elif account_type == "current":
            account = CurrentAccount(account_number, holder_name, initial_balance)
        else:
            print("Invalid account type!")
            return

        self.accounts.append(account)
        print(f"{account_type.capitalize()} account created for {holder_name}!")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        print("Account not found!")
        return None

    def deposit_money(self):
        acc = self.find_account(int(input("Enter account number: ")))
        if acc:
            acc.deposit(float(input("Enter amount to deposit: ")))

    def withdraw_money(self):
        acc = self.find_account(int(input("Enter account number: ")))
        if acc:
            acc.withdraw(float(input("Enter amount to withdraw: ")))

    def transfer_money(self):
        from_acc = self.find_account(int(input("Enter sender account number: ")))
        to_acc = self.find_account(int(input("Enter receiver account number: ")))
        if from_acc and to_acc:
            amount = float(input("Enter amount to transfer: "))
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print("Transfer successful!")

    def show_account_details(self):
        acc = self.find_account(int(input("Enter account number: ")))
        if acc:
            print(f"Account Number: {acc.account_number}")
            print(f"Holder Name: {acc.holder_name}")
            print(f"Balance: {acc.balance}")



def main():
    bank = Bank()
    while True:
        print("\nWelcome to ABC Bank!")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Show Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_money()
        elif choice == "3":
            bank.withdraw_money()
        elif choice == "4":
            bank.transfer_money()
        elif choice == "5":
            bank.show_account_details()
        elif choice == "6":
            print("Thank you for using ABC Bank!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
