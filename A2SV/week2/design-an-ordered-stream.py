class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.ha = {}
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ha[idKey] = value
        result = []
        while self.ptr in self.ha:
            result.append(self.ha[self.ptr])
            self.ptr += 1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)