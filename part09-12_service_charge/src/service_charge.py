# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self._owner = owner
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount: float):
        self._balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self._balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self._balance

    def __service_charge(self):
        self._balance -= 1/100 * self._balance


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
