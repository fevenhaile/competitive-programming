from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        impossible_nums = set()

        for i in range(n):
            if fronts[i] == backs[i]:
                impossible_nums.add(fronts[i])

        smallest_val = float('inf')
        for i in range(n):
            if fronts[i] not in impossible_nums:
                smallest_val = min(smallest_val, fronts[i])
            if backs[i] not in impossible_nums:
                smallest_val = min(smallest_val, backs[i])

        return smallest_val if smallest_val != float('inf') else 0