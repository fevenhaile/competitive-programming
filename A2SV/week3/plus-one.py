class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join(str(d) for d in digits)
        y = list(str(int (x) +1))
        for i in range(len(y)):
            y[i] = int(y[i])
        return y



       

        