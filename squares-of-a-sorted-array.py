class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]*nums[l]<=nums[r]*nums[r]:
                result.append(nums[r]*nums[r])
                r-=1
            else:
                result.append(nums[l]*nums[l])
                l+=1
        return result[::-1]