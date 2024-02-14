class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        unique = set()
        sums = 0
        maxim = 0
        
        while r < len(nums):
            if nums[r] not in unique:
                unique.add(nums[r])
                sums += nums[r]
                maxim = max(maxim,sums)
                r += 1

            else:
                sums -= nums[l]
                unique.remove(nums[l])
                l += 1
             
        
       
        return maxim

            