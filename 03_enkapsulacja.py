# TODO: move classes to modules
from common.operations import DepositOperation, WithdrawOperation


# To jest sposób na to by określić, że nasza klasa też jest wyjątkiem
class InsufficientAmountOnBankAccount(Exception):
    pass


class BankAccount:
    def __init__(self):
        self._operations = []

    def deposit(self, title: str, amount: float):
        self._operations.append(
           DepositOperation(title, amount)
        )

    def withdraw(self, title, amount: float):
        # TODO: Check if user can withdraw (enough cash)
        if amount > self.check_balance():
            raise InsufficientAmountOnBankAccount('You don\'t have enough money')

        self._operations.append(
            WithdrawOperation(title, amount)
        )

    def check_balance(self):
        # 0. Ustal zmienną lokalną balance (zdefiniowaną wewnątrz funkcji)
        # 1. Iteruj po self._operations
        # 2. Jeśli napotkasz na obiekt klasy DepositOperation (isinstance) to dodaj wartość do balansu
        # 3. Jeśli napotkasz na obiekt klasy WithdrawOperation (isinstance) to odejmij wartość do balansu
        # 4. Zwróć balans
        balance = 0
        for operation in self._operations:
            if isinstance(operation, DepositOperation):
                balance += operation.amount
            elif isinstance(operation, WithdrawOperation):
                balance -= operation.amount
            else:
                raise ValueError('Unknown operation type')

        return balance


account = BankAccount()
# account._operations.append(100)
# account.deposit('Wynagrodzenie', 4000)
account.deposit('Zwrot dojazdu', 300)
account.withdraw('Na imprezę', 200)
account.withdraw('Jedzenie', 500)

print('Tyle mi zostało', account.check_balance())

