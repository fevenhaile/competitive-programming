class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sums = []
        
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                x = nums[i] + nums[i+1] + nums[i+2]
                sums.append(x)
        
        if sums and len(sums) > 0:
            return max(sums)
        
        return 0  