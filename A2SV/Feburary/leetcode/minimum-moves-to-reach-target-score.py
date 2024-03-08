class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        countdouble = 0
        operations = 0
        while target > 1:
            if maxDoubles == countdouble:
                operations += target-1
                break
            elif target % 2 == 0 and countdouble < maxDoubles:
                target //= 2
                countdouble += 1
            else:
                target -= 1
            operations += 1
        return operations
