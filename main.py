from abc import ABC, abstractmethod

class BankAmount(ABC):
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
