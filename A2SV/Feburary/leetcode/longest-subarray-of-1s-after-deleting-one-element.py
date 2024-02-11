class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zerocounter = 0
        maxcount = 0
        l =  0
        r = 0
        
        while r < len(nums):
            if nums[r] == 0:
                zerocounter += 1
                
            while zerocounter > 1:
                if nums[l] == 0:
                    zerocounter -= 1
                l+=1
                
            maxcount = max(maxcount,r-l)
            r+=1
        return maxcount
            
            
            