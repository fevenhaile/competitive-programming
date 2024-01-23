class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = []
        x = 0
        result = []
        totalsum = sum(nums)

        for i in range(len(nums)):
            x += nums[i]
            prefix.append(x)

        for i in range(len(prefix)):
            left_sum = prefix[i]  
            right_sum = totalsum - prefix[i] 
            left_count = i + 1 
            right_count = len(nums) - left_count  

            
            difference = (nums[i] * left_count - left_sum) + (right_sum - nums[i] * right_count)
            result.append(difference)

        return result