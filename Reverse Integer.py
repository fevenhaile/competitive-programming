class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        temp = str(x)[::-1]
        result = int(temp)

        if result >= 2**31 - 1:
            return 0
        elif is_negative:
            return -result
        else:
            return result