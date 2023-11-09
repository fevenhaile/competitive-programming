class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and nums[j] < nums[i]:
                    count += 1
            result.append(count)
        
        return result