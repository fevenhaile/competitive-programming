class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False
            visited.add(n)

            next_num = 0
            while n > 0:
                digit = n % 10
                next_num += digit ** 2
                n //= 10
            n = next_num

        return True