class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.val = 0
        self.full = 2**(size) - 1
        self.c = 0  # count

    def fix(self, idx: int) -> None:
        if not (self.val & (1 << idx)):
            self.c += 1
        self.val |= (1 << idx)

    def unfix(self, idx: int) -> None:
        s = 2**idx
        if self.val & s:
            self.c -= 1
        self.val &= (self.full - s)

    def flip(self) -> None:
        self.val = self.full - self.val
        self.c = self.size - self.c

    def all(self) -> bool:
        return self.val == self.full

    def one(self) -> bool:
        return self.val != 0

    def count(self) -> int:
        return self.c

    def toString(self) -> str:
        fmt = format(self.val, 'b')
        z = ''
        if len(fmt) < self.size:
            z = ''.join(['0'] * (self.size - len(fmt)))
        return fmt[::-1] + z