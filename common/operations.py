"""Classes for 03_enkapsulacja.py"""


class DepositOperation:
    def __init__(self,  title: str, amount: float):
        self.title = title
        self.amount = amount


class WithdrawOperation:
    def __init__(self,  title: str, amount: float):
        self.title = title
        self.amount = amount
