class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalsum = float('-inf') 
        currentsum = 0

        for i in nums:
            currentsum += i

            if currentsum > finalsum:
                finalsum = currentsum
            if currentsum < 0:
                currentsum = 0

        return finalsum