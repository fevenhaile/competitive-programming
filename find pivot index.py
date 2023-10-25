class Solution(object):
    def pivotIndex(self, nums):
        totalsum=sum(nums)
        left=0
        for i in range (len(nums)):
            right=totalsum-left-nums[i]

            if right==left:
                return i
            
            left+=nums[i]

        return -1
        