class DepositOperation:
    def __init__(self,  title: str, amount: float):
        self.title = title
        self.amount = amount


class WithdrawOperation:
    def __init__(self,  title: str, amount: float):
        self.title = title
        self.amount = amount


class BankAccount:
    def __init__(self):
        self.operations = []

    def deposit(self, title: str, amount: float):
        self.operations.append(
           DepositOperation(title, amount)
        )

    def withdraw(self, title, amount: float):
        self.operations.append(
            WithdrawOperation(title, amount)
        )

    def check_balance(self):
        # 0. Ustal zmienną lokalną balance (zdefiniowaną wewnątrz funkcji)
        # 1. Iteruj po self.operations
        # 2. Jeśli napotkasz na obiekt klasy DepositOperation (isinstance) to dodaj wartość do balansu
        # 3. Jeśli napotkasz na obiekt klasy WithdrawOperation (isinstance) to odejmij wartość do balansu
        # 4. Zwróć balans
        balance = 0
        for operation in self.operations:
            if isinstance(operation, DepositOperation):
                balance += operation.amount
            elif isinstance(operation, WithdrawOperation):
                balance -= operation.amount
            else:
                pass
                # TODO: throw exception if operation is unknown type

        return balance


account = BankAccount()
account.deposit('Wynagrodzenie', 4000)
account.deposit('Zwrot dojazdu', 300)
account.withdraw('Na imprezę', 200)
account.withdraw('Jedzenie', 500)

print('Tyle mi zostało', account.check_balance())

