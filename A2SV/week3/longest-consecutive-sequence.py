from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        streak = 0

        for n in num:
            if n - 1 not in num:
                current_num = n
                current_streak = 1

                while current_num + 1 in num:
                    current_num += 1
                    current_streak += 1

                if current_streak > streak:
                    streak = current_streak

        return streak