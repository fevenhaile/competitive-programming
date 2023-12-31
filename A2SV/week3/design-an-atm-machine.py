class ATM:
    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.count = [0] * 5

    def deposit(self, banknotes_count: List[int]) -> None:
        for i in range(len(banknotes_count)):
            self.count[i] += banknotes_count[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawal_count = [0] * 5

        for i in range(len(self.denominations) - 1, -1, -1):
            used = min(amount // self.denominations[i], self.count[i])
            withdrawal_count[i] = used
            amount -= used * self.denominations[i]

        if amount != 0:
            return [-1]

        for i in range(len(self.denominations)):
            self.count[i] -= withdrawal_count[i]

        return withdrawal_count


