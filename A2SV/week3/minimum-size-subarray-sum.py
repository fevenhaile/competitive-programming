class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        sums = 0
        minim = float('inf')  # Initialize minim to infinity
        
        if sum(nums) < target:
            return 0

        for r in range(len(nums)):
            sums += nums[r]
            while sums >= target:
                minim = min(minim, r - l + 1)
                sums -= nums[l]
                l += 1
            
                
        # If minim is still infinity, it means no subarray was found
        if minim == float('inf'):
            return 0
        
        return minim