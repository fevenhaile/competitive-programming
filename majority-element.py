class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        # Finding the potential majority candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate