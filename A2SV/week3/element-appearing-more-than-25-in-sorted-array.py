from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4

        num_count = {}
        for num in arr:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

            if num_count[num] > threshold:
                return num

        return -1