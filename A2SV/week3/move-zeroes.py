class Solution(object):
    def moveZeroes(self, nums):
        l=r=0
        n=len(nums)

        if n<2:
            return
        while r<n:
            if nums[l]!=0:
                l+=1
                r+=1
            elif nums[r]==0:
                r+=1
            else:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp    